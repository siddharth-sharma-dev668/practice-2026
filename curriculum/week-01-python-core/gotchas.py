"""
Week 1 Monday drill - predict, THEN run, then compare.

Protocol: for each numbered block, read the code and write down (paper,
notes app, whatever) what you think it prints. Only then run this file
top to bottom: `python gotchas.py`. Every block prints its own answer
plus a one-line "why" immediately after, so you self-grade instantly -
no tab-switching to docs.

This replaces reading the Python docs cover to cover. It targets your
three actual diagnostic misses (comprehension+filter, hashability,
sorted+stability) plus the big-O-of-builtins objective, and drills the
one thing your warm-up showed you skip: running it before trusting it.
"""

print("=== 1. Comprehension with a filter (your diagnostic Q2) ===")
result = [x * x for x in range(6) if x % 2]
print(result)
print("why: x % 2 is truthy only for odd x -> 1,3,5 survive -> squares 1,9,25\n")


print("=== 2. Hashability - what can be a dict key? (your diagnostic Q3) ===")
try:
    bad_key = {[1, 2]: "value"}
    print(bad_key)
except TypeError as e:
    print(f"TypeError: {e}")
good_key = {(1, 2): "value"}
print(good_key)
print("why: dict keys must be hashable. Lists are mutable -> unhashable.")
print("     Tuples are hashable IF every element inside them is too.\n")


print("=== 3. sorted(key=len) + stability (your diagnostic Q6) ===")
words = ["pear", "fig", "plum", "kiwi", "date"]
print(sorted(words, key=len))
print("why: sorted() always returns a NEW list. Timsort is stable, so")
print("     'plum' and 'kiwi' (both len 4) keep their original relative order.\n")


print("=== 4. Multi-key sort - extend #3 ===")
people = [("sid", 27), ("ana", 27), ("bo", 19)]
print(sorted(people, key=lambda p: (-p[1], p[0])))
print("why: tuple keys sort left-to-right - here: age descending, then name ascending.\n")


print("=== 5. Big-O of `in`: list scan vs set hash - measured, not memorized ===")
import timeit
haystack_list = list(range(20000))
haystack_set = set(haystack_list)
t_list = timeit.timeit(lambda: 19999 in haystack_list, number=1000)
t_set = timeit.timeit(lambda: 19999 in haystack_set, number=1000)
print(f"list: {t_list:.5f}s   set: {t_set:.5f}s   ratio: {t_list / t_set:.0f}x")
print("why: list.__contains__ is O(n) - it scans. set.__contains__ hashes straight")
print("     to the bucket, O(1) average. You just measured it instead of reading it.\n")


print("=== 6. Counter - tally + top-k in one line ===")
from collections import Counter
c = Counter("mississippi")
print(c.most_common(2))
print("why: most_common(k) returns [(elem, count), ...] sorted by count, highest first.\n")


print("=== 7. defaultdict - skip the 'if key not in dict' boilerplate ===")
from collections import defaultdict
groups = defaultdict(list)
for word in ["ant", "bee", "ape", "bat"]:
    groups[word[0]].append(word)
print(dict(groups))
print("why: defaultdict(list) auto-creates [] on first touch of a new key - no KeyError guard needed.\n")


print("=== 8. deque - O(1) at both ends vs list's O(n) at the front ===")
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)
n = 20000
lst = list(range(n))
dq = deque(range(n))
t_list_pop0 = timeit.timeit(lambda: lst.pop(0) if lst else lst.extend(range(n)), number=3000)
t_deque_pop0 = timeit.timeit(lambda: dq.popleft() if dq else dq.extend(range(n)), number=3000)
print(f"list.pop(0): {t_list_pop0:.5f}s   deque.popleft(): {t_deque_pop0:.5f}s")
print("why: list.pop(0) shifts every remaining element left -> O(n). deque is a")
print("     doubly-linked structure under the hood -> O(1) at either end.\n")


print("=== Self-check ===")
print("Score yourself 0-8: how many did you predict correctly BEFORE running?")
print("6+ correct -> you knew this, the diagnostic misses were rust, not gaps.")
print("<6 -> that's fine, it's exactly why this drill exists. Re-run any block you missed.")
