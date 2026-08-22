"""Week 1 — Python for Interviews I: 12 exercises.

Rules:
- Implement each function, then run `python check.py` to score yourself.
- Python docs allowed. No AI, no copy-paste solutions — fluency is the goal.
- Think about time complexity for every one (you'll be asked in interviews).

Replace each `raise NotImplementedError` with your implementation.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices [i, j] (i != j) such that nums[i] + nums[j] == target.
    Exactly one solution exists. Aim for one pass with a dict — O(n).

    two_sum([2, 7, 11, 15], 9) -> [0, 1]
    """
    raise NotImplementedError


def dedupe(items: list) -> list:
    """Remove duplicates, preserving first-occurrence order. O(n).

    dedupe([3, 1, 3, 2, 1]) -> [3, 1, 2]
    """
    raise NotImplementedError


def top_k_frequent(words: list[str], k: int) -> list[str]:
    """Return the k most frequent words, most frequent first.
    Ties broken alphabetically. Hint: collections.Counter + sorted with a tuple key.

    top_k_frequent(["i", "love", "i", "love", "code"], 2) -> ["i", "love"]
    """
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams together. Each group sorted alphabetically;
    groups sorted by their first word. Hint: dict keyed by sorted letters.

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    """
    raise NotImplementedError


def first_unique(s: str) -> int:
    """Return the index of the first non-repeating character, or -1.

    first_unique("leetcode") -> 0      first_unique("aabb") -> -1
    """
    raise NotImplementedError


def compress(s: str) -> str:
    """Run-length encode: "aabcccccaaa" -> "a2b1c5a3".
    Return the ORIGINAL string if compression doesn't make it shorter.

    compress("aabcccccaaa") -> "a2b1c5a3"     compress("abc") -> "abc"
    """
    raise NotImplementedError


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping intervals; return them sorted by start.
    Touching intervals merge too: [1,4] and [4,5] -> [1,5].

    merge_intervals([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
    """
    raise NotImplementedError


def rotate_right(nums: list[int], k: int) -> list[int]:
    """Return a NEW list rotated right by k steps (k may exceed len(nums)).

    rotate_right([1,2,3,4,5], 2) -> [4,5,1,2,3]     rotate_right([], 3) -> []
    """
    raise NotImplementedError


def is_balanced(s: str) -> bool:
    """Are the brackets ()[]{} balanced and correctly nested? Classic stack.

    is_balanced("{[]}") -> True     is_balanced("([)]") -> False
    """
    raise NotImplementedError


def chunked(items: list, size: int) -> list[list]:
    """Split into consecutive chunks of `size` (last may be shorter). size >= 1.

    chunked([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    """
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Flatten arbitrarily nested lists (elements are ints or lists). Recursion.

    flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    """
    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    """result[i] = product of all elements except nums[i].
    Challenge: O(n) WITHOUT using division (prefix/suffix products).

    product_except_self([1,2,3,4]) -> [24,12,8,6]
    """
    raise NotImplementedError
