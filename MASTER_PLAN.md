# MASTER PLAN — Siddharth Sharma: Multi-Role Interview Readiness

**Created:** 2026-08-21 · **Rebuilt:** 2026-08-25 (braided structure, real hours) · **Duration:** 24 weeks (Aug 24, 2026 → Feb 7, 2027) · **Effort:** 30–60 min/day, ~5 hrs/week, rising as Sid's capacity grows

---

## 1. Where you are right now (my read of your resume)

You are **not a beginner** — this plan treats you as a working engineer with ~1 year of experience who needs to go deep, prove it publicly, and escape the SDET box.

**Your assets:**
- Real backend experience: 30+ REST endpoints in Java/Spring Boot, Postgres tuning, Redis caching, Docker (Onextel)
- Python in production daily (test frameworks, Flask/FastAPI) at JCI
- Data analyst internship: Power BI, dashboards, EDA, basic ML (KNN)
- **MCP tooling exposure at JCI** — this is gold for AI Engineer / FDE roles; almost nobody at 1 YOE has it
- IEEE publication, IoT/blockchain project

**Your gaps (what interviews will expose):**

| Gap | Severity | Which roles it blocks |
|---|---|---|
| DSA / LeetCode readiness | 🔴 Critical | ALL — every screen at 1–2 YOE is DSA-first |
| No public portfolio (no GitHub on resume, one college project) | 🔴 Critical | ALL — claims need proof |
| ML depth (you have EDA + KNN only) | 🔴 High | ML Engineer |
| AI engineering (RAG, agents, evals, LLM APIs) | 🟠 High | AI Engineer, FDE |
| System design | 🟠 High | Backend, FDE (lighter at your YOE, but asked) |
| Java/Spring interview depth (rusty since Onextel, Dec 2025) | 🟠 High | Backend — most Indian backend interviews are Java-first |
| Advanced SQL (window functions, query plans) | 🟡 Medium | Data Analyst, Backend |
| Statistics / A-B testing / Excel (pivots, lookups) | 🟡 Medium | Data Analyst |
| SDET title pigeonhole risk | 🟠 High | Backend (recruiter filters) — fixed by portfolio + resume positioning |

**Calibration — diagnostic taken Aug 25, 2026: 22/25 (88%).** Python 3/6 · SQL 4/4 · DSA 4/4 · Web 4/4 · Stats 3/3 · ML/AI 4/4.

The Python misses were Q2 (comprehension with a filter), Q3 (hashability) and Q6 (`sorted(key=…)` + stability) — while the *harder* semantic questions (mutable default args, reference aliasing, `is` vs `==`) were all correct. **That is a fluency gap, not a mental-model gap**: normal for a Java-shaped engineer writing pytest daily. Drill idiom and stdlib behaviour, not theory. Caveat on the four perfect sections: 3–4 shallow questions each can't separate "solid" from "strong," and they tested fundamentals only (`LEFT JOIN`, not window functions; big-O recall, not DSA under a timer) — so those stay in the plan at full weight. **Java/Spring was never tested in that diagnostic — a real hole, since it's the headline resume experience and it's cold. A 20-question Java & Spring diagnostic is now on the platform and its result sizes the Java thread.**

