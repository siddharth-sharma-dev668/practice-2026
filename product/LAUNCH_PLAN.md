# Launch Plan — Interview Launchpad (₹4,999 / $59)

**Built:** 2026-08-25 · **Revised:** 2026-08-28 — research pass, then repriced to ₹4,999 as a continuous system · **Horizon:** 16 weeks · **Your time cost:** ~3 h/week

> **Revision history matters here, so it is recorded.** v1 was $9 with Instagram primary. The [research pass](RESEARCH_PLAYBOOK.md) moved it to $19 with LinkedIn primary and found a positioning problem — "a plan sized to the hours you actually have" is exactly what **Grind 75** does, free, by the author of Blind 75. v3 (this one) repriced to **₹4,999** and turned the product from a file into a **continuous system**, because those two changes only work together.

---

## 0. Read this before anything else

### Why ₹4,999 and not ₹999

The research pushed the price up and stopped at $19. Going to ₹4,999 (~$59) goes further, and the evidence supports the direction: **no indie seller in this niche at $5–30 could be found with any reported sales, while every verifiable success sits at $35+.** ₹4,999 is inside the band where things actually sell.

**But price and product have to move together.** ₹4,999 for a static HTML file would generate refunds and bad word of mouth — at that price an Indian 0–3 YOE engineer is spending a serious fraction of a month's take-home and comparing you against courses with video and mentorship. So the product is no longer a file. It is:

| What's included | Why it justifies the price |
|---|---|
| The app — diagnostic, adaptive plan, cut list, progress | The core tool |
| **One live 45-min diagnostic debrief** (recorded, redeem within 90 days) | The human hour is the anchor. No free tool can clone it, and it is the only part that cannot be pirated |
| **12 months of question-pack + topic updates**, emailed | Turns one purchase into ongoing value — and gives you a reason to contact buyers all year |
| **Quarterly re-diagnostic pack** — retake, see the delta | The research's key structural fix: *a file has no second contact* |

### The honest revenue math

At **₹4,999** through Razorpay (2% + GST on the fee) you net **≈ ₹4,880**. At **$59** through Gumroad (10% + $0.50) you net **≈ $52.60** — a 10.8% fee ratio, the best of any price you have considered.

| Sales/month | Net/month | Sanity check |
|---|---|---|
| 3 | ~₹14,600 | Plausible by month 3 with real proof |
| **11** | **~₹53,700** | Your ₹50k target — needs 11 buyers, not 77 |
| 20 | ~₹97,600 | Requires a genuine audience |

That is the whole argument for the higher price: **11 sales a month instead of 77.** Eleven conversations is a thing a person with 3 h/week can actually have. Seventy-seven purchases from cold traffic is not.

### The three things that get harder at ₹4,999 — do not skip these

1. **It is no longer an impulse buy.** Nobody spends ₹5,000 from a cold link. Expect a longer cycle: they read something of yours, they follow you, *then* they buy — often after a question in your DMs. This makes the free diagnostic and your named credibility load-bearing, not optional.
2. **Refunds hurt more and expectations are higher.** One refund is ₹4,999, not ₹800. The defence is honesty on the sales page: state exactly what it is, name Grind 75, and never imply a job outcome.
3. **Your calendar is now the ceiling.** Two sessions a week is ~8/month. Past roughly 10 sales a month you must either raise the price again, make the session an optional paid add-on instead of included, or stop selling. That is a good problem — but decide *before* you have a queue of unhappy buyers waiting on a call.

**Realistic expectation, unchanged:** **~85–90% odds of under $100/month for the first three months**, and **month 1 expected value is zero sales.** A higher price does not fix the cold start; it only means fewer sales are needed once trust exists. Both verifiable successes in this niche published under their own name for **1–3 years** before the product landed.

### Your real constraint: you have 30–60 min/day, total

You are already spending it on your own interview prep. A second job does not fit, and pretending it does is how both fail.

**So this plan is built on one rule: your study log IS your content.**

