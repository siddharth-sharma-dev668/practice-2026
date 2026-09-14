# Interview Launchpad sales website — design

**Status:** approved in chat 2026-09-14 (payment approach, hosting, and post-payment flow each confirmed via explicit question; final design accepted with "no this looks good let up the website").
**Repo:** new `website/` folder in `siddharth-sharma-dev668/lauchpad` (private repo, remote already configured locally as `launchpad`). Pushed via the throwaway-worktree method (`git worktree add <tmp> -b <branch> launchpad/main`), never a force-push of that repo's `main` — it holds files (`dist/*.png`, `INSTAGRAM_PLAN.md`) this workspace doesn't have.
**Host:** Vercel free tier, connected to the `lauchpad` GitHub repo with project root set to `website/`. Not GitHub Pages — GitHub Pages can't run the serverless functions the payment flow needs (confirmed with Sid; he chose Vercel over dropping to a static-only Payment Button).

## 1. Problem

Sid's product (`product/app/index.html`, sold via Gumroad today) has no dedicated sales page with its own checkout — Gumroad hosts the listing and payment. He wants a standalone site under his own `lauchpad` repo with Razorpay-native billing, so the sale, the receipt, and the delivery email are all his own instead of Gumroad's.

## 2. Goal

A single sales page that:
- Tells the existing product story (resume-match-first flow, AI-era angle, ₹4,999 pricing) using only copy that already exists in `product/README.md` / `product/dist/README.md` / `product/legal/*` — no invented testimonials, buyer counts, or metrics.
- Takes payment via Razorpay Checkout (order created and signature-verified server-side, not a client-only Payment Button).
- On verified payment, emails the buyer a download link + booking instructions automatically, and separately notifies Sid a sale happened.

## 3. Non-goals

- No database, no buyer accounts, no admin dashboard. Email is the order record — matches the existing one-person, 2-slots/week debrief model in `product/README.md`.
- No change to `product/app/index.html` itself or to Gumroad — this is an additional, independent sales channel.
- No custom domain in v1 — ships on the default `*.vercel.app` URL. Can be added later without touching the design.
- No booking-tool integration (Calendly etc.) — keeps the existing "reply to this email to book" model from `product/dist/README.md`.
- No USD/international settlement — Razorpay charges in INR only (₹4,999); "$59" appears on the page as context, not as a second checkout currency.

## 4. Architecture

```
website/
  index.html         — the sales page (markup only)
  style.css
  script.js          — client-side: collects name/email, calls /api/create-order,
                        opens Razorpay Checkout, calls /api/verify-payment on success
  api/
    create-order.js    — Vercel serverless fn (Node). Creates a Razorpay order with
                          amount hardcoded server-side (499900 paise / ₹4,999).
                          Ignores any amount sent from the client.
    verify-payment.js  — Vercel serverless fn. Verifies the Razorpay HMAC signature
                          using RAZORPAY_KEY_SECRET. On success: sends the buyer an
                          email (Brevo API) with the download link + booking
                          instructions, and sends Sid a separate notification email.
  dist/
    interview-launchpad.zip   — copied from product/dist/, the actual file the
                                 buyer-email download link points to
  legal/
    LICENSE.txt, DISCLAIMER.md, REFUND_POLICY.md   — copied from product/legal/,
    with <your-email@example.com> replaced by launchpadinterview@gmail.com
  README.md           — deploy steps for Sid: connect repo to Vercel, which env vars
                         to paste into Vercel's dashboard himself, how to test
```

### 4.1 Payment flow

