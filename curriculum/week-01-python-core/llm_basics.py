"""
Week 1 Thursday drill - LLM basics: tokens, context window, temperature.

Same protocol as gotchas.py: predict before you run. Zero dependencies,
zero API key - everything here is pure stdlib (re, math, random) so it
runs on any machine with no setup. You'll call the real Claude API in
Week 3; this is the mental model underneath that call.
"""

import re
import math
import random

print("=== 1. Tokens are not words, and not characters ===")
sentence = "Claude's tokenizer doesn't split on whitespace only."
chars = len(sentence)
words = len(sentence.split())
approx_tokens = len(re.findall(r"\w+|[^\w\s]", sentence))
print(f"chars: {chars}   words: {words}   approx tokens (word+punct split): {approx_tokens}")
print("why: real BPE tokenizers split on sub-word pieces (\"Claude's\" -> \"Claude\" + \"'s\"),")
print("     so token count sits between word count and char count. Rule of thumb:")
print("     ~4 chars/token in English. This is why cost/latency scale with TOKENS,")
print("     not words - a German or Hindi sentence of the same word count can cost more.\n")


print("=== 2. Context window is a hard cutoff, not a soft suggestion ===")
conversation = [f"turn-{i}: some message text here" for i in range(1, 11)]
CONTEXT_WINDOW_TURNS = 4
kept = conversation[-CONTEXT_WINDOW_TURNS:]
dropped = conversation[:-CONTEXT_WINDOW_TURNS]
print(f"kept (model still sees these): {kept}")
print(f"dropped (model has NO memory of these): {dropped}")
print("why: once a conversation exceeds the window, the oldest turns fall off the")
print("     front - the model doesn't 'summarize' or 'remember the gist' unless your")
print("     application code does that. This is exactly the RAG-vs-fine-tune framing:")
print("     the window is knowledge you paid to include, not knowledge the model owns.\n")


print("=== 3. Temperature - same logits, different sampling behavior ===")
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
for temp in (0.1, 1.5):
    probs = softmax(logits, temp)
    counts = {w: 0 for w in vocab}
    for _ in range(200):
        counts[vocab[sample(probs, rng)]] += 1
    dist = {w: f"{100*c/200:.0f}%" for w, c in counts.items()}
    print(f"temp={temp}: probs={[round(p,3) for p in probs]}")
    print(f"           200 samples -> {dist}")
print("why: LOW temperature sharpens the distribution toward the top logit -> 'the' wins")
print("     almost every time (near-deterministic, but 'near' - not exactly 0% chance of")
print("     anything else, which is WHY temp=0 still isn't perfectly deterministic in")
print("     production - see interview-prep/AI_SYSTEM_DESIGN.md section 3).")
print("     HIGH temperature flattens it -> the model actually gambles on 'banana'")
print("     sometimes. Same model, same prompt, same logits - different product behavior.\n")


print("=== Self-check ===")
print("Could you have predicted the dropped turns in #2 without running it?")
print("Could you have predicted which temperature makes 'banana' possible in #3?")
print("If not, that's the actual gap the diagnostic can't see - not tokenizer trivia.")
