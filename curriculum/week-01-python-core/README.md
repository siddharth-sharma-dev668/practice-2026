# Week 1 — Python for Interviews I (Aug 24–30)

You write Python daily at work — this week converts "working Python" into **interview Python**: idiomatic, fast, and with big-O awareness of every builtin you touch.

## Objectives — by Sunday you can:

1. Choose the right structure (list/tuple/set/dict/Counter/defaultdict/deque) and state the big-O of its operations
2. Write comprehensions and generator expressions fluently (incl. dict/set comprehensions)
3. Sort anything: `key=`, multi-key sorts, `reverse`, stability — and explain Timsort is O(n log n)
4. Manipulate strings without O(n²) traps (`join` vs `+=`, slicing, `str` methods)
5. Explain: mutability, `is` vs `==`, shallow vs deep copy, why `[[0]*3]*2` is a bug

## Concept lessons — on the platform, not here

Each of this week's three concept days (Mon Python, Thu AI/ML, Sat SQL) has a full lesson on the Launchpad platform (Roadmap → Week 1 → **Concepts**): a flowchart of the actual mechanism, senior-level explanation text, a short code reference, and a ready-to-paste PowerShell command — all on one page. Open the lesson *before* running that day's drill file; the drill is where you verify what the lesson claims.

## Monday drill (~45 min) — predict, run, compare

Run `python gotchas.py`. The script itself stops and asks — it shows you a block of code, asks a plain-English question, then waits at a prompt. Type anything (a guess, "no idea," whatever) and press Enter; the real answer prints immediately after, with a "why." You don't write your guess anywhere else — typing it into the terminal IS the exercise. 8 blocks, covering exactly your diagnostic misses (comprehension+filter, hashability, sorted+stability) plus multi-key sort and big-O of `in`/`pop(0)` — measured with `timeit`, not memorized off a table.

No doc reading required first. If a block surprises you even after seeing the "why," *then* the [Data Structures tutorial](https://docs.python.org/3/tutorial/datastructures.html) or [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) are there as backup — reference, not homework.

## Monday bonus (~15 min) — the same lesson in Java

Your DSA foundation is Java-first (college), your daily driver now is Python (JCI) — both need reinforcing, not just one. Run [Gotchas.java](Gotchas.java) the same way: `java Gotchas.java` (JDK 11+ runs a single file directly, no `javac` step). It targets your *other* diagnostic's one soft spot — Collections, 3/4 — with the ArrayList-vs-LinkedList cost, HashSet/HashMap hashing, `ConcurrentModificationException`, and the hashCode-mutation gotcha, all measured live. The platform's "Choosing a data structure" lesson has the bilingual diagram and a Python/Java code reference side by side.

## Thursday drill (~45 min) — LLM basics

Same protocol, run [llm_basics.py](llm_basics.py): tokens vs words vs characters, why a context window is a hard cutoff, and temperature reshaping the same logits into different sampled outputs. Zero dependencies, zero API key — the mental model under the Claude API call you'll make in Week 3.

## Saturday drill (~45 min) — SQL joins + aggregation

Run [sql_playground.py](sql_playground.py): a real in-process database (`sqlite3`, stdlib, zero setup) walking INNER vs LEFT JOIN, GROUP BY + aggregation, WHERE vs HAVING, and a genuine alias gotcha that proves why execution order beats typed order. Same reasoning moves onto real Postgres in Week 3-4.

Then solve on the real judge — same LeetCode account as your DSA problems, picked to match today exactly:
- [175 Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) (LEFT JOIN)
- [596 Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) (GROUP BY + HAVING)
- [181 Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) (self-join)

## Deliverable 1 — Exercises (the core work)

Implement all 12 functions in [exercises.py](exercises.py). Before you open the file, open the platform (Roadmap → Week 1 → **Write it yourself**) — it has all 12, in a suggested Tuesday/Friday order: the problem in plain words, a design question to answer *before* you write any code (what approach, what data structure, why), one hint if you're stuck, and exactly which function to edit. No solutions on that page, on purpose — that's what `check.py` and `grade week 1` are for. Check yourself anytime:

```bash
python check.py
```

Target: **12/12 by Sunday.** No AI assistance for these — the point is your fluency. Docs are allowed.

## Deliverable 2 — DSA set (LeetCode, arrays & hashing)

| # | Problem | Target |
|---|---|---|
| 217 | Contains Duplicate | Easy — under 10 min |
| 242 | Valid Anagram | Easy — under 10 min |
| 1 | Two Sum | Easy — under 10 min |
| 49 | Group Anagrams | Medium |
| 347 | Top K Frequent Elements | Medium |
| 238 | Product of Array Except Self | Medium |

You'll meet several of these in `exercises.py` first — that's deliberate. Solve there, then submit the class-based version on LeetCode. Save your solutions in a `dsa/` folder here (one file per problem) so I can review your approach, not just the accept.

## Deliverable 3 — Quiz

Platform → Quizzes → **Week 1: Python for Interviews** (15 questions). Take it Sunday, after the exercises.

## Deliverable 4 — One STAR story (15 min)

Create `interview-prep/stories.md` and write your first story: **the Onextel p95-latency-by-20% bullet** — Situation, Task, Action (what YOU specifically did: which queries, what profiling, why Redis), Result (how measured). This is the story every backend interviewer will pull first.

## Done? Say `grade week 1` in chat.
