"""
Week 1 Saturday drill - SQL joins + aggregation, zero setup.

Same protocol: predict before you run. Uses sqlite3 (Python stdlib, no
install, no server) as a real, in-process database - not a syntax quiz.
You'll move this exact reasoning onto real Postgres in Week 3-4.
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


def run(label, sql, why):
    print(f"=== {label} ===")
    print(sql.strip())
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print(cols)
    for r in rows:
        print(r)
    print(f"why: {why}\n")


run(
    "1. INNER JOIN - only rows that match on both sides",
    """
    SELECT e.name, d.name AS dept
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id;
    """,
    "Deja has department_id = NULL, matches no department row, and simply "
    "vanishes from the result. INNER JOIN keeps only pairs that matched."
)

run(
    "2. LEFT JOIN - every row from the left table, matched or not",
    """
    SELECT e.name, d.name AS dept
    FROM employees e
    LEFT JOIN departments d ON e.department_id = d.id;
    """,
    "Deja is back, with dept = NULL. This is your diagnostic question, live: "
    "LEFT JOIN keeps every left-side row and fills unmatched right columns with NULL."
)

run(
    "3. GROUP BY + aggregation - one row per group",
    """
    SELECT d.name AS dept, COUNT(*) AS headcount, AVG(e.salary) AS avg_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    GROUP BY d.name;
    """,
    "Legal has zero employees and disappears entirely (it's an INNER JOIN feeding "
    "the GROUP BY) - Legal never gets a 0-headcount row. Aggregation only sees rows "
    "that survived the join above it."
)

run(
    "4. HAVING vs WHERE - filter rows, or filter groups?",
    """
    SELECT d.name AS dept, AVG(e.salary) AS avg_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    WHERE e.salary > 65000
    GROUP BY d.name
    HAVING AVG(e.salary) > 70000;
    """,
    "WHERE runs first and removes Chen (60000) as an individual ROW, before any "
    "grouping happens. HAVING runs after grouping and would remove a whole "
    "DEPARTMENT if its post-filter average were too low."
)

print("=== 5. The classic gotcha - can you filter on a SELECT alias in WHERE? ===")
print("SELECT name, salary * 1.1 AS raised FROM employees WHERE raised > 90000;")
cur.execute("SELECT name, salary * 1.1 AS raised FROM employees WHERE raised > 90000;")
print(cur.fetchall())
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

print("=== Self-check ===")
print("Before running: did you expect Legal to vanish in query #3, or show headcount 0?")
print("Before running: did you expect query #5 to work, or to error?")
print("Getting either wrong is exactly why 'execution order' beats 'clause order.'")
