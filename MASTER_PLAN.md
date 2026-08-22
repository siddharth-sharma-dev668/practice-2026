# MASTER PLAN — Siddharth Sharma: Multi-Role Interview Readiness

**Created:** 2026-08-21 · **Duration:** 24 weeks (Aug 24, 2026 → Feb 7, 2027) · **Assumed effort:** 13–16 hrs/week alongside your job

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

**Strategic order (nearest-first):** Backend → AI Engineer → ML Engineer → Data Analyst polish → FDE (FDE is the *synthesis* of all four + client skills — your backend + data + MCP profile is naturally FDE-shaped).

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

Everything happens in this folder. Weekly loop:

1. **Mon:** Say `start week N` → I generate the week's folder: lesson brief, exercises, project spec, DSA set, and add the quiz to your platform.
2. **Mon–Fri (~1.5–2h/day):** Study the brief, do exercises, solve the DSA set.
3. **Weekend (~4–6h):** Build the week's project piece, take the quiz on the platform.
4. **Sunday:** Say `grade week N` → I review every file you wrote, score it, give line-by-line feedback, and update `progress/progress.json`.

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

**Rules:**
- **70% building, 30% reading.** No tutorial hell. Every phase ends in a deployed, public capstone.
- **Everything becomes evidence:** a GitHub repo, a resume bullet, or an interview story. If it produces none of these, we cut it.
- **DSA is non-negotiable daily cardio** (~30–45 min/day, 6 problems/week). It's the gate to every interview.
- **Test-out rule:** already know a week's material? Prove it (≥85%) and skip. The diagnostic (Week 0) sets your starting point.

---

## 3. The roadmap — 7 phases, 24 weeks

### Phase 0 — Setup, Diagnostic & Baseline (NOW → Sun Aug 23)
- [ ] Do the **Diagnostic quiz** on the platform (25 questions, all sections) — send me your section scores
- [ ] Tell me your **real hours/week** and any deadline pressure (I recalibrate the whole plan)
- [ ] Create/clean your **GitHub** account; send me the username
- [ ] Read `resume/REVIEW-2026-08-21.md` — my baseline review of your current resume
- [ ] Set up: VS Code + Python 3.13 ✅ (installed) + Git ✅ (installed) + a LeetCode account

### Phase 1 — Interview Core (W1–4 · Aug 24 → Sep 20)
*Sharpen the fundamentals every interview probes. You "know" Python — now make it bulletproof.*

| Wk | Topic | Build / Deliverable | DSA thread |
|---|---|---|---|
| 1 | Python for interviews I: collections, comprehensions, sorting, strings, big-O of builtins | 12 exercise functions passing `check.py` | Arrays & hashing (6) |
| 2 | Python for interviews II: closures, decorators, generators, itertools, typing, error design | Refactor W1 + build a small `@retry`/`@timed` decorator lib | Two pointers & sliding window (6) |
| 3 | Advanced SQL I: joins mastery, aggregation, subqueries, CTEs, window functions intro | 20 SQL drills on a real schema (I provide dataset) | Stack & binary search (6) |
| 4 | Advanced SQL II: window functions deep, EXPLAIN & indexes, schema design + pytest deep dive | SQL drill set 2 + tested mini-lib (90% coverage) | Linked lists (6) |

**Checkpoint:** you can solve LeetCode easies in <15 min, mediums with hints; you can write window-function SQL cold.

### Phase 2 — Backend Pro (W5–8 · Sep 21 → Oct 18)
*You've done backend at work — now do it at portfolio-grade with modern Python.*

