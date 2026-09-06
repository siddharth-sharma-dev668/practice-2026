"""
Week 1 Monday drill.

HOW TO USE THIS FILE — read this part first, it's the whole instruction:

Run it: `python gotchas.py`
The terminal will show you a block of code and ASK you a question. It will then
wait (nothing else happens until you act). Type WHATEVER your guess is — a value,
a word, "no idea", literally anything — and press Enter. The moment you press
Enter, the real answer prints, right below your guess, with a "why" explaining it.

You don't need to know the right answer to type something. You don't need to
write it anywhere else — typing it into the terminal IS the exercise. Getting it
wrong is not a problem; that's the entire point of doing this before reading the
answer instead of after.

There are 8 blocks. Takes about 15-20 minutes.
"""


def predict(block_num, title, code_shown, question):
    print(f"\n{'=' * 70}")
    print(f"BLOCK {block_num}: {title}")
    print(f"{'=' * 70}")
    print("CODE:")
    for line in code_shown.strip("\n").split("\n"):
        print("    " + line)
    print()
    print("QUESTION:", question)
    input(">>> Type your guess, then press Enter to reveal the real answer: ")
    print()


def reveal(*lines):
    print("ACTUAL ANSWER:")
    for line in lines:
        print("    " + str(line))
    print()


predict(1, "Comprehension with a filter (your diagnostic Q2)",
    "[x * x for x in range(6) if x % 2]",
    "What list does this produce?")
result = [x * x for x in range(6) if x % 2]
reveal(result)
print("why: x % 2 is truthy only for odd x -> 1, 3, 5 survive -> their squares 1, 9, 25\n")


predict(2, "Hashability - what can be a dict key? (your diagnostic Q3)",
    'bad_key = {[1, 2]: "value"}',
    "Does this line run, or crash? If it crashes, what error?")
try:
    bad_key = {[1, 2]: "value"}
    reveal(bad_key)
except TypeError as e:
    reveal(f"TypeError: {e}")
good_key = {(1, 2): "value"}
print(f"(a TUPLE key works fine, though: {good_key})")
print("why: dict keys must be hashable. Lists are mutable -> unhashable.")
print("     Tuples are hashable IF every element inside them is too.\n")


predict(3, "sorted(key=len) + stability (your diagnostic Q6)",
    'words = ["pear", "fig", "plum", "kiwi", "date"]\nsorted(words, key=len)',
    "What order do the words come out in? (pay attention to 'plum' and 'kiwi' - same length)")
words = ["pear", "fig", "plum", "kiwi", "date"]
reveal(sorted(words, key=len))
print("why: sorted() always returns a NEW list. Timsort is stable, so")
print("     'plum' and 'kiwi' (both len 4) keep their original relative order.\n")


predict(4, "Multi-key sort - extends #3",
    'people = [("sid", 27), ("ana", 27), ("bo", 19)]\nsorted(people, key=lambda p: (-p[1], p[0]))',
    "What order do the three people come out in?")
people = [("sid", 27), ("ana", 27), ("bo", 19)]
reveal(sorted(people, key=lambda p: (-p[1], p[0])))
print("why: tuple keys sort left-to-right - here: age descending, then name ascending.\n")


predict(5, "Big-O of `in`: list scan vs set hash",
    "19999 in a_list_of_20000_numbers   vs   19999 in a_set_of_the_same_20000_numbers",
    "Which is faster, and roughly how much faster - 2x? 10x? 1000x? Guess a number.")
import timeit
haystack_list = list(range(20000))
haystack_set = set(haystack_list)
t_list = timeit.timeit(lambda: 19999 in haystack_list, number=1000)
t_set = timeit.timeit(lambda: 19999 in haystack_set, number=1000)
reveal(f"list: {t_list:.5f}s total   set: {t_set:.5f}s total   set is {t_list / t_set:.0f}x faster")
print("why: list.__contains__ is O(n) - it scans. set.__contains__ hashes straight")
print("     to the bucket, O(1) average. You just measured it instead of reading it.\n")


predict(6, "Counter - tally + top-k in one line",
    'Counter("mississippi").most_common(2)',
    "What does this return - and in what format (a list? a dict?)")
from collections import Counter
c = Counter("mississippi")
reveal(c.most_common(2))
print("why: most_common(k) returns [(elem, count), ...] sorted by count, highest first.\n")


predict(7, "defaultdict - skips the 'if key not in dict' boilerplate",
    'groups = defaultdict(list)\nfor word in ["ant", "bee", "ape", "bat"]: groups[word[0]].append(word)',
    "What does the final `groups` dict look like?")
from collections import defaultdict
groups = defaultdict(list)
for word in ["ant", "bee", "ape", "bat"]:
    groups[word[0]].append(word)
reveal(dict(groups))
print("why: defaultdict(list) auto-creates [] on first touch of a new key - no KeyError guard needed.\n")


predict(8, "deque - O(1) at both ends vs list's O(n) at the front",
    "popping 3000 items from the FRONT of a list  vs  popping 3000 items from the FRONT of a deque",
    "Which is faster, and roughly how much? (Same shape of question as block 5, other end of the container.)")
from collections import deque
n = 20000
lst = list(range(n))
dq = deque(range(n))
t_list_pop0 = timeit.timeit(lambda: lst.pop(0) if lst else lst.extend(range(n)), number=3000)
t_deque_pop0 = timeit.timeit(lambda: dq.popleft() if dq else dq.extend(range(n)), number=3000)
reveal(f"list.pop(0): {t_list_pop0:.5f}s total   deque.popleft(): {t_deque_pop0:.5f}s total")
print("why: list.pop(0) shifts every remaining element left -> O(n). deque is a")
print("     doubly-linked structure under the hood -> O(1) at either end.\n")


print(f"\n{'=' * 70}")
print("SELF-CHECK")
print(f"{'=' * 70}")
print("Score yourself 0-8: how many of your typed guesses were actually right?")
print("6+ correct -> you knew this, the diagnostic misses were rust, not gaps.")
print("<6 -> that's fine, it's exactly why this drill exists. Re-run any block you missed.")
