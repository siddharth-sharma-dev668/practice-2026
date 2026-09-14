# Week 1 — Python for Interviews I (Aug 24–30)

You write Python daily at work — this week converts "working Python" into **interview Python**: idiomatic, fast, and with big-O awareness of every builtin you touch.

## Objectives — by Sunday you can:

1. Choose the right structure (list/tuple/set/dict/Counter/defaultdict/deque) and state the big-O of its operations
2. Write comprehensions and generator expressions fluently (incl. dict/set comprehensions)
3. Sort anything: `key=`, multi-key sorts, `reverse`, stability — and explain Timsort is O(n log n)
4. Manipulate strings without O(n²) traps (`join` vs `+=`, slicing, `str` methods)
5. Explain: mutability, `is` vs `==`, shallow vs deep copy, why `[[0]*3]*2` is a bug

## Everyday path: the platform, not this folder

Most days you don't need to open anything in this folder at all. Roadmap → Week 1 → **Concepts** has the flowchart + explanation for each concept day, and **Practice** (right below it) has the same predict-then-reveal drill as the matching `.py`/`.java` file, done entirely in the browser — type a guess, click Reveal, see the real answer and the "why." No VS Code, no terminal, no editor.

The files in this folder (`gotchas.py`, `Gotchas.java`, `llm_basics.py`, `sql_playground.py`) still exist and still work exactly as described below — that's the *deeper* option, for when you want an actual interpreter running your guess through real code, not the *required* one. Use whichever fits the day you're having.

## Monday drill (~45 min) — predict, run, compare

**Browser:** Week 1 → Practice → "gotchas.py - in your browser."
**Real file:** Run `python gotchas.py`. The script itself stops and asks — it shows you a block of code, asks a plain-English question, then waits at a prompt. Type anything (a guess, "no idea," whatever) and press Enter; the real answer prints immediately after, with a "why." 8 blocks, covering exactly your diagnostic misses (comprehension+filter, hashability, sorted+stability) plus multi-key sort and big-O of `in`/`pop(0)` — measured with `timeit`, not memorized off a table.

No doc reading required first. If a block surprises you even after seeing the "why," *then* the [Data Structures tutorial](https://docs.python.org/3/tutorial/datastructures.html) or [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) are there as backup — reference, not homework.

## Monday bonus (~15 min) — the same lesson in Java

Your DSA foundation is Java-first (college), your daily driver now is Python (JCI) — both need reinforcing, not just one. **Browser:** Practice → "Gotchas.java - in your browser." **Real file:** `java Gotchas.java` (JDK 11+ runs a single file directly, no `javac` step). Either way it targets your *other* diagnostic's one soft spot — Collections, 3/4 — with the ArrayList-vs-LinkedList cost, HashSet/HashMap hashing, `ConcurrentModificationException`, and the hashCode-mutation gotcha. The platform's "Choosing a data structure" lesson has the bilingual diagram and a Python/Java code reference side by side.

## Thursday drill (~45 min) — LLM basics

**Browser:** Practice → "llm_basics.py - in your browser" (fully deterministic — your answers will match exactly, not just roughly). **Real file:** [llm_basics.py](llm_basics.py) — tokens vs words vs characters, why a context window is a hard cutoff, and temperature reshaping the same logits into different sampled outputs. Zero dependencies, zero API key — the mental model under the Claude API call you'll make in Week 3.

## Saturday drill (~45 min) — SQL joins + aggregation

**Browser:** Practice → "sql_playground.py - in your browser." **Real file:** [sql_playground.py](sql_playground.py) — a real in-process database (`sqlite3`, stdlib, zero setup) walking INNER vs LEFT JOIN, GROUP BY + aggregation, WHERE vs HAVING, and a genuine alias gotcha that proves why execution order beats typed order. Same reasoning moves onto real Postgres in Week 3-4.

Then solve on the real judge — same LeetCode account as your DSA problems, picked to match today exactly:
- [175 Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) (LEFT JOIN)
- [596 Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) (GROUP BY + HAVING)
- [181 Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) (self-join)

## Deliverable 1 — Pulse's spec (the core work, Tue + Fri)

~~Implement 12 functions in exercises.py~~ — retired 2026-09-06. Four of those functions were the exact same problems as Deliverable 2 below, and the rest were DSA patterns your own thread already schedules for later weeks — redundant work, not two different skills.

Instead: open `pulse/SPEC.md` and write it. Five prompts, no answers given — what Pulse actually is in your own words, one event sketched as JSON, the architecture one hop at a time, the repo layout Week 2 builds, and a running reference table so you're not flipping back to `MASTER_PLAN.md` mid-week. This is design-first, then-code — the same muscle as "design it first" in the old exercises guide, just aimed at the thing that's actually unique this week instead of duplicating Wednesday.

## Deliverable 2 — DSA set (LeetCode, arrays & hashing — the single source for algorithm problems)

| # | Problem | Target |
|---|---|---|
| 217 | Contains Duplicate | Easy — under 10 min |
| 242 | Valid Anagram | Easy — under 10 min |
| 1 | Two Sum | Easy — under 10 min |
| 49 | Group Anagrams | Medium |
| 347 | Top K Frequent Elements | Medium |
| 238 | Product of Array Except Self | Medium |

Solve the first two on LeetCode; the rest are stretch. Save each solution as a file in a `dsa/` folder here so I can review your approach, not just the accept.

## Deliverable 3 — Quiz

Platform → Quizzes → **Week 1: Python for Interviews** (15 questions). Take it Sunday, after the drills.

## Deliverable 4 — One STAR story (15 min)

Create `interview-prep/stories.md` and write your first story: **the Onextel p95-latency-by-20% bullet** — Situation, Task, Action (what YOU specifically did: which queries, what profiling, why Redis), Result (how measured). This is the story every backend interviewer will pull first.

## Done? Say `grade week 1` in chat.
