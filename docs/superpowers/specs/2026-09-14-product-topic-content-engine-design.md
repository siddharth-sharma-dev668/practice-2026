# Product topic-content engine — design

**Status:** approved in chat 2026-09-14, awaiting written-spec review.
**File touched:** `product/app/index.html` only (single static file, no build step, no new files).

## 1. Problem

The personal Launchpad (`platform/index.html`) already solved "study steps must be runnable predict/verify drills, not doc links" — see [feedback-no-doc-link-study.md] extensions 1–7. The sellable product (`product/app/index.html`) never got the same fix. Every one of its 50 topics in `T` (`product/app/index.html:319-379`) still renders as a list of external doc-link chips (`t.lk`, rendered in `renderWeek()` at `product/app/index.html:981`).

The gap is specifically about **who the content is for**. The Launchpad's `LESSONS`/`DRILLS` are keyed by `(week, id)` because Sid's plan is fixed — Week 1 is always Week 1. The product's plan is generated per buyer by `generatePlan()` (`product/app/index.html:579`): the same topic id (e.g. `sql-join`) can land in Week 2 for one buyer and Week 5 for another, depending on their resume and diagnostic. Content must therefore be keyed by **topic id**, globally, not by week.

## 2. Goal

Every buyer, for whatever role/track `generatePlan()` assembles for them, gets the same lesson+drill experience Sid gets in the Launchpad — in the browser, no VS Code, no terminal — for every topic that has been authored. Topics not yet authored keep working exactly as today (doc-link chips), so this ships incrementally across 5 authoring batches without ever breaking the app.

## 3. Non-goals

- No change to `generatePlan()`, `ROLE_PLAN`, `CAPSTONE`, or the diagnostic/quiz engine.
- No new files, no CDN libraries, no server. Stays a single static HTML file (same constraint as `platform/index.html`).
- No requirement to author all 50 topics before anything ships — see §7.
- Not extending to DSA or capstone steps — those already route to LeetCode / are buyer-written project work respectively, matching the Launchpad's own "route to real judges, don't rebuild banks" rule ([feedback-no-doc-link-study.md] extension 5).

## 4. Architecture

### 4.1 `TOPIC_CONTENT` — new top-level object, keyed by topic id

```js
const TOPIC_CONTENT = {
  "sql-join": {
    diagram: "<svg viewBox=\"0 0 640 360\" ...>...</svg>",   // inline SVG, currentColor/CSS vars, same rule as platform LESSONS
    explain: [ "...", "...", "..." ],                          // teacher-voice paragraphs, TEACHING_STYLE.md rules apply
    code: "SELECT ...",                                        // string, OR [{label,text}, ...] for bilingual topics (java-core, java-conc)
    drill: [
      { code: "...", question: "...", answer: "...", why: "..." },
      ...
    ]
  },
  // one entry per authored topic id from T; absent id = not yet authored
};
```

This is the exact shape of `LESSONS[w][i]` + a `DRILLS[w][i]`-style array, merged into one object per topic and re-keyed by topic id instead of `(week, index)`. No new concepts — a direct reuse of the pattern already verified working in `platform/index.html`.

