"""
Week 2 Monday drill -- closures, decorators, generators, typing.
Predict-then-run, same protocol as Week 1's gotchas.py.
Run: python decorators_closures.py
"""


def predict(block_num, title, code, question):
    print("=" * 70)
    print(f"BLOCK {block_num}: {title}")
    print("=" * 70)
    print("CODE:")
    print(code)
    print(f"\nQUESTION: {question}")
    input(">>> Type your guess, then press Enter to reveal the real answer: ")


def reveal(answer, why):
    print("\nACTUAL ANSWER:")
    print(f"    {answer}")
    print(f"\nwhy: {why}\n\n")


# ---------------------------------------------------------------------------
# BLOCK 1: closures capture the VARIABLE, not the value at definition time
predict(1, "Closures and the late-binding loop bug",
    'funcs = [lambda: i for i in range(3)]\nresults = [f() for f in funcs]',
    "What is `results`? [0, 1, 2] or something else?")
funcs = [lambda: i for i in range(3)]
results = [f() for f in funcs]
reveal(results,
    "Every lambda closes over the SAME variable `i`, not its value at creation "
    "time. By the time any lambda runs, the loop has finished and i is 2 -- "
    "so all three calls return 2. Fix: lambda i=i: i, which captures the "
    "value as a default argument instead of a live reference.")


# ---------------------------------------------------------------------------
# BLOCK 2: a decorator without functools.wraps hides the real function
def logged(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


@logged
def greet(name):
    """Say hello."""
    return f"hello {name}"


predict(2, "Decorator without functools.wraps",
    '@logged\ndef greet(name):\n    """Say hello."""\n    return f"hello {name}"\n\nprint(greet.__name__, greet.__doc__)',
    "What do greet.__name__ and greet.__doc__ print -- the real ones, or something else?")
reveal(f"{greet.__name__!r} {greet.__doc__!r}",
    "The decorator returns `wrapper`, so greet IS wrapper now -- its "
    "__name__ becomes 'wrapper' and __doc__ becomes None, not greet's own. "
    "This breaks introspection, help(), and stack traces. Fix: decorate "
    "wrapper with @functools.wraps(fn), which copies __name__/__doc__/etc "
    "from the original function onto the wrapper.")


# ---------------------------------------------------------------------------
# BLOCK 3: a parametrized decorator needs an extra layer of nesting
def repeat(times):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(times):
                last = fn(*args, **kwargs)
            return last
        return wrapper
    return decorator


call_count = {"n": 0}


@repeat(times=3)
def ping():
    call_count["n"] += 1
    return call_count["n"]


predict(3, "Decorator that takes its own argument",
    '@repeat(times=3)\ndef ping():\n    call_count["n"] += 1\n    return call_count["n"]\n\nresult = ping()',
    "After calling ping() ONCE, how many times did the inner function actually run, and what does `result` equal?")
result = ping()
reveal(f"ran 3 times total, result = {result}",
    "@repeat(times=3) needs three levels: repeat(times) returns decorator, "
    "decorator(fn) returns wrapper, and wrapper is what actually runs each "
    "time ping() is called. One call to ping() triggers the inner loop 3 "
    "times, and the wrapper returns whatever the LAST call produced.")


# ---------------------------------------------------------------------------
# BLOCK 4: a generator function's body doesn't run until you pull from it
def make_gen():
    print("    (generator body: about to yield 1)")
    yield 1
    print("    (generator body: about to yield 2)")
    yield 2


predict(4, "Generators are lazy -- calling the function does nothing yet",
    'def make_gen():\n    print("about to yield 1")\n    yield 1\n    print("about to yield 2")\n    yield 2\n\ng = make_gen()\nprint("created g, nothing printed yet? or did it print already?")',
    "Does calling make_gen() print anything immediately, or only once you call next(g)?")
g = make_gen()
print("    created g -- did either print statement run yet? (answer: no)")
first = next(g)
reveal(f"first next(g) = {first}, and the print only happens NOW, not at creation",
    "Calling a generator FUNCTION returns a generator OBJECT immediately -- "
    "none of the function body runs. Each next() call resumes execution from "
    "the last yield until it hits the next one. This is exactly why a "
    "generator can represent an infinite sequence without ever running out "
    "of memory -- it only computes one step at a time, on demand.")


# ---------------------------------------------------------------------------
# BLOCK 5: a generator is single-use -- it exhausts
def three_items():
    yield "a"
    yield "b"
    yield "c"


gen = three_items()
first_pass = list(gen)
predict(5, "Generators exhaust -- you cannot restart one",
    'gen = three_items()\nfirst_pass = list(gen)   # consumes it fully\nsecond_pass = list(gen)  # ??',
    f"first_pass is {first_pass}. What does second_pass equal -- the same list again, or something else?")
second_pass = list(gen)
reveal(second_pass,
    "Once a generator is fully consumed, it's exhausted -- calling list() "
    "again gets an empty list, not a fresh restart. A generator is a "
    "one-shot iterator, not a reusable container. If you need to iterate "
    "twice, either call three_items() again for a NEW generator, or "
    "materialize it into a list once and reuse the list.")


# ---------------------------------------------------------------------------
# BLOCK 6: type hints are NOT enforced at runtime
def add_ints(x: int, y: int) -> int:
    return x + y


predict(6, "Type hints are documentation, not a runtime contract",
    'def add_ints(x: int, y: int) -> int:\n    return x + y\n\nresult = add_ints("a", "b")',
    'add_ints is hinted to take ints. Calling add_ints("a", "b") -- does Python raise TypeError, or does it just run?')
result2 = add_ints("a", "b")
reveal(f'{result2!r} -- it just ran, no error, string concatenation happened',
    "Python's type hints are pure documentation for humans and for external "
    "tools (mypy, your IDE, pydantic) -- the interpreter itself never checks "
    "them at call time. `x: int` is a promise you're making, not a guard "
    "Python enforces. This matters directly for FastAPI in Week 3: FastAPI's "
    "actual runtime validation comes from Pydantic reading those same hints "
    "and validating REAL request data against them -- plain Python functions "
    "get no such protection on their own.")


print("=" * 70)
print("SELF-CHECK")
print("Score yourself 0-6: how many of your typed guesses were actually right?")
print("The closure and decorator gotchas (blocks 1-3) are the ones that bite")
print("in real code reviews, not just interviews.")
