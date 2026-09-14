# Launchpad Sales Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A standalone static sales page for Interview Launchpad, with Razorpay Checkout (order created + signature verified server-side) and an automatic delivery email on successful payment, deployed on Vercel from a new `website/` folder in the `lauchpad` GitHub repo.

**Architecture:** Static `index.html`/`style.css`/`script.js` for the page, plus two Vercel serverless functions (`api/create-order.js`, `api/verify-payment.js`) for the parts that must not run in the browser (amount enforcement, signature verification, secret API keys). No database — a verified payment triggers two emails (buyer + owner), which together are the order record.

**Tech Stack:** Plain HTML/CSS/JS (no framework, no build step, matches the existing product's "single file, no dependencies" ethos), Node.js Vercel serverless functions, `razorpay` npm package, Brevo transactional email REST API (called via `fetch`, no SDK needed).

**Spec:** [docs/superpowers/specs/2026-09-14-launchpad-sales-website-design.md](../specs/2026-09-14-launchpad-sales-website-design.md)

## Global Constraints

- All content copy must trace to an existing doc (`product/README.md`, `product/dist/README.md`, `product/legal/*`) — no invented testimonials, buyer counts, or metrics.
- Never mention Sid's employer anywhere on the page.
- Visual style is light/plain: no dark-gradient-and-glow look (Sid's explicit standing preference, [[linkedin-content-rotation]] memory) — white/off-white backgrounds, one flat accent color, no glassmorphism, no neon glow.
- Price is fixed server-side at ₹4,999 (499900 paise) in `api/create-order.js` — the amount must never be read from the client request.
- Secrets (`RAZORPAY_KEY_SECRET`, `BREVO_API_KEY`) are read only via `process.env` inside `api/*.js` — never in `index.html`/`script.js`, never typed into any file by the plan's executor. `RAZORPAY_KEY_ID` is safe client-side (Razorpay's public key half).
- Contact/sender address across the site and both legal copies and emails: `launchpadinterview@gmail.com`.
- No test framework exists in this repo for static HTML/JS work (matches `platform/index.html` and `product/app/index.html` precedent) — verification is `node --check` on each serverless function plus manual browser passes, not a unit-test suite.

---

## File Structure

```
website/
  index.html
  style.css
  script.js
  package.json
  api/
    create-order.js
    verify-payment.js
  dist/
    interview-launchpad.zip      (copied verbatim from product/dist/)
  legal/
    LICENSE.txt
    DISCLAIMER.md
    REFUND_POLICY.md
  README.md
```

---

### Task 1: Sales page markup (`website/index.html`)

**Files:**
- Create: `website/index.html`

**Interfaces:**
- Produces: DOM ids/classes that Task 2 (`style.css`) and Task 3 (`script.js`) depend on: `#buy-form`, `#buy-name`, `#buy-email`, `#buy-submit`, `#buy-status`, `.nav-toggle`, `#site-nav`, `[data-reveal]` (sections that fade in on scroll).
- Consumes: nothing (first task).

- [ ] **Step 1: Write `website/index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interview Launchpad — Does your resume match the job you want?</title>
<meta name="description" content="Paste your resume, type the role you want, and see the gap between them before you study a single hour. Any role to any role — ₹4,999.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="#top" class="wordmark">Interview Launchpad</a>
    <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="site-nav">
      <span></span><span></span><span></span>
    </button>
    <nav id="site-nav" class="site-nav">
      <a href="#how">How it works</a>
      <a href="#included">What you get</a>
      <a href="#faq">FAQ</a>
      <a href="#buy" class="nav-cta">Buy — ₹4,999</a>
    </nav>
  </div>
</header>

<main id="top">

  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">Any role to any role</p>
      <h1>Does your resume match the job you want?</h1>
      <p class="hero-sub">Paste your resume, type the role you're actually going for — test engineer to backend, support to developer, backend to AI, anything to anything — and see the gap between what you have and what that role needs. Before you spend a single hour studying the wrong thing.</p>
      <div class="hero-actions">
        <a href="#buy" class="btn btn-primary">See what's missing — ₹4,999</a>
        <a href="#how" class="btn btn-ghost">See how it works</a>
      </div>
    </div>
  </section>

  <section id="how" class="section" data-reveal>
    <div class="wrap">
      <h2>The order is the product</h2>
      <p class="section-lede">Four steps, in this order — not a pile of study material and a hope.</p>
      <div class="step-grid">
        <div class="step-card">
          <span class="step-num">1</span>
          <h3>Match</h3>
          <p>A score, what's already there, and what's missing. Missing a must-have is the usual reason a resume never gets read.</p>
        </div>
        <div class="step-card">
          <span class="step-num">2</span>
          <h3>Fix</h3>
          <p>The specific bullet to add for each gap, with the evidence it needs — not "add SQL to your skills."</p>
        </div>
        <div class="step-card">
          <span class="step-num">3</span>
          <h3>Score yourself</h3>
          <p>Closed-book. Your resume says what you can <em>claim</em>; the diagnostic says what you can <em>defend</em>. Both matter, and they're different.</p>
        </div>
        <div class="step-card">
          <span class="step-num">4</span>
          <h3>Then the plan</h3>
          <p>Every gap becomes a step that ends with something real to put on the resume. A rewritten bullet with nothing behind it fails the interview instead of the screen.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt" data-reveal>
    <div class="wrap wrap-narrow">
      <h2>The AI-era problem</h2>
      <blockquote class="pull-quote">
        Everyone prepares with AI now. That is exactly why preparation stopped working. You end up able to <em>describe</em> a solution and unable to <em>produce</em> one — watched, unassisted, in fifteen minutes. Interviews test the second thing. Only the second thing.
      </blockquote>
      <p>So the app is built the way the interview actually works: the diagnostic is closed-book, every plan puts a verify loop in the first three weeks, and there's an AI-era section scoring unassisted fluency, narration and live debugging. <strong>No AI runs inside this app.</strong> Turn your Wi-Fi off and it works identically — that's not a limitation, it's the point.</p>
    </div>
  </section>

  <section id="included" class="section" data-reveal>
    <div class="wrap">
      <h2>What ₹4,999 gets you</h2>
      <p class="section-lede">Not a file. A continuous system.</p>
      <div class="included-grid">
        <div class="included-item">
          <h3>The app</h3>
          <p>Diagnostic, adaptive plan, progress tracking. Yours forever — no subscription, no login.</p>
        </div>
        <div class="included-item">
          <h3>One live 45-minute debrief</h3>
          <p>Reply to your receipt to book it. Two slots a week, so book early — redeem within 90 days.</p>
        </div>
        <div class="included-item">
          <h3>12 months of updates</h3>
          <p>New question packs and topics, emailed as they ship.</p>
        </div>
        <div class="included-item">
          <h3>Quarterly re-diagnostic</h3>
          <p>A fresh pack every ~3 months. Retake it, compare with your first score, see what actually moved.</p>
        </div>
      </div>
      <p class="price-note">₹4,999 <span class="price-alt">(~$59)</span> — one-time, not a subscription.</p>
    </div>
  </section>

  <section id="buy" class="section section-alt" data-reveal>
    <div class="wrap wrap-narrow">
      <h2>Get your diagnostic</h2>
      <p class="section-lede">Fill this in, pay, and your download link + booking instructions land in your inbox.</p>
      <form id="buy-form" novalidate>
        <label for="buy-name">Name</label>
        <input type="text" id="buy-name" name="name" required autocomplete="name">
        <label for="buy-email">Email</label>
        <input type="email" id="buy-email" name="email" required autocomplete="email">
        <button type="submit" id="buy-submit" class="btn btn-primary btn-block">Buy for ₹4,999</button>
        <p id="buy-status" class="buy-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>

  <section class="section" data-reveal>
    <div class="wrap wrap-narrow">
      <h2>Your resume never leaves your device</h2>
      <p>There's no server, no account, no telemetry, and nothing is uploaded. You don't have to take that on faith: <strong>turn off your Wi-Fi and use the whole thing</strong> — it works identically. That's the proof.</p>
    </div>
  </section>

  <section id="faq" class="section section-alt" data-reveal>
    <div class="wrap wrap-narrow">
      <h2>Refunds</h2>
      <blockquote class="pull-quote pull-quote-small">
        14-day refund, no questions asked. If it's not useful, email me and I'll refund you. You keep the file — I'm not going to chase you for an HTML document.
      </blockquote>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <p>Questions or refunds: <a href="mailto:launchpadinterview@gmail.com">launchpadinterview@gmail.com</a></p>
    <p class="footer-links">
      <a href="legal/LICENSE.txt">Licence</a> ·
      <a href="legal/DISCLAIMER.md">Disclaimer</a> ·
      <a href="legal/REFUND_POLICY.md">Refund policy</a>
    </p>
    <p class="footer-copy">© 2026 Interview Launchpad</p>
  </div>
</footer>

<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script src="script.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify markup is well-formed**

Run: `node -e "require('node:fs').readFileSync('website/index.html','utf8')" && echo OK`
Expected: `OK` (this is just a sanity read; there's no HTML linter in this repo — the real check is the browser pass in Task 8).

- [ ] **Step 3: Commit**

```bash
git add website/index.html
git commit -m "Add Launchpad sales page markup"
```

---

### Task 2: Visual design (`website/style.css`)

**Files:**
- Create: `website/style.css`

**Interfaces:**
- Consumes: the ids/classes produced in Task 1.
- Produces: nothing further layers depend on (leaf file).

- [ ] **Step 1: Write `website/style.css`**

```css
:root {
  --bg: #ffffff;
  --bg-alt: #f6f5f2;
  --ink: #14181f;
  --ink-soft: #52596b;
  --accent: #3730a3;
  --accent-tint: #eef0fb;
  --border: #e4e2dd;
  --success: #15803d;
  --success-bg: #ecfdf3;
  --error: #b91c1c;
  --error-bg: #fef2f2;
  --radius: 10px;
  --wrap: 1080px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3 { font-weight: 700; line-height: 1.2; margin: 0 0 0.5em; }
h1 { font-size: clamp(2rem, 5vw, 3rem); font-weight: 800; }
h2 { font-size: clamp(1.5rem, 3.5vw, 2.1rem); }
h3 { font-size: 1.15rem; }
p { margin: 0 0 1em; color: var(--ink-soft); }
a { color: var(--accent); text-decoration: none; }
strong, em { color: var(--ink); }

.wrap { max-width: var(--wrap); margin: 0 auto; padding: 0 24px; }
.wrap-narrow { max-width: 720px; }

.btn {
  display: inline-block;
  padding: 14px 28px;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 1rem;
  border: 1px solid transparent;
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.btn-primary { background: var(--accent); color: #fff; }
.btn-primary:hover { box-shadow: 0 6px 16px rgba(55, 48, 163, 0.25); transform: translateY(-1px); }
.btn-primary:disabled { opacity: 0.6; cursor: not-allowed; transform: none; box-shadow: none; }
.btn-ghost { background: transparent; color: var(--ink); border-color: var(--border); }
.btn-ghost:hover { border-color: var(--accent); color: var(--accent); }
.btn-block { display: block; width: 100%; text-align: center; }

/* Header */
.site-header {
  position: sticky; top: 0; z-index: 20;
  background: rgba(255,255,255,0.92);
  backdrop-filter: saturate(180%) blur(6px);
  border-bottom: 1px solid var(--border);
}
.header-inner { display: flex; align-items: center; justify-content: space-between; height: 64px; }
.wordmark { font-weight: 800; font-size: 1.1rem; color: var(--ink); }
.site-nav { display: flex; align-items: center; gap: 28px; }
.site-nav a { color: var(--ink-soft); font-weight: 500; }
.site-nav a:hover { color: var(--accent); }
.nav-cta { background: var(--accent); color: #fff !important; padding: 8px 16px; border-radius: 8px; }
.nav-toggle { display: none; flex-direction: column; gap: 4px; background: none; border: none; cursor: pointer; padding: 8px; }
.nav-toggle span { width: 22px; height: 2px; background: var(--ink); display: block; }

/* Hero */
.hero { padding: 88px 0 72px; text-align: center; }
.eyebrow { color: var(--accent); font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 12px; }
.hero-sub { font-size: 1.15rem; max-width: 640px; margin: 0 auto 32px; }
.hero-actions { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }

/* Sections */
.section { padding: 72px 0; opacity: 0; transform: translateY(16px); transition: opacity 0.5s ease, transform 0.5s ease; }
.section.is-visible { opacity: 1; transform: translateY(0); }
.section-alt { background: var(--bg-alt); }
.section-lede { font-size: 1.05rem; margin-bottom: 40px; }
.section h2 { text-align: center; }
.section > .wrap > .section-lede { text-align: center; }

.step-grid, .included-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 24px;
}
.step-card, .included-item {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
}
.step-num {
  display: inline-flex; align-items: center; justify-content: center;
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--accent-tint); color: var(--accent);
  font-weight: 700; margin-bottom: 12px;
}
.included-item { background: var(--bg-alt); border-color: var(--border); }
.section-alt .included-item { background: #fff; }

.price-note { text-align: center; font-size: 1.5rem; font-weight: 700; color: var(--ink); margin-top: 40px; }
.price-alt { font-size: 1rem; font-weight: 500; color: var(--ink-soft); }

.pull-quote {
  font-size: 1.3rem; font-weight: 600; color: var(--ink);
  border-left: 3px solid var(--accent);
  padding-left: 20px; margin: 0 0 24px;
}
.pull-quote-small { font-size: 1.1rem; font-weight: 500; }

/* Buy form */
#buy-form { display: flex; flex-direction: column; gap: 14px; max-width: 420px; margin: 0 auto; }
#buy-form label { font-weight: 600; font-size: 0.9rem; }
#buy-form input {
  padding: 12px 14px; border: 1px solid var(--border); border-radius: 8px;
  font-size: 1rem; font-family: inherit;
}
#buy-form input:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.buy-status { min-height: 1.4em; font-weight: 600; text-align: center; margin: 4px 0 0; }
.buy-status.pending { color: var(--ink-soft); }
.buy-status.success { color: var(--success); }
.buy-status.error { color: var(--error); }

/* Footer */
.site-footer { border-top: 1px solid var(--border); padding: 40px 0; background: var(--bg-alt); }
.footer-inner { text-align: center; }
.footer-links { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; color: var(--ink-soft); }
.footer-copy { color: var(--ink-soft); font-size: 0.85rem; margin: 0; }

@media (max-width: 720px) {
  .nav-toggle { display: flex; }
  .site-nav {
    position: absolute; top: 64px; left: 0; right: 0;
    background: #fff; border-bottom: 1px solid var(--border);
    flex-direction: column; align-items: flex-start; gap: 0;
    padding: 8px 24px 16px; display: none;
  }
  .site-nav.is-open { display: flex; }
  .site-nav a { padding: 10px 0; width: 100%; }
  .hero { padding: 56px 0 48px; }
  .section { padding: 48px 0; }
}
```

- [ ] **Step 2: Commit**

```bash
git add website/style.css
git commit -m "Add Launchpad sales page styling"
```

---

### Task 3: Client-side behavior (`website/script.js`)

**Files:**
- Create: `website/script.js`

**Interfaces:**
- Consumes: DOM ids from Task 1 (`#buy-form`, `#buy-name`, `#buy-email`, `#buy-submit`, `#buy-status`, `#nav-toggle`, `#site-nav`, `[data-reveal]`); global `Razorpay` from the checkout.js script tag in Task 1.
- Produces: `POST /api/create-order` request shape `{name, email}`, expects response `{order_id, key_id, amount}` (Task 4 must produce exactly this). `POST /api/verify-payment` request shape `{razorpay_order_id, razorpay_payment_id, razorpay_signature, name, email}`, expects response `{verified: true}` or `{error}` (Task 5 must produce exactly this).

- [ ] **Step 1: Write `website/script.js`**

```js
(function () {
  "use strict";

  // Mobile nav toggle
  var navToggle = document.getElementById("nav-toggle");
  var siteNav = document.getElementById("site-nav");
  navToggle.addEventListener("click", function () {
    var isOpen = siteNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
  siteNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      siteNav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });

  // Scroll-reveal
  var revealTargets = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealTargets.forEach(function (el) { observer.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Buy flow
  var form = document.getElementById("buy-form");
  var submitBtn = document.getElementById("buy-submit");
  var statusEl = document.getElementById("buy-status");

  function setStatus(text, kind) {
    statusEl.textContent = text;
    statusEl.className = "buy-status" + (kind ? " " + kind : "");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = document.getElementById("buy-name").value.trim();
    var email = document.getElementById("buy-email").value.trim();
    if (!name || !email) {
      setStatus("Please fill in both fields.", "error");
      return;
    }

    submitBtn.disabled = true;
    setStatus("Starting checkout…", "pending");

    fetch("/api/create-order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, email: email }),
    })
      .then(function (res) {
        if (!res.ok) throw new Error("create-order-failed");
        return res.json();
      })
      .then(function (order) {
        var rzp = new Razorpay({
          key: order.key_id,
          order_id: order.order_id,
          amount: order.amount,
          currency: "INR",
          name: "Interview Launchpad",
          description: "App + live debrief + 12 months of updates",
          prefill: { name: name, email: email },
          theme: { color: "#3730a3" },
          handler: function (response) {
            setStatus("Verifying payment…", "pending");
            fetch("/api/verify-payment", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
                name: name,
                email: email,
              }),
            })
              .then(function (res) {
                if (!res.ok) throw new Error("verify-failed");
                return res.json();
              })
              .then(function () {
                setStatus(
                  "Payment verified — check your email for your download link and booking instructions.",
                  "success"
                );
                form.reset();
              })
              .catch(function () {
                setStatus(
                  "Payment went through but we couldn't confirm it automatically. Email launchpadinterview@gmail.com with your payment id and we'll sort it out.",
                  "error"
                );
              })
              .finally(function () {
                submitBtn.disabled = false;
              });
          },
          modal: {
            ondismiss: function () {
              setStatus("Checkout closed. No payment was made.", "");
              submitBtn.disabled = false;
            },
          },
        });
        rzp.open();
      })
      .catch(function () {
        setStatus("Couldn't start checkout — please retry or email support.", "error");
        submitBtn.disabled = false;
      });
  });
})();
```

- [ ] **Step 2: Syntax check**

Run: `node --check website/script.js`
Expected: no output (exit code 0).

- [ ] **Step 3: Commit**

```bash
git add website/script.js
git commit -m "Add Launchpad checkout client script"
```

---

### Task 4: `api/create-order.js` serverless function

**Files:**
- Create: `website/api/create-order.js`
- Create: `website/package.json`

**Interfaces:**
- Consumes: `process.env.RAZORPAY_KEY_ID`, `process.env.RAZORPAY_KEY_SECRET` (set by Sid in Vercel dashboard, not by this task).
- Produces: `POST /api/create-order` — request `{name, email}`, success response `200 {order_id, key_id, amount}`, failure `400 {error}` or `500 {error}`. This exact shape is what Task 3's `script.js` already consumes.

- [ ] **Step 1: Write `website/package.json`**

```json
{
  "name": "launchpad-website",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "razorpay": "^2.9.4"
  }
}
```

- [ ] **Step 2: Write `website/api/create-order.js`**

```js
const Razorpay = require("razorpay");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const { name, email } = req.body || {};
  if (!name || !email) {
    res.status(400).json({ error: "Name and email are required" });
    return;
  }

  const instance = new Razorpay({
    key_id: process.env.RAZORPAY_KEY_ID,
    key_secret: process.env.RAZORPAY_KEY_SECRET,
  });

  try {
    const order = await instance.orders.create({
      amount: 499900, // ₹4,999 in paise — fixed here, never taken from the client
      currency: "INR",
      receipt: "launchpad_" + Date.now(),
      notes: { name, email },
    });
    res.status(200).json({
      order_id: order.id,
      key_id: process.env.RAZORPAY_KEY_ID,
      amount: order.amount,
    });
  } catch (err) {
    console.error("create-order failed", err);
    res.status(500).json({ error: "Could not create order" });
  }
};
```

- [ ] **Step 3: Syntax check**

Run: `node --check website/api/create-order.js`
Expected: no output (exit code 0).

- [ ] **Step 4: Install dependency locally so it's available for the later local review**

Run: `cd website && npm install --no-audit --no-fund && cd ..`
Expected: `node_modules/razorpay` created, no errors. (Add `website/node_modules` to `.gitignore` before committing — see Step 5.)

- [ ] **Step 5: Ignore `node_modules` and commit**

```bash
echo "node_modules/" >> website/.gitignore
git add website/package.json website/api/create-order.js website/.gitignore
git commit -m "Add Razorpay order-creation serverless function"
```

---

### Task 5: `api/verify-payment.js` serverless function

**Files:**
- Create: `website/api/verify-payment.js`

**Interfaces:**
- Consumes: `process.env.RAZORPAY_KEY_SECRET`, `process.env.BREVO_API_KEY`, `process.env.SENDER_EMAIL`, `process.env.NOTIFY_EMAIL` (all set by Sid in Vercel). Consumes the request shape Task 3 sends: `{razorpay_order_id, razorpay_payment_id, razorpay_signature, name, email}`.
- Produces: `200 {verified: true}` on success, `400 {error}` on bad input or signature mismatch. This exact shape is what Task 3's `script.js` already consumes.

- [ ] **Step 1: Write `website/api/verify-payment.js`**

```js
const crypto = require("crypto");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const {
    razorpay_order_id,
    razorpay_payment_id,
    razorpay_signature,
    name,
    email,
  } = req.body || {};

  if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature || !name || !email) {
    res.status(400).json({ error: "Missing verification fields" });
    return;
  }

  const expected = crypto
    .createHmac("sha256", process.env.RAZORPAY_KEY_SECRET)
    .update(razorpay_order_id + "|" + razorpay_payment_id)
    .digest("hex");

  if (expected !== razorpay_signature) {
    res.status(400).json({ error: "Signature mismatch" });
    return;
  }

  const site = "https://" + req.headers.host;
  const downloadUrl = site + "/dist/interview-launchpad.zip";

  const buyerEmail = {
    sender: { email: process.env.SENDER_EMAIL, name: "Interview Launchpad" },
    to: [{ email: email, name: name }],
    subject: "Your Interview Launchpad download",
    htmlContent: buildBuyerEmailHtml(name, downloadUrl),
  };
  const ownerEmail = {
    sender: { email: process.env.SENDER_EMAIL, name: "Interview Launchpad" },
    to: [{ email: process.env.NOTIFY_EMAIL, name: "Sid" }],
    subject: "New sale: " + name,
    htmlContent:
      "<p>" + name + " (" + email + ") paid. Payment id: " + razorpay_payment_id +
      ", order id: " + razorpay_order_id + ", time: " + new Date().toISOString() + "</p>",
  };

  try {
    await Promise.all([sendBrevoEmail(buyerEmail), sendBrevoEmail(ownerEmail)]);
  } catch (err) {
    // A verified payment must never be reported as failed to the buyer over an
    // email-provider hiccup — log it, Sid checks Vercel logs if a buyer reports
    // no email arrived.
    console.error("brevo send failed", err);
  }

  res.status(200).json({ verified: true });
};

async function sendBrevoEmail(payload) {
  const resp = await fetch("https://api.brevo.com/v3/smtp/email", {
    method: "POST",
    headers: {
      "api-key": process.env.BREVO_API_KEY,
      "content-type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error("Brevo send failed: " + resp.status + " " + text);
  }
}

function buildBuyerEmailHtml(name, downloadUrl) {
  return (
    '<div style="font-family:Arial,sans-serif;line-height:1.6;color:#1a1a1a">' +
    "<h2>Thanks, " + name + " — here's your Interview Launchpad</h2>" +
    '<p><a href="' + downloadUrl + '">Download the app (zip file)</a></p>' +
    "<p>Unzip it anywhere permanent, then open <code>index.html</code> in your browser. No account, no install.</p>" +
    "<p><strong>To book your free 45-minute debrief:</strong> just reply to this email with a few times that work for you. Two slots a week, so book early — redeem within 90 days.</p>" +
    "<p>14-day refund, no questions asked — reply to this email with your payment id if it's not useful.</p>" +
    "<p>— Sid</p>" +
    "</div>"
  );
}
```

- [ ] **Step 2: Syntax check**

Run: `node --check website/api/verify-payment.js`
Expected: no output (exit code 0).

- [ ] **Step 3: Commit**

```bash
git add website/api/verify-payment.js
git commit -m "Add payment-verification and delivery-email serverless function"
```

---

### Task 6: Legal pages and downloadable product zip

**Files:**
- Create: `website/legal/LICENSE.txt` (copied from `product/legal/LICENSE.txt`, `<your-email@example.com>` → `launchpadinterview@gmail.com`)
- Create: `website/legal/DISCLAIMER.md` (copied from `product/legal/DISCLAIMER.md`, same email replacement)
- Create: `website/legal/REFUND_POLICY.md` (copied from `product/legal/REFUND_POLICY.md`, same email replacement)
- Create: `website/dist/interview-launchpad.zip` (copied verbatim from `product/dist/interview-launchpad.zip` — this is the file Task 5's `verify-payment.js` links to)

**Interfaces:**
- Consumes: `product/legal/*`, `product/dist/interview-launchpad.zip` (must already exist — confirmed present in this repo).
- Produces: the exact path `website/dist/interview-launchpad.zip` that Task 5 hardcodes into the download URL, and the exact paths `website/legal/LICENSE.txt` / `website/legal/DISCLAIMER.md` / `website/legal/REFUND_POLICY.md` that Task 1's footer links to.

- [ ] **Step 1: Copy the zip verbatim**

Run:
```bash
mkdir -p website/dist
cp product/dist/interview-launchpad.zip website/dist/interview-launchpad.zip
```
Expected: `website/dist/interview-launchpad.zip` exists and is byte-identical to the source (`cmp product/dist/interview-launchpad.zip website/dist/interview-launchpad.zip` prints nothing and exits 0).

- [ ] **Step 2: Copy and adapt the three legal files**

Run:
```bash
mkdir -p website/legal
sed 's/<your-email@example.com>/launchpadinterview@gmail.com/g' product/legal/LICENSE.txt > website/legal/LICENSE.txt
sed 's/<your-email@example.com>/launchpadinterview@gmail.com/g' product/legal/DISCLAIMER.md > website/legal/DISCLAIMER.md
sed 's/<your-email@example.com>/launchpadinterview@gmail.com/g' product/legal/REFUND_POLICY.md > website/legal/REFUND_POLICY.md
```
Expected: `grep -c example.com website/legal/*.txt website/legal/*.md` prints `0` for every file (no leftover placeholder).

- [ ] **Step 3: Commit**

```bash
git add website/dist/interview-launchpad.zip website/legal/
git commit -m "Add legal pages and downloadable product zip to the sales site"
```

---

### Task 7: Deploy instructions (`website/README.md`)

**Files:**
- Create: `website/README.md`

**Interfaces:**
- Consumes: the env var names fixed by Tasks 4–5 (`RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `BREVO_API_KEY`, `SENDER_EMAIL`, `NOTIFY_EMAIL`).
- Produces: nothing further layers depend on (this is documentation for Sid, the human operator).

- [ ] **Step 1: Write `website/README.md`**

```markdown
# Interview Launchpad — sales website

Static sales page + Razorpay checkout + auto-delivery email. Deployed on Vercel from this folder.

## One-time setup (all done in your own browser, your own accounts)

1. **Connect to Vercel:** vercel.com → New Project → Import the `lauchpad` GitHub repo → set **Root Directory** to `website` → Deploy. No password needed, it's GitHub OAuth.
2. **Razorpay:** sign in at dashboard.razorpay.com → Settings → API Keys → generate a **test mode** key pair first. Copy the Key ID and Key Secret.
3. **Brevo (email sending):** sign up at brevo.com (free tier, no domain purchase needed) → Senders → add and verify `launchpadinterview@gmail.com` as a single sender → Settings → SMTP & API → create an API key.
4. **Set environment variables** in Vercel: Project → Settings → Environment Variables. Add all five, then redeploy:

   | Name | Value |
   |---|---|
   | `RAZORPAY_KEY_ID` | from Razorpay dashboard |
   | `RAZORPAY_KEY_SECRET` | from Razorpay dashboard |
   | `BREVO_API_KEY` | from Brevo dashboard |
   | `SENDER_EMAIL` | `launchpadinterview@gmail.com` |
   | `NOTIFY_EMAIL` | `launchpadinterview@gmail.com` |

## Testing before going live

1. With Razorpay **test-mode** keys still in place, open the deployed Vercel URL, fill the buy form, and pay with a [Razorpay test card](https://razorpay.com/docs/payments/payments/test-card-details/).
2. Confirm the success message appears, and that both the buyer email and the owner-notification email actually arrive (check Brevo's dashboard logs if not).
3. Only after that works end to end: switch the Razorpay dashboard from test mode to live mode, generate **live** API keys, and replace `RAZORPAY_KEY_ID`/`RAZORPAY_KEY_SECRET` in Vercel with the live values.

## Updating the product file later

If `product/app/index.html` changes, rebuild the zip (see `product/README.md`) and copy the new zip over `website/dist/interview-launchpad.zip`, then push — Vercel redeploys automatically.
```

- [ ] **Step 2: Commit**

```bash
git add website/README.md
git commit -m "Add deploy instructions for the sales website"
```

---

### Task 8: Manual verification pass

**Files:** none created — this task only runs checks against Tasks 1–7.

**Interfaces:**
- Consumes: the full `website/` tree from Tasks 1–7.
- Produces: nothing (terminal task).

- [ ] **Step 1: Serve the static site locally and open it in the Browser tool**

Run (from `website/`): `python -m http.server 8080` (or any static file server)
Then use the Browser tool to navigate to `http://localhost:8080`.

- [ ] **Step 2: Visual check at desktop width**

Confirm: hero renders, nav sticky header works, all four "how it works" cards are visible and readable, pricing section shows ₹4,999, no dark-gradient/glow styling anywhere (flat light backgrounds, one accent color only).

- [ ] **Step 3: Visual check at mobile width**

Use `resize_window` (preset `mobile`) in the Browser tool, reload, confirm the hamburger nav opens/closes and every section reflows without horizontal scrolling.

- [ ] **Step 4: Form validation check**

Click "Buy for ₹4,999" with both fields empty — confirm the inline "Please fill in both fields." message appears and no network request fires (check via `read_network_requests`).

- [ ] **Step 5: Note the limits of local-only verification**

The full payment round-trip (`create-order` → Razorpay Checkout modal → `verify-payment` → Brevo email) requires live Razorpay test-mode keys and a Brevo API key that only Sid can generate in his own accounts (§4.2 of the spec — these are never entered by this task). This task confirms the page renders correctly and the client-side code has no syntax errors; the end-to-end payment test happens after Sid completes `website/README.md`'s setup steps on the deployed Vercel URL.

- [ ] **Step 6: Final syntax sweep**

Run: `node --check website/script.js && node --check website/api/create-order.js && node --check website/api/verify-payment.js && echo ALL_OK`
Expected: `ALL_OK`

---

### Task 9: Push to the `lauchpad` GitHub repo

**Files:** none created — this task moves the already-committed `website/` folder from this workspace's `main` onto `launchpad/main`.

**Interfaces:**
- Consumes: the `website/` tree committed in Tasks 1–7, and the `launchpad` git remote already configured in this workspace (confirmed: `launchpad → https://github.com/siddharth-sharma-dev668/lauchpad.git`).
- Produces: `website/` present on `github.com/siddharth-sharma-dev668/lauchpad` under `main`, without disturbing files already on that remote that this workspace doesn't have (`dist/*.png`, `INSTAGRAM_PLAN.md`, etc. — per [[launchpad-product-direction]] memory, never force-push this repo's `main` onto it).

- [ ] **Step 1: Fetch the current state of the remote**

```bash
git fetch launchpad
```

- [ ] **Step 2: Create a throwaway worktree tracking `launchpad/main`**

```bash
git worktree add ../launchpad-website-push -b add-sales-website launchpad/main
```

- [ ] **Step 3: Copy the `website/` folder into the worktree**

```bash
cp -r website ../launchpad-website-push/website
```

- [ ] **Step 4: Diff-check before committing — confirm nothing outside `website/` changed**

```bash
cd ../launchpad-website-push && git status
```
Expected: only new files under `website/` are listed as untracked/added — nothing existing is modified or deleted.

- [ ] **Step 5: Commit and push the branch**

```bash
git add website/
git commit -m "Add Razorpay-backed sales website"
git push launchpad add-sales-website
```

- [ ] **Step 6: Merge on GitHub, then clean up the worktree**

Open a PR from `add-sales-website` into `main` on `github.com/siddharth-sharma-dev668/lauchpad` (or fast-forward merge locally if Sid prefers no PR ceremony for a solo repo), merge it, then:

```bash
cd "C:\Users\jshar494\sid carrer"
git worktree remove ../launchpad-website-push
git branch -D add-sales-website 2>/dev/null || true
```

- [ ] **Step 7: Confirm Vercel is connected**

This step is Sid's own action per `website/README.md` §"One-time setup" — not something this plan's executor can do (it requires his own Vercel/Razorpay/Brevo browser logins). Report completion back to him with a pointer to `website/README.md` once the push lands.