Every week you already: study 2–3 topics, solve DSA problems, build a capstone step, take a quiz, and write a STAR story. That is not "content adjacent" — it *is* the content, and it is the content nobody else can copy, because it is happening to you in real time. Post what you did. The product sells itself in the caption.

Practically: **~3 h/week**, and about half of it is repackaging work you already did.

| When | Time | What |
|---|---|---|
| Sunday | 90 min | Batch the week: turn your study log into 3 posts + 1 reel script, schedule them all |
| Wednesday | 20 min | Reply to every comment and DM (this is where sales actually happen) |
| Saturday | 45 min | Check numbers, note what worked, fix one thing |
| Ad hoc | ~15 min | Answer buyer emails |

If a week collapses, drop the posts, not your prep. The prep is the asset; the content is a by-product of the asset.

### One thing to settle before your first sale

You are salaried. **Check your employment contract for outside-business / moonlighting clauses before you take money.** Many Indian tech contracts restrict paid outside work, some require written disclosure. Also, selling digital goods in India has GST and income-tax implications once you cross thresholds — talk to a CA, not to me. None of this stops you; all of it is cheaper to handle now than after 200 sales.

---

## 1. Weeks 1–2 — Pre-launch (nothing is public yet)

**Goal: a product someone can pay for, and 9 posts in the bank.** Do not post anything before you have 9 ready — launching with an empty queue is how accounts die in week 3.

### Product
- [ ] Open `app/index.html` on your personal laptop, run the whole flow yourself as if you were a buyer. Every step.
- [ ] Do it again on your phone. Most social traffic is mobile — if it is awkward on a phone, fix that first.
- [ ] **Open Grind 75 and generate the 5 h/week × 16 weeks plan yourself. Screenshot it.** You need to know exactly what your free competitor outputs before you write another line of copy. This is 15 minutes and it is not optional.
- [ ] Give it to **3 real friends** who are job-hunting. Watch them use it without helping. Note every place they hesitate.
- [ ] Fix only what they actually tripped over. Ignore your own aesthetic opinions for now.

### Payment + delivery
- [ ] Set up **exactly ONE payment rail**, chosen by where your first ten conversations came from. INR-first → **Razorpay** (2% + GST on the fee, materially cheaper than any foreign merchant-of-record). USD-first → **Gumroad** (simplest, handles global tax as merchant of record). Do not build a dual-rail geo-detected checkout before you have a single buyer.
- [ ] Product: `Interview Launchpad`, price **₹4,999 / $59**, deliver the ZIP from `dist/`.
- [ ] Turn on "ask for email" and Gumroad's own analytics.
- [ ] **Buy your own product once** at full price. Check the receipt, the download, the file opening on a clean machine. A broken download is the most expensive bug you can ship.

### Legal (10 minutes, in `legal/`)
- [ ] Read `DISCLAIMER.md` — it says no job is guaranteed. Keep it that way; it is both honest and what protects you.
- [ ] Put the refund policy on the Gumroad page itself, not buried in the file.

### Positioning — fix this before writing any content

**The lead is the AI era. This is your sharpest and most timely angle, and it is true.**

Interviews changed faster than prep material did. Assistance is now detected, take-homes come with a defence round, and trivia lost ground to "explain your reasoning while you work." Which produces the paradox that sells this product:

> **Everyone now prepares with AI. That is exactly why preparation stopped working.**
> You end up able to *describe* a solution and unable to *produce* one, watched, in fifteen minutes. Interviews test the second thing. Only the second thing.

You have lived this and should say so: you wrote a nine-line function, never ran it, and it failed on every input from two one-character slips. The algorithm was right; the code did not work. In a live round that scores zero — and you test software for a living.

- [ ] **Hero line:** *"Interviews stopped rewarding people who can describe the answer. This gets you fluent enough to produce it — unassisted, watched, on the clock."*
- [ ] **Second line, the cut list:** *"And it names the two things you have to abandon, because your hours are real."*
- [ ] **Delete "sized to the hours you actually have" as the lead.** Grind 75 does exactly that, free, and better. It stays as a supporting bullet, never the headline.
- [ ] **Name Grind 75 on your own page** — free, and better at DSA scheduling. Honesty is cheaper than being caught and converts the comparison into credibility.
- [ ] Supporting bullets: a diagnostic that is closed-book by design · runs locally, nothing uploaded, works offline (no AI in the loop — that is the point) · a live hour with a named engineer · 12 months of updates.

