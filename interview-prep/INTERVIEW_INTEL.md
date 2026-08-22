# Interview Intelligence — India, 1–2 YOE, researched Aug 2026

Compiled from ~50 web searches across verified 2025–26 interview experiences, JD analyses, and prep guides. This is the *ground truth* the master plan trains against. Salary figures are directional (sources conflict); loop structures are well-corroborated.

---

## 1. Backend / SDE-1

### The loop by company type

| Company type | Typical loop | Flavor |
|---|---|---|
| Product (Amazon, Walmart, Uber, Oracle) | OA (2–3 problems, 60–100 min, HackerRank) → 2–3 live DSA rounds → HM/behavioral | LC-medium center of gravity; behavioral woven INTO coding rounds (Amazon Leadership Principles); standalone HLD rare at SDE-1 — design appears as OOD + DB schema follow-ups |
| Funded startups (Razorpay, Blinkit, Tekion, Chalo, Zepto) | OA → DSA → **LLD/machine coding (60–120 min, working code)** → HLD-lite chat → HM/culture | Machine coding is the signature round. Verified 2025: Tekion & Chalo both asked **chess**; Razorpay asked a **logger** routing logs to file/web/console |
| GCCs (JPMC, Wells Fargo, S&P) | OA → 3–4 rounds blending lighter DSA + **heavier Java/Spring/SQL/project questioning** → managerial → HR | "Can you build and explain production Java services" > LeetCode athleticism |
| Services lateral (Infosys/TCS) | 2 tech rounds + managerial | Project walkthrough, Collections, live Streams coding, SQL, Spring Boot. Little LeetCode |

### DSA expectations
- **LC-medium is the bar.** Live rounds ≈ 2 mediums in 60 min; brute-force → optimal narration is explicitly rewarded.
- Hot topics from 2025 loops: arrays/strings/hashing (dominant), two pointers/sliding window, binary search (Rotated Sorted Array — Tekion), trees/BFS/DFS, graphs (Rotten Oranges — Amazon; topological sort — Blinkit), heaps/intervals (Railway Platforms — Amazon), 1-D DP (House Robber + circular — Blinkit), LRU Cache, Number of Islands.
- Community consensus: **150–250 well-understood problems** suffices. (Plan targets ~150 + timed sets — on track.)

