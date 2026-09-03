# Week 1 Post Kit — 3 posts, 5 asset varieties

Everything here is built and sitting in `linkedin/assets/`. Captions are paste-ready.
No employer named anywhere. No Pramaan specifics anywhere.

**Schedule — one post every 2 days:**

Superseded 2026-09-03: the p95/cache-aside carousel from the earlier session
(`linkedin/post-p95-redis.html`) went live on **2026-09-02**, covering the same
ground as Deck B below. Posting Deck B now would repeat that topic back-to-back,
so it's held out of the active queue (content preserved for a future post instead).
A "MCP in One Piece" post is also already live, low engagement (4 impressions) —
noted so the MCP-stateless post below reads as the substantive follow-up, not a repeat.

| When | Post | Variety | Upload |
|---|---|---|---|
| 2026-09-02 (done) | p95 / cache-aside | Document carousel | `linkedin/post-p95-redis.html` output |
| **2026-09-04 (next)** | Reading beats writing (interview shift) | Document carousel, 6 slides | `assets/deck-interview-shift.pdf` |
| **2026-09-06** | MCP's default token cost | Document carousel, 6 slides | `assets/deck-mcp-token-cost.pdf` |
| held / retired | Cache-aside deck (topic collision with 09-02 post) | — | `assets/deck-cache-aside.pdf` |
| held / spare | MCP goes stateless (weaker sourcing than the token-cost post) | GIF or single image | `assets/mcp-stateless.gif` |