- `diagram` — optional. Hand-authored inline SVG, same as `LESSONS[w][i].svg`. Topics that don't have a natural picture (e.g. `behav`, `resume`) omit it.
- `explain` — array of paragraph strings, teacher-voice per `TEACHING_STYLE.md`: concrete scenario first, plain mechanism, no interview-industry jargon.
- `code` — a single code string, or an array of `{label, text}` pairs for topics that need two languages side by side. Bilingual applies only where the Launchpad already established it matters: `java-core`/`java-conc` (DSA-adjacent, Java-vs-Python is the buyer's actual dilemma). Every other topic is single-language, matching its natural ecosystem (SQL topics are SQL, AI/ML topics are Python, `js-core`/`react` are JS).
- `drill` — array of predict-then-reveal blocks, identical shape to the Launchpad's `DRILLS[w][i]` blocks (`{code, question, answer, why}`). Rendered as text-input-then-reveal, same mechanism as `renderDrill()` in `platform/index.html`.

### 4.2 Rendering changes

**`weekSteps()` (`product/app/index.html:906-932`)** already carries the topic's `id` on every `t` object (confirmed: `generatePlan()` does `chosen.push({id,...t,hrs,mode})` at line 603, and that object flows unchanged into `wk.topics`). Add one field to each pushed step:

```js
wk.topics.forEach(t=>steps.push({
  ...,
  links: t.lk,
  topicId: t.id          // NEW — carries through to renderWeek()
}));
```

`revision` steps get the same `topicId: t.id` addition. DSA/capstone/quiz steps are untouched (no topic id to attach).

**`renderWeek()` (`product/app/index.html:964-996`)**, in the per-step render (around line 981), change the link-chip block from unconditional `s.links` rendering to:

```js
const tc = s.topicId ? TOPIC_CONTENT[s.topicId] : null;
// ...
${tc ? `<div class="topicbtns">
    <button class="go small" data-opentopic="${s.topicId}">Open lesson →</button>
    <button class="go small" data-opendrill="${s.topicId}">Practice here →</button>
  </div>` : (s.links && s.links.length ? `<div class="linkchips">...</div>` : "")}
```

**Fallback is non-negotiable**: if `TOPIC_CONTENT[s.topicId]` is absent, render exactly what renders today (`s.links` doc chips). An unauthored topic must look and behave identically to the current app — this is what makes 5 incremental authoring batches safe to ship one at a time.

### 4.3 New render functions

Two new functions, direct ports of `renderLesson(w,id)` / `renderDrill(w,id)` from `platform/index.html`, re-keyed by topic id instead of `(week,id)`:

- `renderTopicLesson(topicId)` — pushes a lesson view (`diagram` + `explain` + `code`) into `#view-roadmap` (or a dedicated `#view-topic`, matching however the Launchpad overlays its lesson view — reuse that exact mechanism, don't invent a new one), with a back button returning to `renderWeek(w)`.
- `renderTopicDrill(topicId)` — same predict-then-reveal block loop as `renderDrill()`: disabled-until-typed `<input>` per block, "Reveal answer" button, shows `answer` + `why` on click.

Wiring: after `renderWeek()` builds its HTML, `host.querySelectorAll("[data-opentopic]")` / `[data-opendrill]` get click listeners calling the two functions above, exactly mirroring how `platform/index.html` wires `[data-opendrill]` today.

### 4.4 Progress persistence

Drill answers persist through the app's existing `S.tasks` + `save()` mechanism (same pattern already used for step checkboxes and the Launchpad's drills), keyed as:

```
S.tasks[`topic:${topicId}:${blockIndex}`]
```

Using topic id (not week+id) is deliberate: if a buyer's plan repeats a topic across weeks via `revision` (spaced repetition), their drill progress on that topic is shared, not duplicated — which is the correct behavior, since it's the same underlying drill content either way.

No changes to `blank()`'s state shape (`product/app/index.html:516`) — `S.tasks` is already a flat string-keyed map, this just adds a new key prefix alongside the existing `"${w}:${i}"` step-checkbox keys.

## 5. Verification bar

Matches the Launchpad's existing standard, split the same way:

- **Code topics** (anything with an `sk` resume-skill key that maps to a real runnable language/tool — `py-core`, `py-adv`, `py-test`, `java-core`, `java-conc`, `sql-join`, `sql-cte`, `sql-win`, `sql-perf`, `sql-anal`, `js-core`, `react`, `frontend`, `css-core`, `llm-base`, `ml-core`, `ml-sk`, `ml-dl`, `stats`, `ab`, etc.): every `drill` block's code must actually be run before being written into `TOPIC_CONTENT`, and its `answer`/`why` must describe what really happened — same rule as `TEACHING_STYLE.md`'s "show real data before behavior" and "never assert a cross-system claim without running both sides."
- **Conceptual/discussion topics** (no single runnable snippet proves the point — `sysd-1`, `sysd-2`, `lld`, `behav`, `resume`, `verify`, `unassist`, `narrate`, `debuglive`, `defend`, `aitools`, `guard`, `mlops`, `viz`): `explain` + `diagram` (where a diagram helps) carries the lesson, framed as established engineering knowledge — never phrased as "measured" or "verified" since nothing was run. `drill` for these becomes a worked scenario + question, same substitute pattern the Launchpad already uses for non-runnable concept steps (see [feedback-no-doc-link-study.md], the original 2026-09-05 rule: "a worked scenario with a question to answer, not a reading list").

This distinction must be decided per-topic by whoever authors that batch, not assumed from the list above — the list is a starting split, not a rule to apply blindly.

## 6. CSS

Reuse `platform/index.html`'s existing `.figure`, `.codeblock`, `.reveal`, `.drill-block`/`.drill-num`/`.drill-q`/`.drill-row`/`.drill-guess`/`.drill-reveal:disabled`/`.drill-answer`/`.drill-block.done` classes verbatim (copy the CSS block across) plus one new small class, `.topicbtns`, for the two-button row that replaces `.linkchips` when a topic is authored. No new visual language — the product app already shares most of its color tokens/layout primitives with the Launchpad.

## 7. Authoring batches (for session delegation)

All 50 current `T` topic ids, grouped by domain so each batch is self-contained (one person/session/model call can author a batch without needing context from another):

| Batch | Domain | Topic ids | Count |
|---|---|---|---|
| 1 | Python / Java core | `py-core`, `py-adv`, `py-test`, `java-core`, `java-conc`, `spring` | 6 |
| 2 | SQL / Data / Stats | `sql-join`, `sql-cte`, `sql-win`, `sql-perf`, `sql-anal`, `db-design`, `etl-core`, `stats`, `ab`, `viz` | 10 |
| 3 | Web / Systems / Infra / JS | `js-core`, `react`, `api`, `framework`, `auth`, `cache-q`, `ship`, `sysd-1`, `sysd-2`, `lld`, `frontend`, `css-core`, `linux-core`, `cloud-core` | 14 |
| 4 | AI / ML | `llm-base`, `prompt`, `tools`, `mcp`, `rag`, `evals`, `guard`, `ml-core`, `ml-sk`, `ml-real`, `ml-dl`, `mlops`, `aitools` | 13 |
| 5 | Behavioral / interview-craft meta | `behav`, `resume`, `verify`, `unassist`, `narrate`, `debuglive`, `defend` | 7 |

(50 total — corrects the "~38" figure used loosely during the in-chat design discussion; the actual current count in `T` is 50, confirmed by reading the file.)

Each batch is independently committable: adding `TOPIC_CONTENT` entries for Batch 1's 6 ids and shipping is a complete, safe, working state (Batch 1's topics get lessons/drills, the other 44 keep today's doc-link chips via the fallback in §4.2). Batches can be done in any order and by different sessions/Agent calls per Sid's "assign this task to another session if needed" — each batch's task should be handed the schema in §4.1, the verification-bar split in §5, and only its own row from the table above.

## 8. Rollout order

1. Land the mechanism first (§4.2–§4.4: `weekSteps()`/`renderWeek()` changes, the two new render functions, the CSS, an empty `TOPIC_CONTENT = {}`) as one commit — verifiably non-breaking, since every topic falls through to the existing doc-link path.
2. Author and land batches 1–5 as separate follow-up commits/sessions, in whatever order is convenient. Each batch commit should include: the actually-run verification for its code topics (paste real output the way `sql_playground.py`/`Gotchas.java` did), and a manual browser check (open the product app, generate a plan that includes at least one topic from the batch, click "Open lesson" and "Practice here", confirm the reveal mechanism works and progress persists across a reload).

## 9. Testing

No test framework exists in this repo (matches `platform/index.html`'s own verification approach). Verification is:
- `node --check` on the extracted `<script>` block after every edit (same pattern used for every `platform/index.html` publish this project).
- Manual browser pass in the Browser tool: fill setup → generate a plan → open a week containing an authored topic → click through lesson and drill → confirm reveal + persistence.
- For code-topic drills specifically: the snippet is actually executed (Python/Java/SQL as appropriate) before being transcribed into `TOPIC_CONTENT`, exactly as the Launchpad's drill files were.