**Why this angle beats the others:** it is timely, it is verifiable, almost nobody else is selling it, and it makes the product's constraints into features — closed-book diagnostic, no AI assistance on exercises, works offline. The whole thing is built for an era where you have to actually know it.

### Content bank — 9 posts
Formats and captions are in `CONTENT_CALENDAR.md`.
- [ ] 3 × "interview question autopsy" (use the question bank — you have 49)
- [ ] 3 × "hard truth about prep" — but frame these around **the cut**, not around hours
- [ ] 2 × "here is what I am building and why" (your own story, no pitch)
- [ ] 1 × screen recording of the plan generating, ending on the cut list

### Account setup — LinkedIn first
- [ ] **LinkedIn is now your primary channel.** Post from your personal profile, not a company page. Headline: what you do for whom, not adjectives — e.g. *"Software engineer, 1 YOE. Documenting a test-engineering → backend/AI transition in public: real scores, real misses."*
- [ ] **Instagram: same handle, same assets.** It stays a real channel, but it runs on the LinkedIn image rather than its own Reels pipeline — that is what keeps it inside the time budget. Bio: one line + link.
- [ ] **Reddit: create the account now and start using it as a human.** No links for eight weeks. Account age and comment history are the entry ticket.
- [ ] **YouTube: claim the handle, post nothing until month 4.** Highest production cost per unit of output and the slowest feedback loop of anything available to you.

**Do not launch yet.**

---

## 2. Weeks 3–6 — Month 1: audience before offer

**Goal: 20 real conversations and 20 email addresses. Revenue target: $0.** Yes, zero. You are buying evidence that people want this before you ask anyone for money.

**The weekly rhythm (~80 min of posting, batched Sunday):**
- **LinkedIn, 1 document post/week (45 min).** A single page exported from your own diagnostic output, or one week of your own plan. From your personal profile. Product link in the first comment, not the body.
- **Instagram, same asset (15 min).** Cross-post the LinkedIn image. This is near-free *because* it shares the asset — the moment you start producing Instagram-only Reels, the budget breaks.
- **Reddit, 20 min/week.** Answer one question properly in r/developersIndia. **No links, for eight weeks.** Contribution first, always — and read the sidebar rules yourself, because Reddit blocks automated fetching and nobody can verify them for you.
- **Reply to every comment and DM with a real sentence.** At your size this converts far better than posting, and it is the first thing that gets skipped.

**Validate the buyer, cheaply.** Post one price question publicly and DM the first ten people who engage. Ten real answers beat every benchmark in the research — because there is no credible conversion benchmark for a sub-$30 digital product sold from a cold account. That gap is real; the research looked for it and could not find it.

**Know who you are selling to.** The documented failure mode in this category is selling to peers. One post-mortem: 130k+ Reddit views produced 55 store visits and single-digit sales, diagnosed by the author as *"they're my peers, not my buyers."* Your buyer is a 0–3 YOE engineer at a service company, or a final-year student, who has never heard of Grind 75. Not a developer who could build this in a weekend.

**Checkpoint (end of week 6):** are people asking about it unprompted? If yes → launch. If no → your **audience** is wrong before your copy is. Change who you are talking to, not the price.

---

## 3. Weeks 7–10 — Month 2: launch

**Goal: first 10–25 sales. Revenue: ~$160–400.**

