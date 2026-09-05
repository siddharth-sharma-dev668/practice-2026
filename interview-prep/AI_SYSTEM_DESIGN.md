# AI System Design — Production GenAI Concept Bank

Source: Sid's own notes (`AI System design concepts_1451.docx`, added 2026-09-05). This is the reference the AI/ML column of `MASTER_PLAN.md` draws its terminology from for W6–W18, and it's the concept map for the "AI system design" round in the AI Engineer loop (see `INTERVIEW_INTEL.md`).

Frame: a prototype is `Prompt → LLM → Response`. A production system wraps that with retrieval, evaluation, monitoring, optimization, feedback and safety. The seven pieces below are the wrapper.

## Where each piece already lives in the plan

| Concept | Status before Sep 5 | Week(s) it now maps to |
|---|---|---|
| RAG (chunking, embeddings, vector DB, hybrid search, reranking) | Already covered | W4 (embeddings), W7 (RAG concepts), W8 (pgvector/hybrid search), W15 (citations), W16 (reranking) |
| Fine-tuning, RAG-vs-fine-tune, LoRA/PEFT | **Missing entirely** — added | W16 (new) |
| Evals — Task/Trial/Transcript/Grader/Outcome, graders, pass@k vs pass^k, capability vs regression, evals in CI/CD | Partially covered (eval basics W6, eval harness W12) but without the formal vocabulary | W6, W12 (enriched) |
| Observability (latency/cost/quality signals, tracing, versioning) | Named ("observability") but not detailed | W12 (enriched) |
| Caching (exact/semantic/embedding/retrieval/API, invalidation) | Only generic Redis caching (W10), not the LLM-specific layers | W18 (new) |
| User feedback loops (signals → failure analysis → new evals) | Implicit in "production feedback → evals" language, not explicit | Continuous thread, folds into W12 eval-harness work and the Sunday grading loop |
| Guardrails (input/output layers, business-rule enforcement) | Named (PII, prompt injection) but not the layering model | W18 (enriched) |

The gaps that actually needed a new slot were **fine-tuning/LoRA** and the **layered caching taxonomy** — both now placed above. Everything else was already in the plan; this file gives it sharper vocabulary.

---

## 1. RAG — giving the model the right knowledge

**Why:** LLMs are frozen at training time and don't know your private/current data. RAG retrieves relevant context at query time instead of retraining the model.

```
Documents → Parsing → Chunking → Embeddings → Vector DB
User Query → Retrieval → Reranking → Context → LLM → Answer
```

- **Chunking** — how you split documents; size trades off precision (small chunks) vs context (large chunks).
- **Embeddings** — vectors encoding semantic meaning.
- **Vector DB** — stores/retrieves by similarity.
- **Hybrid search** — semantic (vector) + keyword (lexical) combined.
- **Reranking** — a second, more expensive pass that reorders retrieved candidates by relevance.
- **Metadata filtering** — restrict retrieval by doc type, geography, department, version, etc.