**Added 2026-09-05:** research turned up a stronger MCP story than the stateless-spec post —
two independent sources (Anthropic's own engineering blog, and a third-party benchmark firm)
landed on the same finding: MCP's default tool-loading pattern burns 10-30x more tokens than
it needs to. That's now the 09-06 post; the stateless-spec GIF is held as a spare, not deleted.

**Rewritten 2026-09-03:** the original version of the 09-04 post scored and displayed personal
quiz results ("22/25," three Python questions missed, shown as code fragments). Sid's call:
that reads as "doesn't know Python," not as confident engineering content — the opposite of
the positioning goal. Compared directly against Hritika Kucheriya's actual posts (see below),
hers never put her own knowledge on trial; she states a confident thesis about something real
and current, backs it with specifics, and ends on a question. Rebuilt the deck on that model —
the underlying insight (reading code is a different skill from writing it) survives, but the
personal test score is gone entirely.

**Theme rotation — no palette runs more than 3-4 posts.** Posts 1-3 use `signal`
(slate + orange). Post 4 onward switches to `blueprint` (navy + teal), then `press`
(cream + amber) around post 7, then back. Build a rotation with:

```bash
python "linkedin/builders/build_assets.py" --theme blueprint
```

Non-default themes land in `assets/theme-<name>/` so nothing overwrites. To see all three
side by side before choosing: `--preview sheet.png`.

What deliberately does **not** rotate: the typographic cover, the page counter from 1/N,
the dot grid for X-of-N, the axis-free before/after bars, and the honest-gap closing slide.
Those are the structural signature that makes a post recognisably yours. Only the palette
moves. Consistency in structure plus variety in surface is what separates "recognisable"
from "templated" — and repeated identical templates are exactly what reads as AI-generated
filler now that LinkedIn ships an AI-slop report button.

**Topic rotation, same rule.** Week 1 already alternates: interview-prep (post 1),
backend/infra (post 2), AI-MCP (post 3). Keep cycling across backend/infra, AI-MCP/eval,
data, and interview-prep — four straight caching posts would pigeonhole you as narrowly as
the test-engineer label does, which is the opposite of the point.

Spare assets for filler days or reuse: `assets/singles/cache-aside-code.png`,
`assets/singles/mcp-architecture.png`, `assets/mcp-gif-frames/*.png`.

**How to upload a carousel:** Start a post → the **＋** / "Add a document" option (not
"Add a photo") → pick the `.pdf` → LinkedIn renders it as a swipeable carousel. Give it a
short document title when prompted — that title shows above the first slide.

**How to upload the GIF:** Start a post → Add a photo → pick the `.gif`. It animates in feed.

---

## Post 1 — Reading beats writing (post 2026-09-04)

**Asset:** `assets/deck-interview-shift.pdf` · document title suggestion: `Reading beats writing now`

**Why this framing:** it states an opinion with confidence, backs it with reasoning anyone
can follow, and ends on a question — never puts your own competence on trial. No score, no
"here's what I got wrong," no code fragment that could be misread at a glance.

```
A few large tech companies have reportedly rebuilt technical interviews this year — grading candidates on reading and debugging an existing codebase with an AI assistant available, instead of writing algorithms from a blank file.

The reasoning holds up the more I think about it.

When an assistant can write a working function in seconds, the bottleneck isn't "can you write it." It's "can you tell whether what it wrote is actually correct."

Those are different skills. Writing from scratch rewards recall — syntax, algorithms, a solution shape held in your head. Reading rewards something else: holding someone else's logic in your head fast enough to catch what's subtly wrong before it ships.

That's closer to what backend engineers actually do most days anyway — a PR review, a diff, a service someone else wrote six months ago. Writing-from-scratch was always a slightly artificial proxy for that.

If this shift is real, the prep changes too. Fewer blank-file algorithm drills. More: take an unfamiliar file, find the bug, explain why it's wrong.

I'd take that interview over the whiteboard version any day — not because it's easier, but because it's closer to the actual job.

Have you sat a comprehension-style round? What did it feel like against the classic algorithm interview?

#TechnicalInterviews #SoftwareEngineering #BackendEngineering #AIAssistedCoding #CareerGrowth #HiringTrends #CodingInterviews
```

**Changed from the research draft:** the original named Google specifically. The research
itself flagged the per-company claims as sourced to interview-prep vendors who sell
interview practice — likely candidate anecdotes rather than confirmed process. Naming a
company you can't defend if challenged is an avoidable risk, so it says "a few large tech
companies" and keeps the hedge on-slide as well as in the caption.

**The Hritika comparison, concretely** (her real posts, read live 2026-09-03):
- Zerobus/Kafka post: opens "It's that it makes me question whether Kafka needs to be in the architecture at all" — a thesis, not a confession — cites exact throughput numbers, ends "Would you remove Kafka if Delta were genuinely the only downstream consumer?"
- Flink migration post: the personal material is "we learned this the hard way in production," team authority earned through an incident — never "I got a question wrong."
- WASM benchmark post: "I read the actual benchmark paper before writing this post" — she's the one interrogating the source, not the one being tested.
None of her posts show her own knowledge gaps. That pattern is what this deck now follows.

---

## Post 1.5 — MCP's default token cost (post 2026-09-06)

**Asset:** `assets/deck-mcp-token-cost.pdf` · document title suggestion: `MCP is burning your tokens`

**Why this is the strongest post in the kit:** two independent sources — Anthropic's own
engineering blog, and a third-party benchmark firm with no reason to agree with them —
landed on the same finding within weeks of each other. That's about as solid as evidence
gets. It's pure agent-tooling engineering, needs no years of specialized authority, and it's
a contrarian-with-receipts take against the "MCP for everything" hype, which is exactly the
shape that travels.

```
MCP's default setup can cost 10-30x more tokens than it needs to — and two independent sources landed on the same number this year.

Anthropic's own engineering team found it first: loading every tool schema upfront, then routing every intermediate result back through the model, is the expensive way to use MCP. One real example dropped from 150,000 tokens to 2,000 — a 98.7% cut — by having the agent write code against MCP servers exposed as a filesystem instead, loading only what it actually needed.

A third party benchmarked it independently. Same 5 real GitHub tasks, same agent, same model, comparing MCP against a bare CLI tool.

MCP: 32,000-82,000 tokens per task.
CLI: 1,300-9,400 tokens per task.

Projected out to 10,000 operations a month, that's roughly $3.20 versus $55.20.

Reliability took a hit too — MCP hit 72% success against TCP timeouts, versus 100% for the CLI version, on the exact same tasks.

The protocol itself isn't the problem. Loading everything eagerly, by default, on every call, is.

I've spent time this year evaluating MCP-based tooling at work. If you're running it in production — are you loading full tool schemas on every call, or lazy-loading? What did the eager version actually cost you?

#MCP #ModelContextProtocol #AIAgents #BackendEngineering #AgentTooling #SoftwareEngineering #LLM
```

**Sources, so you can defend this if challenged:** Anthropic's own engineering blog on code
execution with MCP (the 150k→2k example); an independent benchmark from Scalekit (Aug 2026)
testing 5 real GitHub tasks, MCP vs. bare CLI, token counts and the 72%/100% reliability
split. Both are primary sources, not vendor hype about a product they're selling.

**A bug I caught before sending this to you:** the reliability slide's dot grid initially had
success and failure colors reversed — the 7 successful calls were drawn red, the 3 failures
green, which visually said the opposite of the caption. Fixed before this ever reached you.

---

## Post 2 — Cache-aside / p95 (post +2 days)

**Asset:** `assets/deck-cache-aside.pdf` · document title suggestion: `One cache, ~20% off p95`

**Before you post — check this against your own memory.** Everything here comes from your
Onextel work. The `~20%` and `10M+ messages/month` are your numbers, but you should be able
to say out loud how you measured the 20% before you publish it, because this is the post
most likely to get a "how did you measure that?" reply.

```
A cache-aside pattern I built cut p95 latency by ~20%, on a system moving 10M+ messages a month in a past role.

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

---

## Post 3 — MCP goes stateless (post +4 days)

**Asset:** `assets/mcp-stateless.gif` (7-frame animation, 230 KB) — or
`assets/singles/mcp-architecture.png` if you'd rather post a still.

**This one is verified.** I checked the spec claim against primary sources before building
it: the official MCP changelog and blog confirm the stateless rewrite, published
**28 July 2026** — the session handshake and `Mcp-Session-Id` are gone, list results carry
`ttlMs`/`cacheScope`, and multi-round-trip requests are now first-class. Microsoft's own
App Service blog covers the scaling consequence. The date is worth getting right: an early
draft of this said August.

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

---

## Design rules these assets follow

From the research in `VISUAL_RESEARCH_AND_DRAFTS.md` — the load-bearing ones:

- **Covers carry typography, not charts.** Axis labels are the first thing to become
  illegible at feed-thumbnail size (Kim et al., IEEE TVCG 2023), so the hero number goes on
  the cover and the actual chart waits for the slide after someone taps in.
- **Light background for every small-text slide.** Light-on-dark degrades faster as text
  shrinks; dark is reserved for slides where the type is huge (covers, the one pivot slide).
- **Before/after = 2 bars, value printed on the bar, no axis.** Nothing to parse. The
  pair is a neutral baseline against the theme accent rather than red-versus-green, so it
  still reads for the ~8% of men with red-green colour deficiency; hue *and* lightness both
  carry the difference.
- **X-of-N = filled/unfilled dot grid**, which removes the axis question entirely — a tool
  for the toolbox, not currently used in any active post since the one deck that used it
  (a personal test score) was retired for putting Sid's own competence on display. Fine to
  reuse for a legitimate non-personal X-of-N stat later.
- **Page counter on every slide from 1/7** — goal-gradient effect (Kivetz, Urminsky & Zheng
  2006); perceived proximity to a finish line increases persistence.
- **Exactly one mid-thought pivot per deck** (Deck B slide 5), never per slide — the
  research explicitly warns that per-slide cliffhangers read as AI slop.
- All text checked against WCAG AA contrast as a floor, not a target.

**What the research could not tell us:** how many slides actually get swiped versus
abandoned. No credible public data on per-slide carousel drop-off exists — every percentage
circulating in this niche traces to unsourced marketing blogs. So 7 slides is a
narrative-structure choice, not an optimum.

## Rebuilding or editing

```bash
python "linkedin/builders/build_assets.py"
```

Edit the text in that file and re-run; it regenerates every PNG, both PDFs, and the GIF.
`linkedin/builders/decks.html` is an SVG version of the same layouts, openable in a browser
if you'd rather nudge things visually.
