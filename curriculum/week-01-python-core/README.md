# Week 1 — Python for Interviews I (Aug 24–30)

You write Python daily at work — this week converts "working Python" into **interview Python**: idiomatic, fast, and with big-O awareness of every builtin you touch.

## Objectives — by Sunday you can:

1. Choose the right structure (list/tuple/set/dict/Counter/defaultdict/deque) and state the big-O of its operations
2. Write comprehensions and generator expressions fluently (incl. dict/set comprehensions)
3. Sort anything: `key=`, multi-key sorts, `reverse`, stability — and explain Timsort is O(n log n)
4. Manipulate strings without O(n²) traps (`join` vs `+=`, slicing, `str` methods)
5. Explain: mutability, `is` vs `==`, shallow vs deep copy, why `[[0]*3]*2` is a bug

## Monday drill (~45 min) — predict, run, compare

Run [gotchas.py](gotchas.py) — but read each numbered block and write down your predicted output *before* running it. Then run the whole file (`python gotchas.py`) and check your predictions against the real output and the one-line "why" printed after each. 8 blocks, covering exactly your diagnostic misses (comprehension+filter, hashability, sorted+stability) plus multi-key sort and big-O of `in`/`pop(0)` — measured with `timeit`, not memorized off a table.

No doc reading required first. If a block surprises you even after seeing the "why," *then* the [Data Structures tutorial](https://docs.python.org/3/tutorial/datastructures.html) or [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) are there as backup — reference, not homework.

## Deliverable 1 — Exercises (the core work)

Implement all 12 functions in [exercises.py](exercises.py). Check yourself anytime:

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