**Common failures:** wrong/no document retrieved, wrong document ranked first, stale documents, poor chunking, too much context stuffed in, hallucination *despite* correct context (the model ignores or misreads good context — retrieval quality alone doesn't guarantee correctness).

**Key line:** RAG is a knowledge problem, not a model-training problem.

## 2. Fine-tuning — teaching the model how to behave

**Why:** further training a pretrained model on task-specific examples to change *behavior*, not knowledge.

**When to use it:** classification, enforcing a specific output format, consistent style/voice, domain-specific behavior, specialized tasks.

**RAG vs Fine-tuning:**

| | RAG | Fine-tuning |
|---|---|---|
| Changes | Context/knowledge | Model behavior |
| Knowledge freshness | Easy (swap the index) | Difficult (retrain) |
| Private knowledge | Good fit | Expensive to keep current |
| Style control | Limited | Strong |
| Classification | Possible | Often the better tool |

**LoRA / PEFT:** parameter-efficient fine-tuning — freeze most of the base model's weights and train small low-rank adapter matrices instead of the full network. Cuts training compute/memory drastically while getting most of the behavior change.

**Biggest common mistake:** fine-tuning a model just because it doesn't know something that changes often — that's a RAG problem, not a fine-tuning problem. Retraining to patch stale knowledge is the wrong tool.

## 3. Evals — testing AI systems (the deepest section — SDET territory)

**Why evals, not just unit tests:** AI outputs are variable, subjective, and often multi-step — a single assert can't capture "did this work."

**Vocabulary (Anthropic's framing):**

```
Task → Trial → Transcript → Grader → Outcome
```
- **Task** — a defined test case with inputs and success criteria.
- **Trial** — one execution of that task.
- **Transcript** — what happened during execution.
- **Outcome** — the resulting state of the system/environment.
- **Grader** — how you decide if the trial succeeded.
- **Evaluation harness** — the infrastructure that runs tasks, captures transcripts, applies graders, produces results.
- **Evaluation suite** — a collection of tasks testing one capability/behavior.

**Graders — three types, complementary not exclusive:**
- **Code-based** (exact match, regex, DB state, API result, schema validation) — fast, cheap, reproducible; too rigid for subjective tasks.
- **Model-based** (LLM-as-judge: rubric scoring, NL assertions, pairwise comparison, reference-based) — flexible; can be inconsistent/biased.
- **Human** — best for expert judgment, hard subjective cases, and validating model-based graders; expensive, doesn't scale.

**Capability vs Regression evals:**
- **Capability** — what can the system do? Use hard tasks where there's room to improve.
- **Regression** — did something that worked before break? Should have a very high pass rate, always.
- Loop: capability evals → improve system → regression evals → protect what already works.

**Non-determinism — pass@k vs pass^k:**
- **pass@k** — at least one of k attempts succeeds (can it eventually solve it?).
- **pass^k** — all k attempts succeed (does it solve it *consistently*?).
- Example: if per-trial success probability is 80%, pass@5 (≥1 of 5 succeeds) is much higher than pass^5 (all 5 succeed) — "can eventually solve" and "reliably solves" are different claims, and interviewers will probe which one you mean.

**Designing a good eval suite:** start small — Anthropic recommends ~20–50 realistic tasks, ideally derived from real failures. Good tasks are clear, solvable, reproducible, representative, easy to grade. Test both "should do X" and "should NOT do X" (don't only reward triggering, or you'll reward over-triggering). Grade the outcome, not a rigid step sequence, whenever possible.

**Evals in CI/CD:**
```
Code/Prompt change → Run eval suite → Compare to baseline → Regression? → yes: investigate / no: deploy
```
This is what turns AI quality into an engineering process instead of a vibe check — and it's precisely the muscle an SDET background already has.

## 4. Observability — understanding what happened

Evals answer "did it work?" Observability answers "why did it work or fail?"

A production trace: `Request → Query processing → Embedding → Retrieval → Reranking → LLM → Response` — capture signal at every stage.

**Signals to track:**
- **Latency** — p50 / p95 / p99 (not just averages — tails are what users feel).
- **Cost** — input tokens, output tokens, cost/request.
- **Quality** — eval scores, user feedback, task completion.
- **RAG-specific** — retrieved documents, similarity scores, context size.
- **Versioning** — model version, prompt version, retrieval/index version.

**Why it matters:** if quality drops from 90% to 75%, observability is what lets you distinguish "retrieval changed" from "prompt changed" from "model changed" from "data went stale" from "an external API failed" — instead of guessing. Goal: debuggable, not mysterious.

## 5. Caching — faster and cheaper

LLM calls are expensive; caching avoids repeating work. Layers, roughly cheapest/most-reused to most-specific:

- **Exact caching** — identical request → reuse response.
- **Semantic caching** — different wording, same intent → potentially reuse.
- **Embedding caching** — don't re-embed unchanged documents.
- **Retrieval caching** — reuse retrieved documents for repeated queries.
- **API caching** — reuse external results when freshness allows.

**The real design question isn't "can we cache this?" — it's "when does the cached value become invalid?"** Caching can cut latency/cost dramatically, but a stale or wrongly-scoped cache creates correctness bugs and, in some cases, security problems (serving one user's cached, personalized result to another).

## 6. User feedback loops — learning from production

Offline evals can't predict every real failure. Signals: 👍/👎, corrections, retries, escalations, abandoned workflows.

**Feedback isn't automatically ground truth** — a thumbs-down could mean wrong answer, wrong retrieval, missing info, bad UX, or just user misunderstanding. The loop that matters:

```
User feedback → Failure analysis → Root cause → Fix → New eval → Regression protection
```

Production feedback is uniquely good at surfacing *unexpected* problems, but it's sparse and biased toward severe failures (people report disasters, not near-misses). The best systems convert feedback into permanent engineering knowledge (a new eval case), not just a one-off fix.

## 7. Guardrails — controlling AI behavior

Three layers: `User → Input guardrails → LLM → Output guardrails → Application`.

- **Input guardrails** — prompt-injection detection, PII detection, input validation, authentication, authorization.
- **Output guardrails** — schema validation, safety checks, PII detection, policy validation, business rules.

**Important principle: business logic should not depend solely on the LLM.** The model proposes, deterministic application code enforces. Example: the LLM says "refund customer ₹50,000"; a hard business rule caps automated refunds at ₹10,000 and anything above routes to block/human approval. This is the pattern to reach for whenever an LLM output touches money, access, or irreversible actions.

## 8. How it all fits together

```
USER → INPUT GUARDRAILS → LLM ⇄ RAG (context) / application data
     → LLM → OUTPUT GUARDRAILS → USER
     → FEEDBACK + OBSERVABILITY → EVALS → FAILURE ANALYSIS
     → RAG fixes / FINE-TUNING → BETTER SYSTEM
```
Caching sits underneath, applied to the expensive components (embeddings, retrieval, LLM calls).

## 9. The production loop

```
BUILD → EVAL → DEPLOY → OBSERVE → COLLECT FEEDBACK → ANALYZE FAILURES → CREATE NEW EVALS → IMPROVE → BUILD
```
The model is one component. The engineering system around it determines whether the application is reliable, measurable, safe, scalable, and continuously improving — that's the actual gap between a demo and a product, and it's the story DocMind (W13–19) is built to prove.

## 10. One-minute summary (say this cold in an interview)

RAG gives the model the right information. Fine-tuning teaches it specialized behavior. Evals tell you whether it works. Observability tells you what happened. Caching makes it faster and cheaper. User feedback tells you what you're missing. Guardrails keep the system inside acceptable boundaries.

**The core relationship:** production failures → feedback → evals → improvements → fewer future failures.
