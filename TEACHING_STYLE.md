# Teaching Voice — how Launchpad content gets written

Sid's feedback, 2026-09-06, verbatim reason: the *content* in the concept lessons was correct, but two things were missing — (1) real data/output was asserted in prose instead of shown, especially a SQLite-vs-Postgres claim that was never actually run against Postgres, and (2) the writing read like an AI/consulting deck ("senior framing," "the tell," em-dash-heavy punchlines) instead of how an Indian engineering teacher actually explains something (GATE Smashers, Apna College, NPTEL-style: concrete example first, plain step-by-step mechanism, direct address, no cleverness for its own sake).

This file is the standing style guide for every Lesson page and drill-file comment in this project, generated now or later, for Sid or for any other Launchpad user — not a one-time fix for Week 1.

## The two structural rules (not style — these are correctness/trust rules)

1. **Show the data before the behavior.** If a lesson involves a table, a dataset, or specific values, render them as an actual visible table/list at the top, before any query or example touches them. Never describe data in prose ("a table of employees") when you can just show the four rows.
2. **Never assert a cross-system/cross-language behavioral claim without running it.** "Postgres rejects this, SQLite doesn't" is not something to state from general knowledge — run it in both, capture the real output, show both side by side. If you can't run it (no access to the second system), say so explicitly and mark the claim as unverified — do not present it with the same confidence as something you checked. (This is exactly the mistake caught in `sql_playground.py`'s first draft: verify against Postgres, don't recite the SQL standard and call it done.)

## The voice — concrete before, concrete after

**Before (what shipped in Week 1, the problem):**
> Junior framing: "what's the difference between a list and a set?" Senior framing: "given this access pattern, what does the wrong choice cost at 10M rows?" Same four containers, different question — and the second one is what actually gets asked once you're past the definitions round.

**After (the fix):**
> Suppose you're checking "have I already seen this user ID?" inside a loop, once per incoming event. With a list, Python checks every element one by one until it finds a match or reaches the end — so each check gets slower as the list grows. With a set, Python jumps straight to the right spot using the value's hash — each check takes roughly the same time whether there are 10 items or 10 million. Do that check inside a loop over 10,000 events, on a list of 10,000 IDs, and you've quietly written 100 million comparisons. That's the actual bug interviewers are listening for.

What changed, concretely:
- **Starts with "suppose"/"let's say"** — a scenario, not an abstract reframe.
- **Explains the mechanism in plain steps** ("checks every element... jumps straight to the right spot using the hash") instead of naming the concept and moving on.
- **One worked number** (10,000 × 10,000 = 100 million) instead of a vague "10M rows."
- **No em-dash-punchline structure, no "framing," no "the tell."** Say the practical consequence directly.
- **Still short.** Teacher-voice is concrete, not longer for its own sake — cut anything the example already showed.

## Concrete rules to write by

1. **Open with a scenario, not a reframe.** "Suppose you have..." / "Say you're building..." / "Consider this table:" — ground the abstract rule in one small, specific situation before naming the rule.
2. **Explain mechanism step by step.** Don't write "HashSet hashes to the bucket" and move on — write what that means: compute the hash, jump to that slot, compare. A reader should be able to trace it by hand.
3. **Use small, literal numbers you can count on your fingers**, not "10M rows" as decoration — unless you're doing the actual scaling arithmetic (as above), in which case show the arithmetic.
4. **Address the reader directly and name the likely wrong guess before correcting it.** "You might expect X here — but actually Y, and here's why." This is the single most common move in these lecture styles and it's what makes an explanation feel taught rather than stated.
5. **Cut the interview-industry vocabulary**: "framing," "the tell," "differentiator," "signal," "flag" (as a noun for "warning sign"), "leverage." These compress an idea instead of explaining it. Say the plain thing instead.
6. **One idea per sentence.** Break up any sentence doing three jobs at once (setup + mechanism + consequence, joined by em-dashes) into two or three short sentences.
7. **End with the plain takeaway, stated once, not a punchline.** Not "that's the kind of bug that passes review and fails at scale" — instead "if you don't catch this in review, it works fine in testing and gets slow only once real traffic hits it."
8. **Repetition for clarity is fine.** Teachers restate the key point in a second, slightly different way. Dense one-pass writing is an AI-voice tell, not a virtue.
9. **Diagnostic tie-ins stay** (they're genuinely motivating and specific to Sid) — just say them plainly: "your diagnostic missed this exact thing" rather than wrapping it in a "senior vs junior" frame.

## Where this applies

Every `explain[]` array on a Lesson page (`LESSONS[w]` in `platform/index.html`), going forward from Week 1 onward — Week 1's three lessons were rewritten under this guide on 2026-09-06 as the reference examples. Drill-file comments (`gotchas.py` etc.) were largely already terse/plain and don't need the same rewrite, but any new prose explanation added to a drill file should follow rules 1-3 and 5-7 above too.

This guide is deliberately generic (no Sid-specific facts in the rules themselves) so it holds if this curriculum generator is ever reused for someone else on the Launchpad platform.