| Wk | Topic | Build (Capstone 1 grows weekly) | DSA |
|---|---|---|---|
| 5 | FastAPI production: structure, Pydantic v2, async, DI, SQLAlchemy 2.0 + Alembic | **Capstone 1 "Relay"** skeleton: webhook delivery service — ingest events API | Trees I (6) |
| 6 | Auth & security: JWT, OAuth2 flows, RBAC, rate limiting, OWASP API top-10 | Relay: API-key auth, HMAC-signed deliveries, rate limits | Trees II (6) |
| 7 | Data layer at scale: transactions & isolation, indexing deep, N+1, Redis patterns, background workers | Relay: queue + worker with retry/backoff + dead-letter | Heaps (6) |
| 8 | Ship it: multi-stage Docker, GitHub Actions CI/CD, deploy, structured logging, load test (locust) | Relay: **deployed + CI + load-test report + design doc README** | Backtracking (6) |

**Java/Spring revision thread (runs through W5–8, ~2h/week):** your professional Java is 8+ months cold, and it's your headline resume experience — interviewers WILL go there. Each week I give you a drill + question bank:
- W5 — Java core I: collections internals (HashMap!), equals/hashCode, generics, Streams API
- W6 — Java core II: concurrency (threads, executors, synchronized/volatile), JVM memory & GC
- W7 — Spring: IoC & bean lifecycle, `@Transactional` pitfalls, JPA/Hibernate (lazy loading, N+1, caching)
- W8 — Spring Boot autoconfiguration, Spring Security basics, actuator + a **full Java/Spring mock interview**

During P2, solve 2 of your 6 weekly DSA problems in Java so syntax stays warm. Capstone 1 stays in FastAPI deliberately — your resume already proves Spring Boot at work, so the portfolio adds breadth and feeds the AI phase; "I've shipped in both stacks" beats two Java repos. (Prefer to build Relay in Spring Boot instead? Say the word — the plan flexes.) If the W8 mock is shaky, we insert a dedicated Java week before applications go out.

**LLD / machine-coding thread (W5–8, ~1.5h/week):** Indian startups (Razorpay, Tekion, Chalo, Zepto…) gate backend hires with a 60–120-min *working-code* design round. One problem per week, **in Java** (double duty with the revision thread): W5 Parking Lot → W6 Logger (an actual Razorpay task) → W7 Rate Limiter → W8 Splitwise. Bar: clean OO modeling + running code + defended design. Full LLD mock in W21.

**🎯 MILESTONE (Oct 18): Backend-interview-ready — Python AND Java/Spring. Start applying to backend roles — referrals + direct hiring-manager outreach first (title filters die at the ATS, not in interviews). Resume v1.**

### Phase 3 — AI Engineer (W9–12 · Oct 19 → Nov 15)
*Your MCP exposure at JCI + FastAPI = fastest path to the hottest market.*

| Wk | Topic | Build (Capstone 2) | DSA |
|---|---|---|---|
| 9 | LLM foundations: tokens, context, sampling, Claude/OpenAI APIs, serious prompt engineering, structured outputs | CLI that extracts structured data from messy docs | Graphs I (6) |
| 10 | Tool use & MCP: function calling, agent loop from scratch, **build your own MCP server**, streaming | **Capstone 2 "DocMind"** start: MCP server + tool-using assistant | Graphs II (6) |
| 11 | RAG: embeddings, chunking strategies, pgvector, hybrid search, reranking, citations | DocMind: RAG over a real document corpus with cited answers | Intervals & greedy (6) |
| 12 | Evals & agents: golden sets, LLM-as-judge, regression evals in CI, guardrails, cost/latency engineering | DocMind: **eval harness (built FIRST — your SDET edge) + deployed + 3-min recorded walkthrough** (take-home reviewers now expect one) | 1-D DP (6) |

**🎯 MILESTONE (Nov 15): AI-Engineer-ready. Apply. Resume v2 (MCP story front and center).**

### Phase 4 — ML Engineer (W13–17 · Nov 16 → Dec 20)
*Your biggest gap — 5 focused weeks, classical-first because that's what junior MLE interviews test.*

