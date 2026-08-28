# Interview Launchpad — your product workspace

Everything needed to sell this. Built 2026-08-25.

**Move this whole `product/` folder to your personal laptop before doing anything commercial with it.** See [work-laptop rules](#before-your-first-sale).

---

## What is here

| Path | What it is | Who reads it |
|---|---|---|
| `app/index.html` | **The product.** Single self-contained file, no dependencies, works offline. | Buyers |
| `dist/interview-launchpad.zip` | **What buyers download.** Upload this to Gumroad. | Buyers |
| `dist/README.md` | Buyer-facing quickstart (goes in the zip) | Buyers |
| `LAUNCH_PLAN.md` | **Start here.** 16-week plan, honest revenue maths, week-one checklist | You |
| `CONTENT_CALENDAR.md` | 12 weeks of posts with hooks + 6 copy-paste captions | You |
| `SALES_PLAYBOOK.md` | Funnel maths, what to track weekly, the fix-next decision tree | You |
| `marketing/studio.html` | 9 graphics — open it, click to export PNG or SVG | You |
| `legal/` | Licence, disclaimer, refund policy | Both |

## Do this first (30 minutes)

1. Open `app/index.html` and go through the entire flow as a buyer would. Then do it on your phone.
2. Open `marketing/studio.html`, export the PNGs you want.
3. Read `LAUNCH_PLAN.md` §7 — the week-one checklist.
4. Replace `<your-email@example.com>` in `dist/README.md`, `legal/LICENSE.txt`, `legal/DISCLAIMER.md` and `legal/REFUND_POLICY.md` with a real address.
5. Replace `@yourhandle` in `marketing/studio.html` with your actual handle.

## Rebuilding the zip after you edit the app

From this folder:

```bash
powershell -Command "Compress-Archive -Path app/index.html,dist/README.md,legal/LICENSE.txt,legal/DISCLAIMER.md -DestinationPath dist/interview-launchpad.zip -Force"
```

Then re-upload to Gumroad and **buy your own product once** to confirm the download works.

## The product in one paragraph

Interview prep built for an era where assistance is detected and interviews test what you can produce unassisted. It scores you closed-book, generates a plan weighted to your real gaps, **names the topics your hours cannot fit**, and drills the things nobody else tests — unassisted fluency, narrating trade-offs, defending a take-home. Runs entirely in the browser; the resume never leaves the device; no AI inside it, deliberately. **₹4,999 / $59** — app + one live 45-min debrief + 12 months of updates + quarterly re-diagnostics.

## Why anyone buys it

**Lead with the AI era.** It is timely, it is true, almost nobody else is selling it, and it turns the product's constraints into features:

> **Everyone prepares with AI now. That is exactly why preparation stopped working.** You end up able to *describe* a solution and unable to *produce* one — watched, unassisted, in fifteen minutes. Interviews test the second thing. Only the second thing.

1. **It trains for the round as it now exists.** Closed-book diagnostic, the verify loop in everyone's first three weeks, an AI-Era section scoring unassisted fluency, narration, live debugging and take-home defence. No AI in the app — turn the Wi-Fi off and it works identically.
2. **It tells you what to abandon.** Nothing free does this, because nothing free will tell someone what they cannot have.
3. **The resume never leaves the device.** No server, no account, verifiable in ten seconds — differentiated in a category full of resume-upload tools with vague privacy policies.
4. **A live hour with a named engineer publishing real scores.** The only part that cannot be cloned or pirated, and what makes ₹4,999 defensible.

**Second angle only:** *"sized to the hours you have."* Never the headline — [Grind 75](https://www.techinterviewhandbook.org/grind75) does that free, by the author of Blind 75. Name it on your own page as free and better at DSA scheduling.

**Read [RESEARCH_PLAYBOOK.md](RESEARCH_PLAYBOOK.md) before executing any of this** — it is the evidence behind the channel choice and positioning, including where the evidence was weak and which claims are bets.

## Before your first sale

- **Read your employment contract yourself, before any money changes hands.** Look for "exclusive", "conflict of interest", "whole time", "prior written consent", "outside employment". No Indian law bans a private-sector side product — your exposure is *contractual*. If any of those clauses appear, the next call is an employment lawyer. **Do not self-report to HR before reading:** if no clause exists, disclosure manufactures an approval decision that never needed to exist.
- **GST: do not register voluntarily.** You are exempt below ₹20 lakh aggregate turnover including exports (notifications 10/2017-IT and 65/2017-CT). Registering converts zero compliance into permanent monthly filings. The one genuinely open question — whether a foreign platform's commission triggers reverse-charge registration — needs a paid CA consult, because published CA opinions contradict each other and no CBIC circular settles it.
- **Do all commercial activity from your personal laptop, network and accounts.** Copyright Act s.17(c) makes an employer first owner of work made in the course of employment, and standard Indian IT contracts widen that with forward-assignment clauses. Hours and hardware are what you actually control.
- **Never reference your employer at all** — not by name, not by size, not by industry, not inside an "interview experience" post, and never real questions from an internal loop. "An engineer with one year of experience" is the whole of it. ("A Fortune 500" was in an earlier draft of this file; the research is stricter and right — size plus location plus role identifies a company.)

## The one rule that matters

Your own interview prep is worth **20× this business** in year one — a backend/AI role is ₹10–25L/year; this is a few hundred dollars a month at best. The plan is built so your study log *is* your content, which makes the business nearly free in time. **The moment it starts stealing prep hours, it is costing you more than it earns.** Prep wins. Every time.
