"""Week 1 self-checker. Run:  python check.py"""
import sys

import exercises

# (function name, [ (args, expected) ... ], normalizer applied to the returned value)
TESTS = [
    ("two_sum", [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ], sorted),
    ("dedupe", [
        (([3, 1, 3, 2, 1],), [3, 1, 2]),
        (([],), []),
        ((["a", "a", "a"],), ["a"]),
    ], None),
    ("top_k_frequent", [
        ((["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"]),
        ((["a", "b", "a", "b", "c"], 2), ["a", "b"]),
        ((["z"], 1), ["z"]),
    ], None),
    ("group_anagrams", [
        ((["eat", "tea", "tan", "ate", "nat", "bat"],), [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]),
        (([""],), [[""]]),
        ((["a"],), [["a"]]),
    ], None),
    ("first_unique", [
        (("leetcode",), 0),
        (("loveleetcode",), 2),
        (("aabb",), -1),
    ], None),
    ("compress", [
        (("aabcccccaaa",), "a2b1c5a3"),
        (("abc",), "abc"),
        (("",), ""),
        (("aaaa",), "a4"),
    ], None),
    ("merge_intervals", [
        (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
        (([[1, 4], [4, 5]],), [[1, 5]]),
        (([[5, 6], [1, 2]],), [[1, 2], [5, 6]]),
    ], None),
    ("rotate_right", [
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
        (([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3]),
        (([], 3), []),
    ], None),
    ("is_balanced", [
        (("()[]{}",), True),
        (("([)]",), False),
        (("{[]}",), True),
        (("(",), False),
        (("",), True),
    ], None),
    ("chunked", [
        (([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
        (([], 3), []),
        (([1, 2], 5), [[1, 2]]),
    ], None),
    ("flatten", [
        (([1, [2, [3, 4]], 5],), [1, 2, 3, 4, 5]),
        (([],), []),
        (([[[1]]],), [1]),
    ], None),
    ("product_except_self", [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([0, 4, 0],), [0, 0, 0]),
        (([2, 3],), [3, 2]),
    ], None),
]


def main() -> int:
    passed_fns = 0
    passed_cases = 0
    total_cases = 0
    print("=" * 62)
    for name, cases, norm in TESTS:
        fn = getattr(exercises, name, None)
        total_cases += len(cases)
        if fn is None:
            print(f"MISSING  {name:<22} function not found in exercises.py")
            continue
        fails = []
        todo = False
        ok = 0
        for args, expected in cases:
            try:
                got = fn(*args)
                if norm is not None:
                    got = norm(got)
                if got == expected:
                    ok += 1
                else:
                    fails.append(f"    {name}{args!r} -> got {got!r}, expected {expected!r}")
            except NotImplementedError:
                todo = True
                break
            except Exception as e:  # show the error, keep checking other functions
                fails.append(f"    {name}{args!r} raised {type(e).__name__}: {e}")
        passed_cases += ok
        if todo:
            print(f"TODO     {name:<22} not implemented yet")
        elif not fails:
            passed_fns += 1
            print(f"PASS     {name:<22} {ok}/{len(cases)} cases")
        else:
            print(f"FAIL     {name:<22} {ok}/{len(cases)} cases")
            for line in fails:
                print(line)
    print("=" * 62)
    print(f"SCORE: {passed_fns}/{len(TESTS)} functions  ({passed_cases}/{total_cases} cases)")
    if passed_fns == len(TESTS):
        print("All green. Take the Week 1 quiz, then say 'grade week 1' in chat.")
    return 0 if passed_fns == len(TESTS) else 1


if __name__ == "__main__":
    sys.exit(main())