| Wk | Topic | Build (Capstone 3) | DSA |
|---|---|---|---|
| 13 | ML core: bias-variance, train/val/test, metrics (precision/recall/ROC-AUC), linear & logistic regression (once from scratch in NumPy) | Regression from scratch + sklearn comparison notebook | 1-D DP II (6) |
| 14 | sklearn mastery: trees, random forest, gradient boosting/XGBoost, pipelines, cross-validation, tuning | **Capstone 3 "PredictMaint"**: predictive-maintenance model on public sensor data (ties to your IoT story) | 2-D DP (6) |
| 15 | Real-world ML: feature engineering, leakage, imbalanced data, interpretation (SHAP) | PredictMaint: feature pipeline + honest evaluation report | Timed easy/med sets |
| 16 | PyTorch: tensors, autograd, training loop, simple nets, transfer learning, DL-vs-classical judgment | Small PyTorch project (e.g., fine-tune a text classifier) | Timed sets |
| 17 | MLOps: MLflow tracking, model serving via FastAPI, monitoring & drift, data/model versioning | PredictMaint: **served + tracked + monitored + deployed** + written end-to-end project narrative + walkthrough mock (the highest-weight MLE round) | Timed sets |

**🎯 MILESTONE (Dec 20): Junior/mid MLE-ready. Apply. Resume v3.**

### Phase 5 — Data Analyst Sharpening (W18–20 · Dec 21 → Jan 10)
*You interned in this — 3 weeks of polish, mostly stats + hard SQL + storytelling.*

| Wk | Topic | Build (Capstone 4) |
|---|---|---|
| 18 | Statistics: distributions, sampling, confidence intervals, hypothesis testing, A/B testing end-to-end, common traps | A/B test analysis writeup on real experiment data |
| 19 | Analytics SQL: cohort/retention/funnel queries, gaps-and-islands (consecutive-days problems), hard window-function drills + metrics design | 25 hard SQL drills + metrics doc |
| 20 | Excel power tools (XLOOKUP, INDEX/MATCH, pivot tables, what-if analysis) + Power BI advanced, DAX basics, dashboard design, exec communication | **Capstone 4: analytics deep-dive — Excel workbook + published dashboard** + 30-min TIMED drill: raw data → clean → pivot → mini-dashboard (analyst loops test exactly this, live) |

**🎯 MILESTONE (Jan 10): Data-Analyst-ready (senior-intern → analyst level).**

### Phase 6 — FDE + Interview Gauntlet (W21–24 · Jan 11 → Feb 7)
*FDE = backend + AI + data + consulting craft. Then we drill interviews hard.*

| Wk | Topic | Deliverable |
|---|---|---|
| 21 | System design I: load balancing, caching, queues, sharding, consistency, capacity estimation, API design | 2 full design docs (I review like an interviewer) + 90-min LLD mock (machine coding, in Java) |
| 22 | System design II + AI system design: design a RAG platform, ML serving at scale; take-home simulation | 1 AI system design + timed take-home |
| 23 | FDE craft: **48-hour POC drill** (I play a fuzzy customer, you scope + build + demo), **decomposition case drills** (Palantir-style: "reduce a city's 911 response times" — the FDE signature round, ~40% pass rate), client-roleplay ("the CTO is calling"), discovery questions, demo storytelling | POC repo + recorded demo pitch + 2 decomposition cases |
| 24 | Gauntlet: timed DSA sets, one full mock per role (5 mocks — the backend one in Java/Spring), behavioral STAR bank (12 stories), resume vFinal, application tracker | Interview-ready across all 5 roles |

**🎯 MILESTONE (Feb 7): FDE-ready. Full portfolio: 4 capstones + POC, ~150 DSA problems solved, 5 resume versions.**

---

## 4. Continuous threads (run every week)