1. Buyer fills name + email, clicks **Buy for ₹4,999**.
2. `script.js` → `POST /api/create-order` `{name, email}`.
3. `create-order.js` calls Razorpay Orders API with `amount: 499900, currency: "INR"` (both hardcoded, never taken from the request body) using `RAZORPAY_KEY_ID`/`RAZORPAY_KEY_SECRET` from Vercel env vars. Returns `{order_id, key_id}` (key_id is Razorpay's public key — safe client-side).
4. `script.js` opens Razorpay Checkout with that `order_id`. On success, Razorpay hands the client `{razorpay_payment_id, razorpay_order_id, razorpay_signature}`.
5. `script.js` → `POST /api/verify-payment` with those three fields plus the buyer's name/email collected in step 1.
6. `verify-payment.js` recomputes the HMAC-SHA256 of `order_id|payment_id` using `RAZORPAY_KEY_SECRET` and compares to `razorpay_signature`. Mismatch → 400, page shows an error and asks the buyer to email support instead of retrying blindly.
7. On match: calls Brevo's transactional email API twice — once to the buyer (download link to `/dist/interview-launchpad.zip` + the same booking/refund copy as `product/dist/README.md`), once to Sid at `launchpadinterview@gmail.com` (payment id, buyer name/email, timestamp) as the order record.
8. Page shows: "Payment verified — check your email for your download link and booking instructions."

### 4.2 Secrets

All read from `process.env` inside the two serverless functions only, never present in `index.html`/`script.js`:
- `RAZORPAY_KEY_ID` (also returned to the client — this half is public by design)
- `RAZORPAY_KEY_SECRET`
- `BREVO_API_KEY`
- `SENDER_EMAIL` = `launchpadinterview@gmail.com` (must be verified as a single sender in Brevo — no domain purchase needed for their free tier)
- `NOTIFY_EMAIL` = `launchpadinterview@gmail.com` (where the sale-notification copy goes; same address is fine, can be split later)

Sid enters these directly into Vercel's dashboard (Project → Settings → Environment Variables). They are never pasted into chat, a file this session writes, or a command this session runs.

### 4.3 Content sections (index.html)

In order, all copy sourced from existing docs (cited per section so nothing is invented):
1. **Hero** — "Does your resume match the job you want?" + one-line any-role-to-any-role framing (`product/README.md` §"The hook").
2. **How it works** — Match → Fix → Score yourself → Plan, the four steps (`product/README.md` §"Why anyone buys it", point 1-4).
3. **The AI-era angle** — the "everyone prepares with AI now" paragraph, verbatim framing (`product/README.md` / `product/dist/README.md`).
4. **What's included / pricing** — app + one live 45-min debrief (2 slots/week, 90-day redeem) + 12 months of updates + quarterly re-diagnostic, ₹4,999 (`product/README.md` §"Price").
5. **Buy section** — name/email form + Buy button (Razorpay Checkout trigger).
6. **Privacy note** — "resume never leaves your device", turn-off-Wi-Fi proof (`product/dist/README.md`).
7. **Refund** — the exact public-facing blockquote from `product/legal/REFUND_POLICY.md` ("14-day refund, no questions asked...").
8. **Footer** — contact (`launchpadinterview@gmail.com`), links to `legal/LICENSE.txt` / `legal/DISCLAIMER.md` / `legal/REFUND_POLICY.md`.

No section names an employer, invents a metric, or claims a buyer count/testimonial that isn't in the source docs — none exist there, so none appear here.

## 5. Error handling

- `create-order.js` Razorpay API failure → 500, client shows "Couldn't start checkout, please retry or email support."
- `verify-payment.js` signature mismatch → 400, client shows a message directing the buyer to email `launchpadinterview@gmail.com` with their payment id rather than retrying payment.
- Brevo send failure after a verified payment → logged (Vercel function logs), but the buyer still sees the success message — a payment that verified must never be reported as failed to the buyer over an email-provider hiccup. Sid checks Vercel logs if a buyer reports no email.

## 6. Testing / verification

- `node --check` on both serverless functions after writing them.
- Razorpay test-mode keys (test card numbers) used for a full manual run-through in the Browser tool: fill form → Checkout modal → test payment → verify success message → confirm both emails actually arrive (buyer + Sid) via Brevo's dashboard/logs.
- Confirm signature-mismatch path manually (send a tampered payload to `/api/verify-payment` with curl) returns 400 and does not send email.
- Manual visual pass at desktop and mobile widths (resize_window in the Browser tool) before calling it done — this is a page real buyers will land on from a phone.

## 7. Rollout

1. Build `website/` locally in this workspace's worktree area first (not yet pushed).
2. Push to `lauchpad` via the throwaway-worktree method, diff-checked against what's already on `launchpad/main`.
3. Sid connects the repo to Vercel himself (OAuth, not a password) and sets the five env vars in §4.2 in Vercel's dashboard.
4. Sid gets a test-mode Razorpay key pair from his own Razorpay dashboard and a Brevo API key + verified sender from his own Brevo signup — both browser-based, both his own accounts.
5. Full manual test pass per §6 against the live Vercel preview URL before switching Razorpay from test to live keys.