### Java/Spring topics ranked by frequency
1. **HashMap internals** (put/get, collisions, Java-8 treeification) — near-universal
2. equals()/hashCode() contract (what breaks in a HashSet)
3. Spring Boot vs Spring, auto-configuration, starters, annotations (@Component vs @Service; @Controller vs @RestController)
4. String pool, immutability, StringBuilder (+ output-prediction questions)
5. Java 8 Streams/lambdas — **live coding**: "group employees by dept, max salary each"
6. **@Transactional under the hood** — proxies; the **self-invocation trap** (#1 trap question); propagation; rollback rules
7. JPA/Hibernate: N+1 selects, LazyInitializationException, fetch joins
8. Concurrency: volatile vs synchronized, ExecutorService, ConcurrentHashMap (Java 8: CAS + per-bucket sync)
9. REST exception handling (@ControllerAdvice), status codes, idempotency for payment retries
10. JVM/GC + OutOfMemoryError diagnosis (heap dump, GC logs); Actuator monitoring

### LLD / machine coding (startup gate)
60–120 min, **running code** (in-memory stores, no DB), then a defended code review. Scoring ≈ structure 30% / working 25% / SOLID 20% / extensibility 15% / edges 10%. Most-asked: **Parking Lot, Snake & Ladder, Vending Machine, Shopping Cart** → then Elevator, **Chess**, Movie Booking → **Rate Limiter, Logger, Splitwise, LRU Cache, Notification Service, Wallet**. At 1–2 YOE the bar = clean OO modeling + working code, not perfect concurrency.

### Market + transition notes
- GCCs are the strongest junior absorber (+35% YoY in tier-2 cities); AI-tagged roles growing +33% YoY while plain-CRUD listings shrink — **backend + AI story wins**.
- **AI-cheating crackdown is real**: 38.5% of candidates flagged in one 19k-interview study → stricter proctoring, more in-person finals, "explain your reasoning live" pressure. (This is why the plan bans AI on exercises — fluency must be yours.)
- **SDET→backend:** interviewers judge current ability, not title. Lead with Onextel: *"backend engineer currently in an SDET seat."* The blocker is ATS/recruiter title filters → mitigate with referrals + direct hiring-manager outreach, not more portal applications.
- Comp (directional, 1–2 YOE): services ₹4.5–10L · mid-size ₹6–12L · product/startups ₹10–20L+ESOPs · top GCC/product ₹18–25L+ (Walmart SDE-1; Microsoft ~₹24.8L median TC).

---

## 2. AI Engineer / GenAI Engineer

### The loop (4–6 stages; 60%+ GenAI content, classical-ML depth NOT required)
Recruiter screen → practical Python coding (API integration, parsing — not hard LeetCode; some companies now *observe* AI-assisted coding) → LLM/GenAI concepts (45–60 min) → **AI system design** (design a RAG chatbot / doc pipeline / multi-agent system) → **take-home (2–7 days) + 45–90 min defense** → behavioral. Consulting/GCC variants (e.g., McKinsey QuantumBlack) mix in a light ML-vocabulary round.

### Topics ranked (five clusters ≈ 90% of loops)
1. **RAG architecture** — chunking, embeddings, vector DBs, hybrid search, reranking (top JD skill; 40%+ of take-homes)
2. **Agents / tool use / function calling** (30%+ of take-homes)
3. **Prompting + structured outputs** (ReAct, self-consistency, JSON schemas)
4. **Evals** — golden sets, LLM-as-judge, RAGAS — *the single biggest differentiator; most candidates skip it*
5. LLM fundamentals (tokenization, context, temperature/top-p — and why temp=0 isn't deterministic)
6. Hallucination mitigation ("the #1 enterprise blocker") · 7. Cost/latency (caching, routing, streaming) · 8. Fine-tune vs RAG framework · 9. Guardrails (PII, prompt injection) · 10. **MCP — now explicitly in JDs**, called "baseline for agentic work"

### Question bank highlights
- Why does naive RAG fail in production (bad chunking, lost-in-the-middle, top-k stuffing)?
- Do you actually NEED a vector DB? When does pure vector search fail (exact terms, IDs)?
- How do you evaluate a RAG system (RAG triad: faithfulness / answer relevance / context relevance)?
- LLM-as-judge — biases, calibration against human labels?
- How does function calling work; tool-schema design; handling failed calls?
- Agent vs workflow — when would you NOT build an agent?
- **What is MCP; how does it differ from plain function calling; MCP security (injection via tool results)?**
- Keep p95 under ~800ms on a frontier model (streaming, semantic caching, small-model routing)
- "Tell me about an LLM feature that failed in production"

### Take-homes — what reviewers score
Functional correctness → **evaluation methodology (BUILD THE EVAL HARNESS FIRST — biggest differentiator)** → architecture → production readiness (caching, monitoring, cost, PII) → tests → README with trade-off rationale. One disclosed rubric: 30% functionality / 30% challenge completion / 25% context engineering / 15% code quality. **A recorded video walkthrough is increasingly expected.**

### Sid-specific edges
1. **SDET background = evals background.** Position: "I build test/eval harnesses and quality gates for LLM systems." This is the rarest skill in the loop.
2. **Real MCP work exposure is ahead of the market** — almost no 1-YOE candidate can discuss tool schemas and injection-via-tool-results from work experience. By W12 you'll have BUILT MCP servers too.
- Who hires juniors: GCCs (Bengaluru/Hyderabad), funded AI startups (Sarvam, Krutrim, Yellow.ai), unicorns, consulting AI teams. Comp directional: entry with real projects ₹8–16L; 2–4 yrs hands-on GenAI ₹18–30L.

---

## 3. Forward Deployed Engineer

### Reality check first
FDE postings grew ~800% in 2025 (Palantir model copied by OpenAI, Anthropic "Applied AI Engineer", Databricks, Scale, ElevenLabs). **Most want 2–4+ YOE.** Verified India-remote postings exist (OpenAI "AI Deployment Engineer – Startups, India"; Databricks "AI Engineer – FDE, Remote India"). Palantir = relocation (no India engineering office).
**Sequencing for Sid: Indian-startup FDE / solutions-engineer / deployment roles at W24 → global-lab FDE at 2.5–4 YOE** with a shipped GenAI product + eval harness + customer-facing evidence.

### The loop (5–8 stages)
Screen ("why FDE, not SWE?") → project deep-dive → practical coding (realistic, not LeetCode) → system design under enterprise constraints → **decomposition case (THE signature round: ~40% pass rate, ~30% weight)** → client-simulation roleplay → behavioral. Palantir onsite pool: decomposition, learning (apply an unfamiliar library live), coding, re-engineering (debug a several-hundred-line codebase), design — AI tools banned. OpenAI: ~5-hr take-home on their APIs **+ recorded video treated as a customer demo**.

### Reported exercises
- Decomposition: reduce a city's 911 response times · unify fraud detection across 3 legacy bank systems · pharma AI assistant with IP constraints
- Coding: **rate limiter with per-user + global limits (Anthropic favorite)** · parse messy CSVs · streaming consumer with backpressure · small RAG pipeline over a folder · diagnose a slow SQL query · paginated API fetcher
- Roleplay: "Client insists on a suboptimal approach — what do you do?" · "Deployment slipped 3 weeks; the CTO is calling."

### How "customer-facing" is scored
Diagnostic questions BEFORE solutions · name your assumptions · ownership language ("I'll have this by Friday") · acknowledge what the customer is right about before pushing back · options with explicit trade-offs · calibrated commitments · plain-language explanations of AI limits. Failure modes: silence and jargon.

---

## 4. ML Engineer (junior/mid)

### The loop
3–5 rounds. Product/GCC: DSA still gates (LC easy-medium) → ML breadth round → light ML system design ("design churn prediction" — a *discussion*: framing, metric, baseline, imbalance, monitoring — not distributed-serving depth) → behavioral. Analytics services (Fractal, Tiger, Tredence, Quantiphi): aptitude + light DSA → Python/pandas coding → theory rapid-fire + **project end-to-end walkthrough (the highest-weight round at this level)** → client-case → HR. Startups: ML coding from scratch (k-NN, k-means, a metric) + take-homes.

### Theory ranked by frequency
1. Bias–variance / overfitting (the #1 question everywhere) · 2. Metrics: precision/recall/F1, ROC-AUC, **"when accuracy lies"** (scenario forcing a precision-vs-recall choice) · 3. Regularization L1/L2 (why L1 → sparsity) · 4. Cross-validation & tuning (stratification; time-series CV) · 5. **RF vs XGBoost, bagging vs boosting** (India = tabular-heavy) · 6. Imbalanced data (SMOTE, class weights, PR-AUC) · 7. Feature engineering/encoding/scaling · 8. **Data leakage** (the "real experience" probe) · 9. **Transformer/LLM basics now expected of MLEs** (attention, embeddings, fine-tune vs RAG, hallucination) · 10. Backprop/GD intuition; when DL vs classical · 11. k-means/PCA/outlier detection (**your KNN internship is directly reusable**)

### MLOps at 1–2 YOE
Awareness-level only: drift types, monitoring, MLflow tracking/versioning, FastAPI+Docker serving, retraining triggers. "I containerized a FastAPI model server and tracked runs in MLflow" puts you ahead. **Your backend+SDET profile maps perfectly onto "MLE = SWE who productionizes models."**

- Hireable without Masters: yes — analytics services, GCCs, startups (portfolio substitutes). Comp directional: services/GCC ₹7–14L; product/AI-startup ₹15–25L (scarcer, portfolio-gated). GenAI-skilled juniors command a premium.

---

## 5. Data Analyst

### The loop
3–5 rounds: screen → **SQL live coding (the universal make-or-break round)** → Excel/Python analytical round → **business case + guesstimate** → HR. Verified 2025: Zomato = 5 rounds (SQL joins/subqueries/window functions + Excel + guesstimate); Flipkart = 4–5 SQL questions + stats, then 2 case rounds; Swiggy = SQL screen, then window functions/CTEs/optimization + mini case.

### SQL ranked + hot questions
Joins → **window functions (highest-signal: ROW_NUMBER vs RANK vs DENSE_RANK, LAG/LEAD, running totals)** → GROUP BY/HAVING → CTEs → dedup patterns → **date logic & cohort/retention** → UNION vs UNION ALL, indexes.
Classics: 2nd-highest salary per dept · Jan-but-not-Feb customers (anti-join) · 7-day rolling average · MoM growth % (LAG) · top-3 per region · **consecutive login days (gaps-and-islands — the hard tier)** · month-1 retention by cohort · INNER vs LEFT JOIN row counts with duplicate keys (the trap).

### Excel — tested LIVE
Given raw data: **clean it → pivot table → mini-dashboard in 20–30 minutes.** Checklist: XLOOKUP/VLOOKUP/INDEX-MATCH (+ "VLOOKUP vs XLOOKUP" theory), SUMIFS/COUNTIFS, IFERROR, TRIM/TEXTJOIN, dynamic arrays (FILTER/UNIQUE/SORT), pivots + calculated fields, conditional formatting, Power Query.

### Stats, cases, BI
- Stats: mean vs median, CLT, p-value, CIs, Type I/II, correlation≠causation, IQR outliers, imputation. A/B: H0/H1, metric choice, power conceptually, peeking pitfall.
- Case staple: **"DAU dropped 15% — investigate"** → validate tracking → incidents/releases → segment (platform/geo/new-vs-returning) → internal vs external (MECE) → seasonality/competitors. *Structure is graded, not the answer.* Guesstimates persist (Zomato/Swiggy/Flipkart).
- **Power BI leads Tableau ~3:1 in India** (~72% of analytics JDs — Microsoft-stack enterprises, BFSI). DAX bar: calculated columns vs measures, row vs filter context, CALCULATE, time intelligence, star schema. **Your Power BI internship is directly marketable — be ready to demo a dashboard and defend DAX choices.**
- Analyst → DS/MLE at 18–36 months is India's standard upward path (30–60% bump). Comp directional: ₹4–8L at 0–2 YOE, product/fintech higher.

---

## 6. Cross-cutting truths (all roles)

1. **Project deep-dive rounds outweigh trivia at 1–2 YOE.** Every capstone needs a rehearsed end-to-end narrative: problem → decisions → what broke → what you'd redo.
2. **Referrals beat portals** — title filters (SDET) die at the ATS layer, not in interviews. Weeks 8+ application strategy = referrals + direct HM outreach + LinkedIn presence (the content engine exists for exactly this).
3. **Proctoring is tightening; in-person finals returning.** Fluency must be live and explainable — practice narrating solutions aloud (mocks will enforce this).
4. **Every number on the resume gets probed.** stories.md is not optional homework.
5. Behavioral is woven into technical rounds (Amazon LPs et al.) — STAR stories must be reflexive, not recited.

## Plan mapping (what changed because of this research)

| Finding | Plan change |
|---|---|
| LLD/machine coding gates startup backend loops | **NEW: LLD thread W5–8** — 1 problem/week in Java (Parking Lot → Logger [real Razorpay task] → Rate Limiter → Splitwise); LLD mock in W21 |
| Evals = #1 AI differentiator; SDET = evals background | DocMind (W10–12) builds the **eval harness FIRST**; resume/interview positioning updated |
| FDE decomposition round is the gate | W23 adds decomposition case drills (911-response-time style) + client roleplay |
| Take-homes expect recorded video walkthroughs | DocMind + Relay both ship with a 3-min recorded demo |
| MLE loops: project walkthrough = highest weight; LLM basics expected | W17 adds written project narrative + walkthrough mock; P3 (AI phase) already precedes P4 ✓ |
| Analyst Excel tested live, timed | W20 includes a 30-min timed raw-data→pivot→dashboard drill |
| Gaps-and-islands SQL, cohort/retention | W19 drill set includes them explicitly |
| Referrals > portals for title-filtered candidates | W8 milestone includes referral-outreach playbook, not just applications |

*Full source URLs available in the research transcripts; key ones: tryexponent.com FDE guides, developersIndia wiki (SDET→dev), GeeksforGeeks/Medium 2025 interview experiences (Tekion, Chalo, Blinkit, Amazon SDE-1), DataCamp RAG/MCP/MLOps question sets, github.com/alexeygrigorev/ai-engineering-field-guide, levels.fyi India comp, Naukri JobSpeak 2026.*