- **DSA:** NeetCode-150 ordering, 6/week baseline W1–14, timed mixed sets W15–24 → ~150 problems total. Log every solve in `progress/`.
- **Java/Spring:** revision thread W5–8 (drills + question banks + mock), then keep 2 DSA solves/week in Java so it never goes cold again. Say `quiz me on java` anytime for a rust check.
- **Resume:** updated after every capstone (v1 W8, v2 W12, v3 W17, vFinal W24). Reviews live in `resume/`.
- **Applications:** start at W8 (backend), add roles at each milestone. Don't wait for "perfect."
- **Interview stories:** every week you write 1 STAR story from your real work (JCI/Onextel) into `interview-prep/stories.md` — by W24 you have 20+.
- **Spaced review:** each week's quiz includes 3 questions from prior weeks.

## 5. Capstone portfolio (what recruiters will see)

| # | Name | One-liner | Proves |
|---|---|---|---|
| 1 | **Relay** | Webhook delivery service: queued, retried with backoff, HMAC-signed, dead-lettered, load-tested, deployed with CI/CD + 3-min recorded demo | Backend at production grade |
| 2 | **DocMind** | RAG + agent service with its own MCP server, citation-grounded answers, and a regression eval harness in CI — **eval harness built first** + recorded walkthrough | AI engineering, evals maturity |
| 3 | **PredictMaint** | End-to-end predictive-maintenance ML service: features → XGBoost/PyTorch → MLflow → served → monitored | ML engineering lifecycle |
| 4 | **Analytics deep-dive** | Public-dataset investigation + A/B analysis + published Power BI dashboard + exec summary | Analyst rigor + storytelling |
| + | **48h POC** | Fuzzy-brief-to-demo build | FDE speed + client skills |

GitHub standards: pinned repos, real READMEs (problem → architecture diagram → decisions → how to run → metrics), meaningful commit history, profile README.

## 6. Market strategy (research-backed, Aug 2026)

- **Where:** GCCs are the strongest junior absorber right now (+35% YoY in tier-2 cities) + funded startups (fintech, quick-commerce, AI) + select product companies. AI-tagged roles grew +33% YoY while plain-CRUD listings shrank — **the backend + AI combination is precisely the winning profile.**
- **Positioning:** "Backend engineer currently in an SDET seat" — lead with Onextel production work. Never "SDET looking to switch." Interviewers judge current ability; it's the **ATS/recruiter title filter** that kills SDET candidates → from W8, referrals + direct hiring-manager outreach come FIRST, portal applications second. (The LinkedIn content engine exists for exactly this.)
- **The MCP story is your differentiator** — MCP now appears in AI-engineer JDs explicitly, and almost no 1-YOE candidate has work exposure. By W12 you'll have *built* MCP servers, not just evaluated them.
- **Your SDET background is secretly an evals background** — evals are the most under-supplied skill in AI-engineer loops. Say: "I build test/eval harnesses and quality gates for LLM systems."
- **FDE sequencing (be realistic):** Indian-startup FDE / solutions-engineer / deployment roles are targetable at W24; global-lab FDE (OpenAI/Anthropic/Databricks — India-remote postings exist) realistically lands at 2.5–4 YOE with a shipped GenAI product + customer-facing evidence. The plan builds that evidence now.
- **Comp reality check (directional, 1–2 YOE):** backend — services ₹4.5–10L, product/startups ₹10–20L+, top GCCs ₹18–25L · AI engineer — ₹8–16L entry with real projects, ₹18–30L at 2–4 yrs · MLE — ₹7–14L services/GCC, ₹15–25L product · DA — ₹4–8L. Don't anchor on LinkedIn-influencer numbers.
- Cadence from W8: ~10 quality applications/week + 5 referral asks + the Thursday LinkedIn log doing inbound work. Application tracker built at W24 (or earlier — say the word).

## 7. Anti-patterns I will call out

1. Watching tutorials instead of building (I will check your commits).
2. Skipping DSA "just this week."
3. Perfecting a capstone instead of shipping it.
4. Not applying because "not ready yet." Milestones = apply dates.
5. Listing skills on the resume you can't defend for 10 minutes (current resume has a few — see review).

---

*This plan recalibrates whenever reality demands: your diagnostic score, your hours, an interview you land next week. The plan serves you, not the reverse. — Claude*
