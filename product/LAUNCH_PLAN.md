# Launch Plan — Interview Launchpad ($19 / ₹999)

**Built:** 2026-08-25 · **Revised:** 2026-08-27 after go-to-market research · **Horizon:** 16 weeks · **Your time cost:** ~3 h/week

> **This plan was revised.** The first version priced at $9 and made Instagram the primary channel. A 17-agent research pass ([RESEARCH_PLAYBOOK.md](RESEARCH_PLAYBOOK.md)) found better evidence against both, plus a positioning problem: "a plan sized to the hours you actually have" is exactly what **Grind 75** does — free, by the author of Blind 75, off a repo with 130k+ stars. Read that document; it is the reasoning behind everything below.

---

## 0. Read this before anything else

### The honest revenue math

At **$19** through Gumroad (10% + $0.50) you net **≈ $16.60 per sale**.

| Sales/month | Net/month | What that requires |
|---|---|---|
| 10 | ~$166 | A small warm audience — achievable by month 3 |
| 36 | ~$600 (₹50k) | A working content engine, sustained |
| 150 | ~$2,490 | A real audience. Rare inside 12 months. |

**Why not $9.** The flat $0.50 alone is 5.6% of a $9 sale — all-in **15.6%**, versus ~13% at $19. Digital chargebacks run ~1.8% with $15–30 dispute fees, so **one dispute wipes out three $9 sales**. And the finding that settled it: across the research, *no indie seller in interview prep at the $5–30 band could be found with any reported sales at all*, while every verifiable success sits at $35+. The $5–30 careers band is where templates and PDFs go to die, and $9 tells the buyer which category you are in.

**Realistic expectation — this is the number that matters:** the research puts **~85–90% odds of earning under $100/month for the first three months**, reasoned from Gumroad's own July 2025 distribution (of 37,006 creators who earned anything, 8,507 cleared $100 that month). **Month 1 expected value is zero sales.** That is not pessimism and it is not failure — it is the base rate. Most people quit in month 2, which is exactly why month 3 works for those who don't.

**The ceiling problem, stated honestly:** both zero-to-audience successes in this niche published under their own name for **1–3 years** before the paid product landed. Nothing compresses that. So take near-term money from your calendar (a paid session) and let the file compound slowly behind it. Ladder in §5.

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

You work at Johnson Controls. **Check your employment contract for outside-business / moonlighting clauses before you take money.** Many Indian tech contracts restrict paid outside work, some require written disclosure. Also, selling digital goods in India has GST and income-tax implications once you cross thresholds — talk to a CA, not to me. None of this stops you; all of it is cheaper to handle now than after 200 sales.

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
- [ ] Product: `Interview Launchpad`, price **$19 / ₹999**, deliver the ZIP from `dist/`.
- [ ] Turn on "ask for email" and Gumroad's own analytics.
- [ ] **Buy your own product once** at full price. Check the receipt, the download, the file opening on a clean machine. A broken download is the most expensive bug you can ship.

### Legal (10 minutes, in `legal/`)
- [ ] Read `DISCLAIMER.md` — it says no job is guaranteed. Keep it that way; it is both honest and what protects you.
- [ ] Put the refund policy on the Gumroad page itself, not buried in the file.

### Positioning — fix this before writing any content
- [ ] **Delete "sized to the hours you actually have" from the hero.** Grind 75 does exactly that, free, and better. Using that framing invites the comparison and loses it.
- [ ] **Lead with the cut list instead:** *"It names the two things you have to abandon."* Nothing free does this, because nothing free is willing to tell you what you cannot have.
- [ ] **Name Grind 75 on your own page** and say it is free and better than you at DSA scheduling. Honesty is cheaper than being caught, and it converts the comparison into a credibility signal.
- [ ] Supporting bullets: runs locally, nothing uploaded, works offline · one payment, no subscription, no account · a named engineer publishing real scores.

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
- **Price ladder, honoured as a real deadline:** *"$19 for the first 100 buyers, then $29."* Not an experiment — you will learn nothing about elasticity at your traffic, so treat it as a commitment and keep it.
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

### The product ladder

| Tier | Price | What it is | Why it works |
|---|---|---|---|
| Free | $0 | The 20-question diagnostic as a carousel + a sample week | Costs nothing, proves competence, builds the list |
| **Core** | **$19 / ₹999** | Interview Launchpad — the app | Out of the PDF band, fees drop to ~13% |
| **Session** | **₹999–1,499 / $19–29** | 45-min diagnostic debrief, 2 slots/week, recorded | The only thing on your shelf a free tool cannot clone |

**Sell ONE thing at launch.** With zero social proof, a three-column pricing grid adds abandonment rather than revenue. Mention the session in the post-purchase email, not on the sales page.

**On the session price:** the earlier plan said $99. That is wrong for your signalling at 1 YOE — Topmate comparables for mock-interview-plus-resume-review sit around ₹999. Price it at your level and say so plainly on the page: *"I am one year in and mid-transition. If you want advice from a staff engineer, book one of them instead."* That sentence is a feature, not a weakness — and the scarcity is honest, because two slots a week is genuinely your calendar.

**The arithmetic worth noticing:** one session out-earns a plausible *month* of app sales in your first quarter. If you need revenue this quarter, sell sessions. If you want a bestseller, keep publishing under your own name and stop measuring the app monthly.

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
- [ ] Create the product at **$19 / ₹999**, upload the ZIP, buy it yourself at full price

Nothing goes public until the 9-post bank exists and the contract is read.
