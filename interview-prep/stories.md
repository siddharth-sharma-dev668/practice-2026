# STAR stories

Each story here has a companion note on the ONE thing that's easy to overclaim in it —
read that before you say the story out loud in an interview, not after.

---

## Story 1 — Onextel p95 latency, cut ~20%

**Situation:** At Onextel, on a platform serving 10M+ messages/month, one of the endpoints
I owned was showing up as slow — not from a monitoring dashboard, but from users/QA
reporting sluggishness on a specific flow. That's the honest starting point: I found it
by someone noticing, not by proactively watching a metric.

**Task:** Track down why that endpoint was slow and fix it, without breaking correctness
or making the fix worse for other callers of the same tables.

**Action:** I dug in with `EXPLAIN` on the queries behind the slow endpoint to see where
time was actually going — sequential scans, bad join order, whatever `EXPLAIN` showed.
From there it was a mix of three things, not one silver bullet:
- Fixed/added indexes where `EXPLAIN` showed a sequential scan that should have been an
  index scan.
- Rewrote at least one query that was structured inefficiently (e.g. doing more round
  trips or joins than the data actually needed).
- Put a Redis cache-aside layer in front of the read path so repeat reads of the same
  data didn't re-hit Postgres at all.

I chose Redis specifically because the data being read was read far more often than it
changed — a cache-aside pattern (check Redis, fall back to Postgres on a miss, write
back to Redis) fit that access pattern directly, rather than reaching for caching as a
default.

**Result:** p95 latency on that path came down by roughly 20%. **Important, be honest
about this part**: I didn't pull that number myself off a dashboard or a load test — my
team/lead reported the improvement after the fix shipped. I know what changed and why it
should have helped (fewer sequential scans, fewer round trips, cache hits avoiding the DB
entirely) — but I can't hand an interviewer my own before/after measurement for the
percentage itself.

**If probed further ("how did you measure that?" / "walk me through the query plan"):**
Say exactly what's true — "the 20% figure was reported to me by my lead after the fix
shipped; what I can walk you through directly is what `EXPLAIN` showed before and after
on the queries I changed, and why each of the three fixes should reduce latency." That's
a stronger answer than pretending you pulled the dashboard yourself — interviewers probe
harder on a shaky claim than an honest one.

**Still to fill in, if you remember and want the story sharper:** which table/endpoint this
was (order lookups? messaging status? something else), and roughly how many indexes/which
query you rewrote. Not required to use this story, but it makes the "Action" section
concrete instead of general if you want to add it later.
