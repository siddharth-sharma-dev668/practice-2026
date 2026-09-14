"""
Week 2 Thursday drill -- prompting + structured JSON output reliability.
Zero dependencies, zero API key -- the failure modes below are the exact
ones you hit calling a real LLM API in Week 3, just simulated with fixed
strings so the lesson is deterministic and needs no network call.
Run: python prompting_json.py
"""

import json


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
# BLOCK 1: a model asked for "JSON" often wraps it in prose + markdown fences
model_output_1 = '''Sure! Here's the JSON you asked for:

```json
{"name": "Ana", "age": 27}
```

Let me know if you need anything else!'''

predict(1, "Naive json.loads() on a raw model response",
    'model_output = \'Sure! Here\\\'s the JSON...\\n```json\\n{"name": "Ana", "age": 27}\\n```\\n...\'\n'
    'result = json.loads(model_output)',
    "Does json.loads() on that raw string work, or crash? If it crashes, what error?")
try:
    result1 = json.loads(model_output_1)
    outcome1 = f"parsed successfully: {result1}"
except json.JSONDecodeError as e:
    outcome1 = f"json.JSONDecodeError: {e}"
reveal(outcome1,
    "Models trained to be helpful add conversational wrapper text and markdown code fences even when you "
    "ask for 'just JSON' -- json.loads() expects the ENTIRE string to be valid JSON, so the leading prose "
    "breaks it immediately. This is why real integrations either (a) ask the model for a specific structured-"
    "output mode that guarantees bare JSON, or (b) strip fences/prose before parsing, or (c) both. Never "
    "assume 'the model followed instructions' is the same as 'the string is parseable.'")


# ---------------------------------------------------------------------------
# BLOCK 2: stripping fences is a real, necessary step -- not a hack
def extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines)
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        return text
    return text[start:end + 1]


predict(2, "Extracting the JSON out of the wrapper",
    "cleaned = extract_json(model_output)\nresult = json.loads(cleaned)",
    "Using the same messy model_output from Block 1, after stripping fences and taking only the { ... } span, does it parse now?")
cleaned = extract_json(model_output_1)
result2 = json.loads(cleaned)
reveal(f"parsed: {result2}",
    "Slicing from the first '{' to the last '}' after stripping code fences recovers the real payload -- "
    "{'name': 'Ana', 'age': 27}. This exact defensive-parsing step is standard in production LLM code, not "
    "a workaround you'd be embarrassed to show an interviewer -- it's the difference between a demo that "
    "works once and an integration that survives the model's next minor prompt-following slip.")


# ---------------------------------------------------------------------------
# BLOCK 3: schema validation catches a structurally-valid-but-wrong response
def validate_person(obj):
    required = {"name": str, "age": int}
    for key, typ in required.items():
        if key not in obj:
            return False, f"missing required field: {key}"
        if not isinstance(obj[key], typ):
            return False, f"field {key!r} should be {typ.__name__}, got {type(obj[key]).__name__}"
    return True, "valid"


candidate_a = {"name": "Bo", "age": 30}
candidate_b = {"name": "Chen", "age": "thirty"}
candidate_c = {"age": 25}

predict(3, "Valid JSON is not the same as valid DATA -- schema-check each field",
    'candidate_a = {"name": "Bo", "age": 30}\n'
    'candidate_b = {"name": "Chen", "age": "thirty"}   # age is a STRING\n'
    'candidate_c = {"age": 25}                          # no name at all\n'
    "for c in [candidate_a, candidate_b, candidate_c]: print(validate_person(c))",
    "Which of the 3 candidates pass validate_person, and why do the failing ones fail specifically?")
results3 = [validate_person(c) for c in [candidate_a, candidate_b, candidate_c]]
reveal(results3,
    "candidate_a passes -- both fields present with the right types. candidate_b parses as valid JSON (it's "
    "well-formed) but FAILS validation because age is a string, not an int -- the model followed JSON syntax "
    "but not your actual schema. candidate_c fails because 'name' is missing entirely. This is the real "
    "reliability lesson: json.loads() succeeding tells you nothing about whether the DATA is usable -- you "
    "still need an explicit schema check (or a real library like Pydantic, which you'll use for exactly this "
    "in Week 3's FastAPI work) before trusting a model's structured output downstream.")


# ---------------------------------------------------------------------------
# BLOCK 4: the retry-until-valid pattern, and why it needs a cap
fake_model_attempts = [
    '{"name": "Deja", "age": "not a number"}',   # attempt 1: wrong type
    'not json at all',                             # attempt 2: not even JSON
    '{"name": "Deja", "age": 22}',                # attempt 3: finally valid
]


def get_valid_response(attempts, max_retries=3):
    for i, raw in enumerate(attempts[:max_retries], start=1):
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        ok, _ = validate_person(obj)
        if ok:
            return obj, i
    return None, max_retries


predict(4, "Retry until a response actually validates -- with a hard cap",
    "fake_model_attempts = [\n"
    '    \'{"name": "Deja", "age": "not a number"}\',\n'
    "    'not json at all',\n"
    '    \'{"name": "Deja", "age": 22}\',\n'
    "]\n"
    "result, attempt_num = get_valid_response(fake_model_attempts, max_retries=3)",
    "Which attempt number finally succeeds, and what does `result` end up being?")
result4, attempt_num = get_valid_response(fake_model_attempts, max_retries=3)
reveal(f"succeeds on attempt {attempt_num}: {result4}",
    "Attempt 1 is valid JSON but fails the schema (age is a string). Attempt 2 isn't even valid JSON, caught "
    "and skipped by the except clause. Attempt 3 finally satisfies both json.loads() AND validate_person(). "
    "The max_retries cap matters as much as the retry itself -- an LLM call that NEVER produces valid output "
    "needs a defined giving-up point, or your code hangs retrying forever against a model that's genuinely "
    "stuck. This exact retry-with-cap shape is what a production structured-output call looks like.")


print("=" * 70)
print("SELF-CHECK")
print("Score yourself 0-4. The real lesson isn't tokens or temperature this time --")
print("it's that 'the model said it would return JSON' is a claim to verify, not trust.")
