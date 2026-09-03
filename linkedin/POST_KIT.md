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
| **2026-09-04 (next)** | Code-comprehension self-test | Document carousel, 7 slides | `assets/deck-diagnostic.pdf` |
| 2026-09-06 | MCP goes stateless | Animated GIF **or** single image | `assets/mcp-stateless.gif` |
| held / retired | Cache-aside deck (topic collision with 09-02 post) | — | `assets/deck-cache-aside.pdf` |

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

## Post 1 — Code-comprehension self-test (post today)

**Asset:** `assets/deck-diagnostic.pdf` · document title suggestion: `The 3 I missed`

**Why this one leads:** it's entirely your own measured result, so there is nothing in it
anyone can challenge you on, and it ends on an honest gap rather than a win.

```
A few large tech companies have reportedly rebuilt technical interviews around AI-assisted coding this year.

The shape people describe: a round graded on reading and debugging an existing codebase with an AI assistant available, instead of writing from a blank file — per a few interview-prep sources I've read, not something I've sat myself.

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

**Changed from the research draft:** the original named Google specifically. The research
itself flagged the per-company claims as sourced to interview-prep vendors who sell
interview practice — likely candidate anecdotes rather than confirmed process. Naming a
company you can't defend if challenged is the one avoidable risk in an otherwise
bulletproof post, so it now says "a few large tech companies" and keeps the hedge.

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
- **X-of-N = filled/unfilled dot grid** (the 22/25 slide), which removes the axis question
  entirely.
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