- **Week 7 — the launch post.** Not "buy my thing." Tell the story: *"I failed a Python question I should have known. Here is what I built so it doesn't happen again."* Then the link. Story-first outsells feature-first at this size.
- **Price ladder, honoured as a real deadline:** *"₹4,999 for the first 50 buyers, then ₹6,999."* Not an experiment — you will learn nothing about elasticity at your traffic, so treat it as a commitment and keep it.
- **Get 5–8 real, named reviews via a disclosed beta.** Give free copies to real job-seekers, get written permission to quote them by name and role, and label the block *"Beta testers — received a free copy in exchange for an honest review."* **Never write, edit, or paraphrase a testimonial:** the FTC's consumer-reviews rule (effective 21 Oct 2024) bans fake and incentivised-positive reviews, and the US is your largest potential market. Free-for-honest-review with disclosure is the compliant version.
- **Start the email list properly.** One short email a week: one useful thing, no pitch. It is the only audience you own.
- **Then stop touching the page.** Impose a rule: no changes until 300 unique visitors have landed. You cannot A/B test anything — a split test needs roughly 10,000 visitors *per variant* to resolve effects this size. Every hour after launch goes to traffic, not to tweaking.

**If you get 0 sales in 2 weeks:** it is almost never the price. It is that nobody understands what they get in the first three seconds, or that you are talking to the wrong people. Check the audience first, the hero line second.

**Week 8 — run the gate.** If impressions-to-link-clicks stays under **0.5% for four consecutive weeks**, the audience is wrong. Change *who you are talking to* — not the price, not the copy. This gate exists because the LinkedIn recommendation is a bet, and you should find out in eight weeks rather than eight months.

---

## 4. Weeks 11–14 — Month 3: find what works and repeat it

**Goal: 25–60 total sales. Revenue: ~$400–1,000.** Adjust down without drama if month 2 came in low — the base rate says most people are under $100/month here.

- **Read the analytics** (`SALES_PLAYBOOK.md` §4). Find your single best post by **saves**, not likes. Make four more like it. Most accounts have exactly one format that works; the job is to notice it and stop being creative.
- **List the session on Topmate**, 2 slots/week. This is where near-term revenue actually comes from — one session out-earns a plausible month of app sales right now.
- **Add real social proof:** the named beta reviews, your own before/after diagnostic scores. Never a fabricated buyer count.
- **Book one paid CA consult (~₹1,500–3,000). Two questions only:** how to characterise this income for filing, and whether a foreign platform's commission triggers a reverse-charge GST registration for an otherwise-unregistered individual. Two published CA opinions directly contradict each other on the second and no CBIC circular settles it. Do not resolve this from blog posts — the downside is permanent monthly compliance.
- **If a foreign payout is coming, email your bank's trade-forex desk (20 min).** From 1 Oct 2026, FEMA (Export and Import of Goods and Services) Regulations 2026 replaces SOFTEX with a monthly consolidated EDF. Ask for their process for a resident individual under ₹10 lakh/year, in writing, *before* the first payout lands.
- **Fix the product from real feedback.** Ship one improvement, then post about shipping it — visible improvement is itself marketing.

---

## 5. Weeks 15–16 — Month 4: make it a system

**Goal: predictable, and no longer dependent on you posting daily.**

### The offer — one SKU, deliberately

| Tier | Price | What it is |
|---|---|---|
| Free | ₹0 | The 20-question diagnostic as a carousel + one sample week. Your lead magnet, pinned. |
| **Interview Launchpad** | **₹4,999 / $59** | The app + one live 45-min debrief + 12 months of updates + quarterly re-diagnostics |
| Extra sessions | ₹1,499 each | For buyers who want another after the included one |

**One SKU on the page.** With zero social proof, a pricing grid adds abandonment rather than revenue. The extra session is mentioned only in the post-purchase email.

**Say your level out loud on the sales page:** *"I am one year in and mid-transition. You are buying a tool and an hour with someone one step ahead of you, not advice from a staff engineer. If you want that, book one of them instead."* That sentence prevents the mismatch that causes refunds, and at ₹4,999 preventing one refund is worth more than a marginal sale.

**Honest scarcity:** two session slots a week, because that is genuinely your calendar. Do not manufacture urgency beyond it — a scarcity claim on an infinitely copyable file is self-evidently false to an audience already scanning for scams.

### Delivering the "12 months of updates" without infrastructure

This is what makes ₹4,999 defensible, and it needs no server, no login, and no subscription billing:

