"""
Week 1 Thursday drill - LLM basics: tokens, context window, temperature.

HOW TO USE THIS FILE: run `python llm_basics.py`. The terminal will show you
some code and ASK a question, then wait. Type anything - a number, a guess,
"no idea" - and press Enter. The real answer prints right after, with a "why".
Same idea as gotchas.py, 3 blocks this time. Zero dependencies, zero API key -
you'll call the real Claude API in Week 3; this is the mental model underneath it.
"""

import re
import math
import random


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


predict(1, "Tokens are not words, and not characters",
    'sentence = "Claude\'s tokenizer doesn\'t split on whitespace only."\n'
    'chars = len(sentence)\nwords = len(sentence.split())',
    "The sentence has 52 characters and 7 words. Guess a number for how many TOKENS "
    "a real tokenizer would split it into - closer to 7, closer to 52, or in between?")
sentence = "Claude's tokenizer doesn't split on whitespace only."
chars = len(sentence)
words = len(sentence.split())
approx_tokens = len(re.findall(r"\w+|[^\w\s]", sentence))
reveal(f"chars: {chars}   words: {words}   approx tokens (word+punct split): {approx_tokens}")
print("why: real BPE tokenizers split on sub-word pieces (\"Claude's\" -> \"Claude\" + \"'s\"),")
print("     so token count sits between word count and char count. Rule of thumb:")
print("     ~4 chars/token in English. This is why cost/latency scale with TOKENS,")
print("     not words - a German or Hindi sentence of the same word count can cost more.\n")


predict(2, "Context window is a hard cutoff, not a soft suggestion",
    "conversation = 10 turns, turn-1 through turn-10\n"
    "CONTEXT_WINDOW_TURNS = 4   # the model can only see the last 4",
    "Which turns does the model still see, and which ones does it have ZERO memory of? "
    "Name the turn numbers on each side.")
conversation = [f"turn-{i}: some message text here" for i in range(1, 11)]
CONTEXT_WINDOW_TURNS = 4
kept = conversation[-CONTEXT_WINDOW_TURNS:]
dropped = conversation[:-CONTEXT_WINDOW_TURNS]
reveal(f"kept (model still sees these): {kept}", f"dropped (model has NO memory of these): {dropped}")
print("why: once a conversation exceeds the window, the oldest turns fall off the")
print("     front - the model doesn't 'summarize' or 'remember the gist' unless your")
print("     application code does that. This is exactly the RAG-vs-fine-tune framing:")
print("     the window is knowledge you paid to include, not knowledge the model owns.\n")


predict(3, "Temperature - same logits, different sampling behavior",
    'vocab = ["the", "a", "definitely", "possibly", "banana"]\n'
    'logits favor "the" heavily. Sample 200 times at temp=0.1, then 200 times at temp=1.5.',
    "At temp=0.1, roughly what % of the 200 samples do you think will be \"the\"? "
    "At temp=1.5, do you think \"banana\" (the model's LEAST likely word) will ever get picked?")
def softmax(logits, temperature):
    scaled = [x / temperature for x in logits]
    m = max(scaled)
    exps = [math.exp(x - m) for x in scaled]
    total = sum(exps)
    return [e / total for e in exps]

def sample(probs, rng):
    r = rng.random()
    cumulative = 0.0
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            return i
    return len(probs) - 1

vocab = ["the", "a", "definitely", "possibly", "banana"]
logits = [4.0, 3.6, 1.0, 0.8, -2.0]  # "the" is the model's top pick by a clear margin

rng = random.Random(42)
lines = []
for temp in (0.1, 1.5):
    probs = softmax(logits, temp)
    counts = {w: 0 for w in vocab}
    for _ in range(200):
        counts[vocab[sample(probs, rng)]] += 1
    dist = {w: f"{100*c/200:.0f}%" for w, c in counts.items()}
    lines.append(f"temp={temp}: probs={[round(p,3) for p in probs]}")
    lines.append(f"           200 samples -> {dist}")
reveal(*lines)
print("why: LOW temperature sharpens the distribution toward the top logit -> 'the' wins")
print("     almost every time (near-deterministic, but 'near' - not exactly 0% chance of")
print("     anything else, which is WHY temp=0 still isn't perfectly deterministic in")
print("     production - see interview-prep/AI_SYSTEM_DESIGN.md section 3).")
print("     HIGH temperature flattens it -> the model actually gambles on 'banana'")
print("     sometimes. Same model, same prompt, same logits - different product behavior.\n")


print(f"\n{'=' * 70}")
print("SELF-CHECK")
print(f"{'=' * 70}")
print("Were your typed guesses in the right ballpark for all 3 blocks?")
print("If not, that's the actual gap this drill exists to close - not tokenizer trivia.")