**Depth priority (where the hours go when they're scarce):** Backend + AI Engineer first — that's where the existing experience and the MCP differentiator already live. ML, Data and FDE ride along inside the same capstones rather than getting their own months. This is a *weighting*, not a sequence: see §2.

### What the interviews actually look like (researched Aug 2026 — full detail in [interview-prep/INTERVIEW_INTEL.md](interview-prep/INTERVIEW_INTEL.md))

| Role | The loop at 1–2 YOE in India | The make-or-break round |
|---|---|---|
| Backend | OA (2–3 LC-medium) → DSA rounds → **LLD/machine coding at startups** → Java/Spring+SQL+project rounds at GCCs → HM | Live DSA + HashMap/@Transactional-depth Java; startups: 90-min working-code LLD (Parking Lot, Logger, Chess) |
| AI Engineer | Screen → practical Python → GenAI concepts → AI system design → **take-home (RAG/agent) + defense** | The take-home — and **evals are the #1 differentiator** (your SDET background IS an evals background) |
| ML Engineer | OA/DSA → ML breadth → junior-level ML system design (a discussion) → **project end-to-end walkthrough** | The project walkthrough — highest-weight round at this level |
| Data Analyst | Screen → **live SQL** → live Excel (raw data → pivot → dashboard, timed) → case/guesstimate → HR | Live SQL with window functions; "DAU dropped 15% — investigate" case |
| FDE | Screen → practical coding → enterprise design → **decomposition case (~40% pass rate)** → client roleplay | Decomposition + how you talk to "customers" (diagnostic questions before solutions) |

Two cross-cutting 2026 realities: **proctoring is tightening and in-person finals are returning** (38.5% of candidates flagged for AI-cheating in one 19k-interview study — fluency must be live and explainable), and **project deep-dives outweigh trivia at your level** — every capstone gets a rehearsed narrative.

---

## 2. The operating system (how we work)

**Every week touches every track.** Sid's call, and it's the right one — the old plan finished Backend in October and interviewed in February, by which point it was five months cold. That failure mode is already visible in his Java: strongest experience on the resume, untouched since Dec 2025. Interleaving prevents a repeat, and it's how spaced practice is supposed to work.

### The daily braid (~45 min/day)

| Day | Focus | Why this slot |
|---|---|---|
| **Mon** | Backend / Python concept | Fresh head on the deepest material |
| **Tue** | Capstone build | Apply Monday immediately |
| **Wed** | DSA — 2 problems | Mid-week cardio, never skipped |
| **Thu** | AI / ML concept | The differentiator track |
| **Fri** | Capstone build | Ship something before the weekend |
| **Sat** | Data ↔ Java (alternating weeks) | Keeps SQL sharp and Java from going cold again |
| **Sun** | Quiz + review + weekly log | Spaced recall, and the log feeds LinkedIn |

Missing a day is fine — miss the *same* day two weeks running and tell me, that's a signal the plan is wrong, not that you failed.

### The weekly loop

1. **Mon:** say `start week N` → I generate the week's brief, exercises, capstone step, DSA pair and quiz.
2. **Through the week:** follow the braid above; tick steps in the Launchpad as you go.
3. **Sun:** say `grade week N` → I review every file you wrote, score it, give line-by-line feedback, update `progress/progress.json`, and generate the next week.

**Commands you can say to me anytime:**

| You say | I do |
|---|---|
| `start week N` | Generate that week's full content + platform quiz |
| `grade week N` | Review your code/answers, score, detailed feedback |
| `quiz me on <topic>` | Live adaptive quiz in chat |
| `explain <topic>` | Deep lesson with examples + mini-exercise |
| `dsa` | Serve today's problems / review your solutions |
| `mock interview <role>` | Realistic timed mock (coding, design, or behavioral), then scorecard |
| `review my resume` | Re-review against the latest version in `resume/` |
| `status` | Where you are, weak areas, what's next |
| `test out of week N` | Hard quiz + practical — score ≥85% and you skip it |
| `more hours` | Recalibrate the plan upward when capacity actually grows |

**Rules:**
- **70% building, 30% reading.** No tutorial hell. Everything lands in a capstone, a resume bullet, or an interview story — or we cut it.
- **DSA is non-negotiable**, but honestly sized: **2 problems/week** (~50 by Feb), pattern coverage over volume.
- **Test-out rule:** already know a week's material? Prove it (≥85%) and skip it. Your 88% diagnostic already bought you a lighter Week 1.
- **One capstone at a time**, and it must stay deployable at every stage. A half-finished second project is worth nothing.

### What ~5 hrs/week honestly buys (read this once, then stop worrying about it)

24 weeks × ~5 h ≈ **120 hours**. The original plan assumed ~350. So the arithmetic has to show up somewhere, and it shows up here:

- **Interview-strong by Feb:** Backend (Python + Java/Spring) and AI Engineer. These get the most hours and match your real experience.
- **Screen-credible by Feb:** ML and Data Analyst — you'll have shipped genuine work in both (a served model, a real analytics layer) and can defend it in a project deep-dive. You would not survive a specialist MLE loop against someone who does only ML. That's an honest trade, not a failure.
- **FDE:** a stretch regardless of hours — the research says 2.5–4 YOE for global-lab FDE. Indian startup FDE/solutions roles are reachable, and the capstones build exactly that evidence.
- **~50 DSA problems, not 150.** This is the single biggest cut. 50 problems understood cold beats 150 half-remembered, but be aware: strong candidates arrive with more. If hours grow, DSA is where the first extra hour goes.

If capacity rises, say `more hours` and I'll re-cut this — more DSA first, then ML depth.

---

## 3. The roadmap — 4 stages, 24 weeks, every track every week

### Stage 1 · Foundations (W1–6 · Aug 24 → Oct 4)
*Python fluency where the diagnostic found gaps, SQL, FastAPI, LLM basics, Java warm-up. Capstone 1 starts W2.*

| Wk | Backend & Python | AI / ML | Data ↔ Java | Capstone 1 "Pulse" | DSA (2) |
|---|---|---|---|---|---|
| 1 | Collections, comprehensions, sorting, big-O of builtins — **targets your Q2/Q3/Q6 misses** | LLM basics: tokens, context, temperature | SQL: joins + aggregation | *spec & repo plan* | Arrays & hashing |
| 2 | Functions, closures, decorators, generators, typing | Prompting + structured JSON outputs | Java: collections internals, generics, Streams | Repo skeleton, FastAPI up, Docker | Two pointers |
| 3 | FastAPI: routing, Pydantic v2, dependency injection | Calling the Claude API from Python | SQL: subqueries + CTEs | Event-ingest endpoint + Postgres | Sliding window |
| 4 | SQLAlchemy 2.0 + Alembic migrations | Embeddings & vector intuition | Java: concurrency, JVM memory & GC | Events persisted, schema designed | Stack |
| 5 | async, background tasks, error design | Tool calling / function calling | SQL: window functions I | Async ingest + worker stub | Binary search |
| 6 | pytest patterns, fixtures, coverage (**your SDET edge**) | Eval basics: golden sets, why temp=0 isn't deterministic | Java: Spring IoC/DI, `@Transactional` | Test suite + GitHub Actions CI | Linked lists |

**Checkpoint W6:** Pulse ingests events, persists them, is tested, CI is green. You can write a window function cold.

### Stage 2 · Build (W7–12 · Oct 5 → Nov 15)
*Pulse becomes a real multi-role system: auth, scale, a model, an LLM feature, an analytics layer.*

| Wk | Backend & Python | AI / ML | Data ↔ Java | Capstone 1 "Pulse" | DSA (2) |
|---|---|---|---|---|---|
| 7 | Auth: JWT, API keys, HMAC signing | RAG concepts: chunking, retrieval | SQL: window functions II | Auth + signed deliveries | Trees I |
| 8 | Rate limiting, OWASP API top-10 | pgvector + hybrid search | Java: JPA/Hibernate, N+1 | Rate limits + retrieval endpoint | Trees II |
| 9 | Transactions, isolation, indexing, EXPLAIN | First ML model: logistic regression, train/test, metrics | SQL: EXPLAIN + index design | Anomaly-detection baseline | Heaps |
| 10 | Redis caching; queue + retry/backoff + DLQ | scikit-learn pipelines, cross-validation | SQL: cohort, funnel, retention | Worker with retries + analytics queries | Intervals |
| 11 | Multi-stage Docker, deploy, structured logging | **NL-query feature**: LLM + tools over Pulse data | Java: Spring Boot, Security, actuator | NL-query endpoint + deployed | Greedy |
| 12 | Load testing, observability | **Eval harness** for NL-query (LLM-as-judge) — built like an SDET | Dashboard (Power BI/Excel) on Pulse data | **PULSE SHIPS** — design doc, 3-min demo, eval report | Backtracking |

**🏁 Milestone W12 (Nov 15): Pulse deployed. Resume v1. Applications + referral outreach begin — do not wait for "ready."**

### Stage 3 · Deepen (W13–18 · Nov 16 → Dec 27)
*System design, MCP, and Capstone 2 — the AI-heavy one that carries your differentiator.*

| Wk | Backend & Python | AI / ML | Data ↔ Java | Capstone 2 "DocMind" | DSA (2) |
|---|---|---|---|---|---|
| 13 | System design I: LB, caching, queues, capacity estimation | **Build your own MCP server** | Metrics design | Spec + MCP skeleton | Graphs I |
| 14 | System design II: sharding, consistency | Agent loop from scratch, streaming | Java: LLD — Parking Lot / Rate Limiter | MCP server working | Graphs II |
| 15 | API versioning, idempotency, webhooks at scale | RAG with citations over a real corpus | Stats: CIs, hypothesis tests, A/B | Cited RAG answers | 1-D DP |
| 16 | Write one service in **Spring Boot** (prove the Java) | Reranking + chunking strategies compared | Java: Spring depth + Q-bank | Retrieval quality tuned | 2-D DP |
| 17 | Monitoring, drift, MLflow serving | **MLOps**: track, serve and monitor the Pulse model | A/B analysis writeup | Eval suite running in CI | Timed mixed |
| 18 | Cost & latency: caching, routing, streaming | Guardrails: PII, prompt injection | Java: JVM tuning + concurrency drills | Guardrails + cost report | Timed mixed |

**🏁 Milestone W18 (Dec 27): DocMind functional with evals in CI. Resume v2. Both capstones public.**

### Stage 4 · Prove (W19–24 · Dec 28 → Feb 7)
*Deploy, rehearse, mock, apply hard. Almost no new syntax — this stage is about performance.*

| Wk | Focus | Mock / Deliverable | DSA (2) |
|---|---|---|---|
| 19 | DocMind deployed + recorded walkthrough | Mock: backend (Python) | Timed mixed |
| 20 | Excel/BI power tools + exec storytelling; analytics deep-dive on Pulse data | Mock: AI engineer (take-home defense) | Timed mixed |
| 21 | LLD in Java, 90-min working-code drill | Mock: LLD (Java) | Timed mixed |
| 22 | FDE craft: 48-hour POC drill, decomposition cases, client roleplay | Mock: MLE project walkthrough | Timed mixed |
| 23 | Full loop rehearsal + resume vFinal + application push | Mock: backend (Java/Spring) + system design | Timed mixed |
| 24 | **The Gauntlet** — one mock per role, behavioral polish, portfolio final | Scorecard per role | Timed mixed |

**🏁 Milestone W24 (Feb 7, 2027): interview-ready — 2 deployed multi-role capstones, ~50 DSA solves, 6 mocks, 20+ STAR stories, resume vFinal.**

---

## 4. Continuous threads (run every week)

- **DSA:** 2 problems/week, NeetCode pattern order → ~50 by Feb. From W7, one of the two is written **in Java** so the language never goes cold again. Log every solve.
- **Java/Spring:** alternating Saturdays all year (not a 4-week block) + Java DSA from W7 + a Spring Boot service in W16 + an LLD mock in W21. Sized by the Java diagnostic score.
- **Resume:** v1 at W12, v2 at W18, vFinal at W23. Reviews live in `resume/`.
- **Applications:** start W12, ~10 quality applications + 5 referral asks per week. Referrals and hiring-manager outreach come *first* — the SDET title filter is real.
- **Interview stories:** 1 STAR story/week into `interview-prep/stories.md` → 20+ by Feb.
- **LinkedIn:** Mon DECODE / Thu UPGRADE LOG from `linkedin/studio.html` — the Sunday review doubles as post material.
- **Spaced review:** every weekly quiz carries 3 questions from earlier weeks.

## 5. Capstone portfolio (what recruiters will see)

Two systems, not four toys — each one deliberately spans every role you're targeting. One repo that ingests data, serves a model, answers questions with an LLM and proves it with evals is a stronger artifact than four disconnected tutorials, and it fits the real hours.

### 1. "Pulse" — event ingest & insight platform (W2–12)
| Role it proves | How |
|---|---|
| **Backend** | FastAPI + Postgres + auth + HMAC signing + rate limits + Redis + queue with retry/backoff/DLQ + multi-stage Docker + CI/CD + deployed + load-tested |
| **Data Analyst** | Cohort / funnel / retention SQL over real events, window functions, EXPLAIN-tuned, plus a dashboard |
| **ML Engineer** | Anomaly-detection model on the event stream, served through the same API, MLflow-tracked and monitored |
| **AI Engineer** | Natural-language query over the data via tool calling — *with an eval harness and an honest quality report* |
| **FDE** | Design doc, 3-min recorded demo, and a decomposition write-up framing it as a customer problem |

### 2. "DocMind" — MCP + RAG + evals (W13–19)
| Role it proves | How |
|---|---|
| **AI Engineer** | Your own **MCP server**, an agent loop written from scratch, citation-grounded RAG, reranking, streaming |
| **Evals maturity** | Golden set + LLM-as-judge + regression evals in CI — **built first, not bolted on**. This is your rarest signal. |
| **Backend** | FastAPI service, guardrails (PII, prompt injection), cost/latency report, deployed |
| **Java** | One component or the W21 LLD written in Java/Spring |

*Stretch (only if hours grow): a 48-hour POC from a deliberately fuzzy brief — pure FDE speed signal.*

GitHub standards: pinned repos, real READMEs (problem → architecture diagram → decisions → how to run → measured results), meaningful commit history, profile README.

## 6. Market strategy (research-backed, Aug 2026)

- **Where:** GCCs are the strongest junior absorber right now (+35% YoY in tier-2 cities) + funded startups (fintech, quick-commerce, AI) + select product companies. AI-tagged roles grew +33% YoY while plain-CRUD listings shrank — **the backend + AI combination is precisely the winning profile.**
- **Positioning:** "Backend engineer currently in an SDET seat" — lead with Onextel production work. Never "SDET looking to switch." Interviewers judge current ability; it's the **ATS/recruiter title filter** that kills SDET candidates → from W12, referrals + direct hiring-manager outreach come FIRST, portal applications second. (The LinkedIn content engine exists for exactly this.)
- **The MCP story is your differentiator** — MCP now appears in AI-engineer JDs explicitly, and almost no 1-YOE candidate has work exposure. By W14 you'll have *built* MCP servers, not just evaluated them.
- **Your SDET background is secretly an evals background** — evals are the most under-supplied skill in AI-engineer loops. Say: "I build test/eval harnesses and quality gates for LLM systems."
- **FDE sequencing (be realistic):** Indian-startup FDE / solutions-engineer / deployment roles are targetable at W24; global-lab FDE (OpenAI/Anthropic/Databricks — India-remote postings exist) realistically lands at 2.5–4 YOE with a shipped GenAI product + customer-facing evidence. The plan builds that evidence now.
- **Comp reality check (directional, 1–2 YOE):** backend — services ₹4.5–10L, product/startups ₹10–20L+, top GCCs ₹18–25L · AI engineer — ₹8–16L entry with real projects, ₹18–30L at 2–4 yrs · MLE — ₹7–14L services/GCC, ₹15–25L product · DA — ₹4–8L. Don't anchor on LinkedIn-influencer numbers.
- Cadence from W12: ~10 quality applications/week + 5 referral asks + the Thursday LinkedIn log doing inbound work.

## 7. Anti-patterns I will call out

1. Watching tutorials instead of building (I will check your commits).
2. Skipping DSA "just this week" — at 2/week there is no slack left to skip.
3. Perfecting a capstone instead of shipping it.
4. Not applying because "not ready yet." Milestones = apply dates.
5. Listing skills on the resume you can't defend for 10 minutes (current resume has a few — see review).
6. **Starting DocMind before Pulse is deployed.** Two half-built repos prove less than one finished one.
7. **Claiming ML-engineer depth off the back of one served model.** Say what's true: "I built and served an anomaly-detection model end to end." That sentence is strong *and* defensible.

---

*This plan recalibrates whenever reality demands: your diagnostic score, your hours, an interview you land next week. The plan serves you, not the reverse. — Claude*