- **Monthly:** email the updated `index.html` with new question packs. The footer shows a version stamp (`v2026.08.28 · 56 questions`) so buyers can see at a glance that what they received is newer.
- **Quarterly:** email a re-diagnostic pack. They retake, compare to their first score, and see the delta — *"System design 18 → 47."* That is a second contact and a far better thing to share than a plan.
- **Bump `VERSION` and `BANK_COUNT` in the app** each time. Two constants at the top of the file.
- **Budget:** roughly 60 minutes a month. Write the questions from what you are already studying that month — the same dual-purpose trick that makes the content nearly free.

If you ever stop shipping updates, **say so and stop charging for them.** A promise of 12 months that quietly becomes three is the fastest way to earn the refund requests this price makes expensive.

### Systematise
- [ ] A 30-post evergreen bank you can re-run when a week collapses
- [ ] Templates for the 3 formats that actually worked, so making a post takes 15 minutes not 60
- [ ] One weekly metrics check (10 min, `SALES_PLAYBOOK.md` §4)
- [ ] Decide honestly: is this worth 3 h/week? If month 4 nets under $100 and your prep is slipping, **pause the business and keep the prep.** The interview job is worth ₹10–25L/year. Do not trade a career for a side income of ₹5,000/month.

---

## 6. Guardrails — the things that actually kill this

1. **Do not let it eat your prep.** Your interview outcome is worth 20× this business in year one. If they conflict, prep wins. Every time.
2. **Do not promise jobs.** "Get placed in 90 days" is a lie, it attracts refund requests and angry DMs, and it is what every scam account in this niche says. Your credibility is your only real moat.
3. **Do not buy followers or engagement.** It poisons your reach permanently and converts at zero.
4. **Do not rebuild the product for months before selling.** Ship at "good enough for a friend to use," then improve from real feedback.
5. **Do not name or hint at your employer.** Not by name, not by size, not by industry, not inside an "interview experience" post, and never real questions from an internal loop. Describe yourself as an engineer with one year of experience and stop there. The earlier draft of this plan said "a Fortune 500" was acceptable — the research is stricter and it is right: in a small market, size plus location plus role identifies a company.
6. **Do not ignore the first 10 buyers.** They will tell you exactly what to build and become your named testimonials if you treat them well.
7. **Read your own employment contract before publishing anything with your name and a price on it.** Look for "exclusive", "conflict of interest", "whole time", "prior written consent", "outside employment". There is no central Indian law banning a private-sector side product — your exposure is *contractual*. If any of those clauses appear, the next call is an employment lawyer, not HR. And do not self-report before reading: if no such clause exists, disclosure manufactures an approval decision that never needed to exist.
8. **Hard hardware separation.** Personal laptop, personal network, personal email, personal GitHub/payment accounts. The product should not exist on the work machine at all. Copyright Act s.17(c) makes the employer first owner of work made in the course of employment, and standard Indian IT contracts widen that with forward-assignment clauses — hours and hardware are what you actually control.

---

## 7. Week-one checklist (start here tomorrow)

Roughly 170 minutes, in this order.

- [ ] **Read your employment contract and handbook (30 min).** This is a gate, not a task. Do it before anything with your name on it goes public.
- [ ] **Hardware separation (20 min).** Move `product/` to the personal laptop. Personal network, personal accounts, nothing on the work machine.
- [ ] **Open Grind 75, generate the 5 h/week × 16 week plan, screenshot it (15 min).** Know your free competitor's output before writing copy.
- [ ] **Rewrite the hero + three bullets (45 min):** the cut list first, then local/no-upload, then one payment no subscription. Add the Grind 75 comparison row.
- [ ] **Read the r/developersIndia sidebar rules yourself (10 min).** Non-delegable — Reddit blocks automated fetching, so no tool can verify these for you. Then answer one question in-sub, no links (20 min).
- [ ] **Post the price question; start the ten DMs (30 min).**
- [ ] Run the product start to finish on your laptop, then on your phone
- [ ] Send it to 3 job-hunting friends; watch, don't help
- [ ] Create the product at **₹4,999 / $59**, upload the ZIP, buy it yourself at full price

Nothing goes public until the 9-post bank exists and the contract is read.
