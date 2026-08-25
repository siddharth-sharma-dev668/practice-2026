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

An interview prep planner that reads your resume locally, runs a role-matched diagnostic, and generates a braided week-by-week plan sized to the hours you actually have — then tells you honestly what those hours could not fit. Runs entirely in the browser; the resume never leaves the device. $9, one file, no subscription.

## Why anyone buys it

Three things nothing else in this market does:

1. **It respects the hours you actually have.** Every free roadmap assumes 15 h/week. Most people have five, fall behind by week 3, and quit believing they failed. This one plans for five and *shows you what it dropped*.
2. **It adapts twice** — the diagnostic finds your real gaps, and your resume compresses what you can already prove. You get extra hours on your weak sections and a quick verify on your strong ones.
3. **The resume never leaves the device.** No server, no account, works with Wi-Fi off. In a category full of resume-upload tools with vague privacy policies, this is genuinely differentiated — and it is verifiable in ten seconds.

## Before your first sale

- **Check your JCI employment contract for outside-business / moonlighting clauses.** Many Indian tech contracts restrict paid outside work; some require written disclosure. Handle it before money changes hands.
- **Selling digital goods in India has GST and income-tax implications** past certain thresholds. Talk to a CA.
- **Do all commercial activity from your personal laptop and personal accounts.** Never from the work machine or work network.
- **Never reference JCI, its projects, tooling or screenshots** in any post, ever. "A Fortune 500" is the most you say.

## The one rule that matters

Your own interview prep is worth **20× this business** in year one — a backend/AI role is ₹10–25L/year; this is a few hundred dollars a month at best. The plan is built so your study log *is* your content, which makes the business nearly free in time. **The moment it starts stealing prep hours, it is costing you more than it earns.** Prep wins. Every time.
