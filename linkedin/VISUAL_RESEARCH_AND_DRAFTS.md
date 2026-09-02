# Self-Verification (Step 1)

I read both research batches that bear on visual/structural design (`visual-design` and `slide-mechanics`) with the standing instruction to distrust unsourced guru numbers. Here's what I dropped or downgraded before writing anything, and why:

**Dropped entirely (unsourced, or redundant with a better-sourced figure already verified):**
- The Zeigarnik "~90% better recall" magnitude — mechanism (interrupted tasks are recalled more) is real 1927 psychology, but that specific number doesn't trace to Zeigarnik's methodology in any source provided. I kept the mechanism, dropped the number.
- The "document posts get 40.5% vs 10.7% engagement" multiplier — no disclosed methodology, and it's redundant with the already-verified 6.6% vs <2% figures from prior research, which *do* have a traceable source. Using both would double-count the same claim at different (contradictory) confidence levels.
- pgvector's "~80% of agentic use cases" figure — SEO-content-sourced, adds nothing, not used anywhere below.

**Downgraded:**
- Van der Blom's "8-12 slides" / "5-10 slides" optimal-count claim: the entire slide-count citation graph in this niche terminates in one paywalled report with undisclosed statistics, and secondary sources can't even agree on what it says (3-10 vs 5-10 vs 8-12). I'm treating this as "a soft ~6-10 range exists as folklore" rather than a number worth designing around. Slide counts in the drafts below are chosen for narrative-structure reasons, not this.
- The AI-assisted-interview-restructuring claims (Google's specific round, Meta's, Canva's): sourced to interview-prep/coaching companies (Exponent, interviewing.io, Karat) that sell interview practice and have a commercial incentive to hype "the interview is changing." Karat's data is closer to a real proprietary dataset (they administer interviews at scale); the specific per-company claims read more like individual candidate anecdotes. Downgraded high→medium confidence, and Draft 3 below hedges this explicitly in the caption ("per a few interview-prep sources, not something I've sat myself") rather than stating it as fact.

**Flagged but not dropped — kept out of the drafts instead:**
- Redis 8.6 / Valkey 8.1 performance numbers (5x, 8% faster, 22% lower p99, 82% market share): these are vendor-reported, and one source (dragonflydb.io) is a *competitor* to both Redis and Valkey commenting on their licensing dispute — a party with its own stake in the narrative. Rather than downgrade-and-still-use, I simply exclude all of these numbers from every draft. Draft 1 uses only Siddharth's own measured number.

Nothing in the WCAG contrast standard, the Kim et al. TVCG 2023 thumbnail study, the LinkedIn dwell-time engineering blog, or the Kivetz/Urminsky/Zheng goal-gradient study needed adjustment — these are real, checkable, and I raised no objection to how the research already tagged them.

---

# The Report: Visual & Structural Design for Technical LinkedIn Carousels

*Scope: synthesizes the `visual-design` and `slide-mechanics` research batches — both are genuinely about how a carousel looks and is structured. The `current-topics` batch isn't re-reported here; it's used only to select what the three drafts below are about.*

### A. The cover: does a bold hero-stat beat a text-only cover?

Direct answer to the question posed in the goal: **neither extreme wins outright, and no one has actually run this A/B test for engineering carousels.** The real evidence is indirect but points the same direction —

- **[INFERENCE|medium]** No controlled test of "hero-stat cover" vs. "text-only cover" for data/engineering carousels exists in what was found. The nearest real evidence is Stanford's Aaker research on story-vs-statistic recall, which found a bare number is recalled far worse than a number embedded in a short frame. Applied here: a bare "20%" with nothing else is the *weak* pattern, not the strong one — the winning shape is **number + one short framing clause** ("20% faster p95. Here's the pattern — and where it breaks."), not bare-number-alone or headline-alone. *(buffalo7.co.uk/blog/storytelling-with-data; kaushik.net)*
- **[MEASURED|high]** At thumbnail size, chart axis labels and tick marks are the first element to become illegible, and a thumbnail-optimized chart needs different simplification than the full-size version — not just a shrunk copy of it. Practically: the cover carries **typography, not a chart** — put the actual axes/precision on the slide the reader reaches *after* tapping in. *(Kim et al., IEEE TVCG 2023 — arxiv.org/html/2305.17051v1)*

### B. Chart and data-viz idioms that survive feed-thumbnail size

- **[MEASURED|high]** Axis tick labels degrade first as chart width shrinks; different chart elements (color fill, shape, clutter) trade off attention vs. interpretability differently at small size. *(Kim et al. 2023)*
- **[REPORTED|medium]** Practitioner mobile-dashboard guidance converges on ≤5-7 bars/categories, vertical stacking over dense side-by-side, and treating tick labels/gridlines as removable. *(querio.ai; uxpin.com)*
- **[INFERENCE|medium]**, extending the above: for a before/after comparison, 2 bars with the value printed directly on each bar (no axis at all) is safer than any bar chart with a labeled axis — it should read as "short bar vs. tall bar" without requiring the eye to find and parse a scale. For a simple X-of-N ratio (e.g., a test score), a filled/unfilled dot or icon grid reads faster than a bar chart, since there's no axis question at all — this is my own extension of the bar-chart finding, not something directly sourced.

### C. Color, contrast, dark vs. light

- **[MEASURED|high]** WCAG 2.1 AA: 4.5:1 minimum contrast for normal text, 3:1 for large text (≥18pt/24px, or bold ≥14pt/19px) and for meaningful graphical elements. Treat this as a **floor**, not a target — feed thumbnails re-compress further (JPEG/PNG re-encode, phone auto-brightness). *(uxpin.com; pencilandpaper.io)*
- **[MEASURED|medium]** No universal winner between light and dark mode for reading/comprehension — it genuinely depends on task and lighting. The one finding with a clear direction: as text shrinks, light-mode/high-contrast holds up better than light-on-dark. *(nngroup.com; boia.org; ceur-ws.org/Vol-3575/Paper15.pdf)*
- **Applied rule for the drafts below:** cover slides may use a dark background if the hero element is large (size compensates for dark-mode's small-text weakness), but every data/caption slide with smaller text defaults to a **light background, dark high-contrast text**, checked against WCAG AA as a floor.

### D. Text density per slide

- **[REPORTED|medium]** Practitioner consensus places "too much text" at roughly 40-50 words per slide — a design heuristic, not a measured threshold, but it's consistent with a real mechanism: **[INFERENCE|medium]** working-memory/chunking research (generalized from classroom contexts, not carousels specifically) supports one idea per slide as reducing the load a reader has to hold mid-swipe. *(smallppt.com; nngroup.com/minimize-cognitive-load; pubmed.ncbi.nlm.nih.gov/29698045)*
- Working rule: one idea, one number or one short sentence per slide — roughly tweet-length, not a paragraph.

### E. Code snippets on slides

- **[REPORTED|medium]** Practitioner consensus (no controlled study): monospace font, generous line-height, syntax highlighting, ~5-8 lines max, one concept per snippet. Legible-at-thumbnail-size beats completeness — this is the one place where showing *less* of the real code with a *bigger* font beats showing the whole function. *(poper.ai; snappify.com)*

### F. Slide count and pacing mechanics

- **[MEASURED|high]** LinkedIn's own engineering team has confirmed dwell time (active engagement time after opening a post) is a deliberate, trusted ranking signal, distinct from click-through. A carousel that gets swiped slide-by-slide structurally generates more dwell time per impression than a single-read text post — this is a real mechanical advantage of the *format*, independent of any one slide's design. *(linkedin.com/blog/engineering/feed/understanding-feed-dwell-time)*
- **[MEASURED|high]** The goal-gradient effect (Hull; replicated by Kivetz, Urminsky & Zheng 2006 on real loyalty-program completion data) is real: perceived proximity to a finish line increases persistence, and the effect is *strongest* when the start already reads as in-progress rather than at zero. **[INFERENCE]** applied to carousels: a visible page counter on every slide (starting the cover at "1/N," not unnumbered) is a documented lever for getting to the last slide, not folklore.
- **[REPORTED|medium]** The Zeigarnik effect (mechanism real, 1920s psychology; magnitude unverified — see drop above) supports ending a slide mid-thought to pull the reader forward — but the research explicitly warns this reads as manipulative "AI slop" if done on every slide. **Rule applied below: reserve it for exactly one structural pivot per carousel** (problem → reveal, or setup → fix), never as a per-slide tic.
- **[INFERENCE|high, meaning: high confidence this evidence gap is real]** No credible, methodologically transparent measurement of LinkedIn-*document*-carousel swipe-through or per-slide drop-off exists anywhere in what surfaced. Every specific percentage in this niche (15-25%, 40-75%, "slide 3 is where people drop off") traces to unsourced marketing blogs, not LinkedIn's own data or an independent study. **This directly answers the goal's question "how many slides actually get swiped through vs. abandoned": nobody outside LinkedIn can say, and any draft or design rationale claiming otherwise would be borrowing rigor that doesn't exist.** *(postnitro.ai, postunreel.com — both flagged as unsourced, not treated as evidence)*

### G. Closing slide / CTA

- **[REPORTED|low]** Marketing-design sources (not lab-tested) suggest the final slide should carry one specific, closed-ended question rather than an open-ended or generic ask. This creates real tension with the already-validated pillar of ending on an *honest, unresolved* observation rather than a resolved conclusion. **Resolution used in the drafts below:** keep the honesty and the open framing (never fabricate a resolution he doesn't have), but make the question concrete and one-line-answerable — e.g., not "thoughts on caching?" but "jitter, locking, or something else — what actually worked for you?" *(usevisuals.com; pineable.com)*

### H. What's still thin or absent — do not treat as solved

1. Per-slide swipe-through/completion data — **does not exist publicly.** (Section F above.)
2. The "optimal" slide count — a folklore range (~6-10), not a measured number; any specific count in the drafts below is chosen for message structure, stated as such.
3. Hero-stat-vs-text-cover as a direct A/B — no such study exists; the Aaker-derived inference (number + framing clause) is the best available substitute, not a confirmed winner.
4. Zeigarnik's exact recall magnitude — mechanism credible, "90%" figure unverifiable, not used.

---

# Three Ready-to-Post Drafts

All three use **only** facts given in CTX (Onextel-era backend metrics, the MCP evaluation at work, the 22/25 diagnostic result). No employer or Pramaan specifics are named anywhere. Where a stronger version of a post would need a number Siddharth hasn't measured, the draft says so explicitly rather than inventing one — flagged inline below each draft.

## Draft 1 — Cache-aside postmortem (Onextel-era backend work)
**Pillars:** 1 (a benchmark he actually ran) leading into 3 (honest postmortem, ends unresolved).
**Unmeasured gap, stated explicitly in the post itself:** how the setup behaves under an actual cache stampede — not invented, named as an open question.

**Hook:**
> A cache-aside pattern I built cut p95 latency by ~20%, in a past role. Here's the pattern — and the one failure mode I still haven't tested.

**Caption (ready to paste):**
```
A cache-aside pattern I built cut p95 latency by ~20%, on a system doing 10M+ requests a month in a past role.

The pattern itself is simple.
Read from Redis first.
Miss? Read Postgres, write the result back to Redis, return it.
Hit? Skip the database entirely.

Simple to describe. Easy to get wrong in one specific way.

What happens when a hot key expires and 500 requests land on it in the same second?

Every one of them misses. Every one of them hits Postgres at once. That's a cache stampede.

I don't have a clean, measured answer for how our setup would behave under that. Request coalescing and TTL jitter are the two fixes I'd want to test before trusting this pattern at higher scale.

The 20% number is real. The stampede question isn't answered yet. I'd rather post it that way than pretend the second part is solved.

If you've hit cache stampede in production — jitter, locking, request coalescing, or something else — what actually worked?

#BackendEngineering #Redis #PostgreSQL #Caching #SystemDesign #SoftwareEngineering #DistributedSystems
```

**Slide outline (7 slides):**
1. **Cover** — hero number "~20%" large/bold, ≥3:1 contrast, one short framing line beneath: *"faster p95. The pattern — and the failure mode I haven't tested."* Counter "1/7." No chart — typography only (per §A, §B).
2. **Context** — one line: *"A system doing 10M+ requests/month. Every ms on the read path multiplies."* Simple request/server pictogram.
3. **The pattern** — 3-box flow diagram: Request → Redis (hit) / miss → Postgres → write-back. Diagram carries it, minimal words (§D).
4. **The result** — 2 bars only, before/after p95, values printed on the bars, no axis (§B).
5. **The turn** — one line, tonal shift (accent color, not alarm-red): *"But cache-aside doesn't protect you from this."* The single deliberate mid-thought cutoff in this deck (§F).
6. **The stampede** — diagram: one expiring key, N concurrent requests, N simultaneous DB hits. Label: *"no fix tested yet — jitter or request coalescing."*
7. **Close** — restated honest line + the concrete comment prompt. Counter "7/7."

## Draft 2 — MCP goes stateless (MCP/AI angle)
**Pillar fit:** closest in spirit to pillar 2 (reacting to a primary-source spec change, honest about what's unverified firsthand) — there's no single number to reproduce here, so it's an adjacent variant, not a literal fit. Flagged rather than forced.
**Unmeasured gap, stated explicitly:** he hasn't run two MCP instances behind a load balancer himself — named as the open test, not claimed as done.
**Fully generic per CTX:** no mention of employer or what he evaluated MCP *for.*

**Hook:**
> MCP just went stateless. If you've scaled a REST API behind a load balancer, you already know why that matters.

**Caption (ready to paste):**
```
MCP — the protocol a lot of AI agent tooling is built on — just changed how it handles connections.

Until recently, an MCP server kept a persistent, stateful connection open per client.

Fine for a demo. A known problem the moment you run more than one instance behind a load balancer.

The July 28, 2026 spec update moves MCP to stateless-per-request.
Cacheable list results. Header-based routing. Multi-round-trip requests as a first-class feature, not a workaround.

That's the same trade REST made over the stateful protocols it replaced. No sticky sessions. No server holding client state in memory. Any instance can answer any request.

I've spent time this year evaluating MCP-based tooling at work. Reading this spec change land, my first thought wasn't about agents — it was about how many times I've made this exact statelessness trade on a normal REST service just to make it scale horizontally.

What I haven't done yet: actually run two MCP server instances behind a load balancer and watch the stateless version behave the way REST does. That's the test that would make this more than a spec-reading exercise.

If you've run MCP servers in production — has the stateless change simplified deployment, or moved the hard part somewhere else?

#MCP #ModelContextProtocol #BackendEngineering #APIDesign #SoftwareArchitecture #SystemDesign #AIAgents
```

**Slide outline (6 slides):**
1. **Cover** — no number to lead with (architectural, not a benchmark post) — big visual contrast instead: *"STATEFUL"* (struck through) → *"STATELESS."* Subtext: *"What MCP's July 2026 spec change means for scaling agent infra."* Counter "1/6" (§A note: cover doesn't need a hero stat, but does need one dominant idea/visual).
2. **Old model** — diagram: client ↔ persistent connection ↔ one MCP server. Label: *"works until you need a second instance."*
3. **What changed** — 4 short labeled chips (not a bulleted paragraph): *Stateless per request / Cacheable list results / Header-based routing / Multi-round-trip, native* (§D — chips read faster than a bullet list at thumbnail size).
4. **The REST analogy** — side-by-side diagram: REST (N instances behind a load balancer, any instance answers) next to the old MCP model, converging toward it. The "why backend engineers should care" slide.
5. **The honest gap** — one line: *"Reading the spec and running it are different things. Haven't put two MCP instances behind a load balancer yet."*
6. **Close** — concrete question restated. Counter "6/6."

*(Note for the parent session: Postgres 18's `uuidv7()` is a stronger literal pillar-2 candidate — a small, self-runnable before/after on index locality — but only once Siddharth has actually run that test. Flagging as a future draft, not fabricating it now.)*

## Draft 3 — Interview comprehension trend + his own diagnostic (current topic)
**Pillar fit:** 3, cleanly — postmortem of his own diagnostic, ends on an honest gap, not a resolved win. This is the research's own strongest-flagged hook.
**Hedge applied per self-verification:** the interview-restructuring claim is explicitly attributed to secondhand sources, both in the caption and on-slide, not stated as verified fact.

**Hook:**
> Big tech interviews are reportedly grading code comprehension now, not just code-from-scratch speed. I ran myself through a comprehension-style self-test to see where that would actually catch me.

**Caption (ready to paste):**
```
A few companies have reportedly rebuilt technical interviews around AI-assisted coding this year.

Google added a round graded on reading and debugging an existing codebase with an AI assistant available, not writing from a blank file — per a few interview-prep sources I've read, not something I've sat myself.

What stuck with me: the skill being graded isn't "can you write the algorithm." It's whether you can read code fast, validate what a tool gives you, and catch what's subtly wrong.

So I ran a 25-question self-test built around exactly that — reading and reasoning about code, not writing it from scratch.

Score: 22/25.

The 3 I missed weren't concept gaps. They were fluency gaps:
— a list comprehension where I misjudged what got filtered
— why a mutable type can't be a dict key
— whether sorted() with a key function keeps the original order on ties

I knew all three concepts. I was slower and less certain reading the actual code than I expected.

If code-reading is genuinely becoming the graded skill, "I understand hashability" and "I read that line correctly in 4 seconds under pressure" are two different skills.

Right now I only have real evidence for the first one.

Have you tried a comprehension-style self-test on your own code recently? What did it catch that you didn't expect?

#TechnicalInterviews #SoftwareEngineering #Python #CodingInterviews #CareerGrowth #BackendEngineering #AIAssistedCoding
```

**Slide outline (7 slides):**
1. **Cover** — hero number "22/25" large/bold + framing line: *"The 3 misses taught me more than the 22 hits."* Counter "1/7" (§A: number + framing clause, not a bare score).
2. **Why this test** — one line, hedge visible on the slide itself, not just in the caption: *"2026: a few companies reportedly grade code-reading and debugging, not just writing from scratch — per interview-prep sources, not verified firsthand."*
3. **The test** — *"25 questions. Read and reason about code — no writing, no LLM."* Simple icon.
4. **The score, visually** — 25-dot/icon grid, 22 filled + 3 outlined (§B: reads as a ratio instantly, no axis needed for a simple X-of-N count).
5. **The 3 misses** — one short line each with a small syntax-highlighted code fragment, large font: `[x for x in … if …]` (filtering misjudged), `{mutable: …}` (why it can't be a key), `sorted(x, key=f)` (tie order) (§E: fragments, not full functions).
6. **The reframe** — *"Concept gap vs. fluency gap. I knew all three. I was slow reading them under pressure."*
7. **Close** — concrete question restated. Counter "7/7."

---

## Grounding check (all three drafts)

- Draft 1 numbers: 10M+ requests/month, ~20% p95 cut, Redis cache-aside, PostgreSQL — all from CTX's Onextel evidence. Employer not named; "past role" framing used deliberately since this predates his current job.
- Draft 2: "evaluating MCP-based tooling at work" — matches CTX's sanctioned generic framing exactly ("evaluated MCP tooling at his day job... employer never named"). No specifics of what it was evaluated for.
- Draft 3: 22/25, the 3 specific Python misses (comprehension filter, hashability, `sorted(key=)` stability) — verbatim from CTX's diagnostic result. No fabricated interview claims about himself — only his own test result is asserted as fact; the industry trend is explicitly sourced as secondhand.
- No draft names Onextel, JCI, or Pramaan. No draft states a number Siddharth would need to go measure as if it were already measured — each such gap (stampede behavior, load-balanced MCP behavior) is named as an open question instead.