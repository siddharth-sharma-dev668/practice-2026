# Pulse — spec (Week 1 draft)

This is the start of the actual capstone repo, not another exercise. Everything
below is a prompt, not an answer — fill in your own words/decisions. This file
is what you rehearse from in a "tell me about a project you built" interview
question from Week 12 onward, so write it like you'll actually say it out loud.

## 1. What is Pulse, in your own words?

(3-5 sentences. Not "an event platform" — say what it ingests, what it's for,
and which of your target roles it proves. If you're stuck, the honest source
is `MASTER_PLAN.md` section 5 — read it, then write this in YOUR words, not
copied.)

>

## 2. One event, sketched

Pulse ingests "events." Before any code exists, decide the minimum shape of
ONE event — field names and types. This becomes the Postgres table you design
in Week 3, so a real decision now saves a rewrite later.

```json
{

}
```

Questions to answer before you write the JSON above:
- What's the one field every event MUST have, no matter what kind of event it is?
- What's genuinely optional, and what does "missing" mean for it? (Look back at
  the SQL lesson's `department_id = NULL` — same idea: NULL is a design choice,
  not an accident.)

## 3. Architecture, one hop at a time

Fill in each arrow with what actually moves across it (a request? a row? a
message?) — not just box names.

```
[ ?? ] --> [ ?? ] --> [ ?? ] --> [ ?? ]
```

By Week 12 this needs to include: an ingest endpoint, Postgres, Redis, a queue
with retries, an anomaly-detection model, and an NL-query path. You don't need
all of that now — just the shape you'd start building next week.

## 4. Repo layout — what Week 2 actually builds

Propose a folder structure for the FastAPI service (this becomes real in
Week 2 — "Repo skeleton, FastAPI up, Docker builds"). A reasonable starting
shape, edit it:

```
pulse/
  app/
    main.py
    models.py
    routes/
  tests/
  Dockerfile
  requirements.txt
```

## 5. What gets built when (reference, not a prompt)

Copied from `MASTER_PLAN.md` §3 so you don't have to flip files mid-week.

| Week | What ships |
|---|---|
| 2 | Repo skeleton, FastAPI up, Docker builds |
| 3 | Event-ingest endpoint + Postgres |
| 4 | Events persisted, schema designed for real |
| 5 | Async ingest + worker stub |
| 6 | Test suite + CI green — Stage 1 checkpoint |
| 7-11 | Auth, rate limits, model, NL-query, deploy |
| 12 | **PULSE SHIPS** — design doc, demo, eval report, Resume v1 |
