"""
Week 1 Saturday drill - SQL joins + aggregation, zero setup.

HOW TO USE THIS FILE: run `python sql_playground.py`. The terminal shows you a
query and ASKS a question, then waits. Type anything - your guess, "no idea" -
and press Enter. The real query result prints right after, with a "why".
Uses sqlite3 (Python stdlib, no install, no server) as a real, in-process
database - not a syntax quiz. You'll move this exact reasoning onto real
Postgres in Week 3-4.
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT, salary INTEGER, department_id INTEGER
);
INSERT INTO departments VALUES (1, 'Engineering'), (2, 'Sales'), (3, 'Legal');
INSERT INTO employees VALUES
    (1, 'Ana',   90000, 1),
    (2, 'Bo',    70000, 1),
    (3, 'Chen',  60000, 2),
    (4, 'Deja',  85000, NULL);   -- contractor, no department yet
""")

print("THE DATA (fixed for every question below):")
print("  departments: (1, Engineering) (2, Sales) (3, Legal)")
print("  employees:   (1, Ana, 90000, dept 1)  (2, Bo, 70000, dept 1)")
print("               (3, Chen, 60000, dept 2)  (4, Deja, 85000, dept NULL)")


def predict(block_num, title, sql_shown, question):
    print(f"\n{'=' * 70}")
    print(f"BLOCK {block_num}: {title}")
    print(f"{'=' * 70}")
    print("QUERY:")
    for line in sql_shown.strip("\n").split("\n"):
        print("    " + line.strip())
    print()
    print("QUESTION:", question)
    input(">>> Type your guess, then press Enter to reveal the real answer: ")
    print()


def run(sql):
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print("ACTUAL ANSWER:")
    print("   ", cols)
    for r in rows:
        print("   ", r)
    print()


predict(1, "INNER JOIN - only rows that match on both sides",
    "SELECT e.name, d.name AS dept FROM employees e\nINNER JOIN departments d ON e.department_id = d.id;",
    "Deja has no department. Does Deja show up in the result at all?")
run("SELECT e.name, d.name AS dept FROM employees e INNER JOIN departments d ON e.department_id = d.id;")
print("why: Deja has department_id = NULL, matches no department row, and simply")
print("     vanishes from the result. INNER JOIN keeps only pairs that matched.\n")


predict(2, "LEFT JOIN - every row from the left table, matched or not",
    "SELECT e.name, d.name AS dept FROM employees e\nLEFT JOIN departments d ON e.department_id = d.id;",
    "Same question, different join. Does Deja show up this time - and if so, what's her dept?")
run("SELECT e.name, d.name AS dept FROM employees e LEFT JOIN departments d ON e.department_id = d.id;")
print("why: Deja is back, with dept = NULL. This is your diagnostic question, live:")
print("     LEFT JOIN keeps every left-side row and fills unmatched right columns with NULL.\n")


predict(3, "GROUP BY + aggregation - one row per group",
    "SELECT d.name AS dept, COUNT(*) AS headcount, AVG(e.salary) AS avg_salary\n"
    "FROM employees e JOIN departments d ON e.department_id = d.id\nGROUP BY d.name;",
    "Legal has ZERO employees. Does Legal show up with headcount 0, or does it vanish entirely?")
run("SELECT d.name AS dept, COUNT(*) AS headcount, AVG(e.salary) AS avg_salary "
    "FROM employees e JOIN departments d ON e.department_id = d.id GROUP BY d.name;")
print("why: Legal disappears entirely (it's an INNER JOIN feeding the GROUP BY) -")
print("     Legal never gets a 0-headcount row. Aggregation only sees rows that")
print("     survived the join above it.\n")


predict(4, "HAVING vs WHERE - filter rows, or filter groups?",
    "SELECT d.name AS dept, AVG(e.salary) AS avg_salary\n"
    "FROM employees e JOIN departments d ON e.department_id = d.id\n"
    "WHERE e.salary > 65000\nGROUP BY d.name\nHAVING AVG(e.salary) > 70000;",
    "Chen earns 60000 (fails the WHERE). Sales only has Chen. Does Sales show up in the result at all?")
run("SELECT d.name AS dept, AVG(e.salary) AS avg_salary FROM employees e "
    "JOIN departments d ON e.department_id = d.id WHERE e.salary > 65000 "
    "GROUP BY d.name HAVING AVG(e.salary) > 70000;")
print("why: WHERE runs first and removes Chen (60000) as an individual ROW, before")
print("     any grouping happens - so Sales has nobody left and never even forms a")
print("     group. HAVING runs after grouping and would remove a whole DEPARTMENT")
print("     if its post-filter average were too low - a different failure mode.\n")


predict(5, "The classic gotcha - alias inside your own WHERE clause",
    "SELECT name, salary * 1.1 AS raised FROM employees\nWHERE raised > 90000;",
    "'raised' is an alias YOU just invented in the SELECT list. Does WHERE know what "
    "'raised' means, or does this error out?")
run("SELECT name, salary * 1.1 AS raised FROM employees WHERE raised > 90000;")
print("why: this WORKED - and if you predicted an error, you predicted correctly for")
print("     the rule, just not for SQLite specifically. The rule is real: WHERE runs")
print("     BEFORE SELECT (FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY is")
print("     the true order, not the order you type), so 'raised' shouldn't exist yet")
print("     when WHERE runs. Verified for real on 2026-09-06 (a throwaway Postgres 16")
print("     container, docker run postgres:16-alpine): the identical query fails with")
print("     ERROR: column \"raised\" does not exist. MySQL and SQL Server are widely")
print("     documented to reject it for the same reason, but that part was NOT run in")
print("     this session - treat it as likely, not verified, until you check yourself.")
print("     SQLite is the outlier here, not the rule. The bigger lesson: your LOCAL dev")
print("     database (SQLite, zero setup) can silently accept something your DEPLOYED")
print("     database (Postgres, from Week 3) will reject. Re-run this exact query once")
print("     Pulse has real Postgres and see for yourself - don't take this file's word")
print("     for it either.\n")

conn.close()

print(f"\n{'=' * 70}")
print("SELF-CHECK")
print(f"{'=' * 70}")
print("Were your 5 guesses right? Getting #3 or #5 wrong is exactly why")
print("'execution order' beats memorizing clause order.")
