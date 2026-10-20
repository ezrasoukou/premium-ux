# Audit playbook

> Audit mode: reviewing a shipped or in-progress product and recommending what would make it feel
> premium.

## Contents

- [What an audit is for](#what-an-audit-is-for)
- [Step 1: Frame](#step-1-frame)
- [Step 2: Gather evidence](#step-2-gather-evidence)
- [Step 3: Score](#step-3-score)
- [Step 4: Prioritize](#step-4-prioritize)
- [Step 5: Write it up](#step-5-write-it-up)
- [Working from limited access](#working-from-limited-access)

## What an audit is for

The deliverable is a **prioritized diagnosis**, not a list of complaints. The failure mode of
design reviews is 40 findings of equal weight that nobody can act on. A good audit tells someone
what to do on Monday and why it matters more than the other 39 things.

Three rules that keep an audit useful:

**Evidence over opinion.** Every finding names where it is, what happens, and why it costs
something. "The onboarding feels cheap" is not a finding. "Step 3 of onboarding clears the form
when email validation fails, so users who typo re-enter four fields" is.

**Lead with the ceiling, not the paint.** People expect an audit to be about visual design, and
it mostly should not be. The diagnosis that earns its fee is usually that the product's states,
transitions, and failure paths are unfinished — which is also the cheapest thing to fix and the
hardest for a competitor to copy. Say that clearly even when the brief said "make it look more
premium."

**Name what is already working.** Partly because audits that read as pure criticism get defended
against rather than acted on. Mostly because premium work is cumulative: if you do not know what
the product's existing strengths are, your recommendations will quietly sand them off.

## Step 1: Frame

Before touching the product, establish:

- **The job.** What does this product do, for whom, instead of what?
- **The premium thesis.** What justifies charging more than the alternatives? Get the team's answer
  in one sentence. If there is no coherent answer, that is the headline finding — the problem is
  positioning, and UX work will not substitute for it. Say it plainly and early rather than
  delivering polish that cannot fix it.
- **The core flow.** The one path that matters most. Audit it deeply rather than auditing
  everything shallowly.
- **What "premium" means here.** It is not universal. A surgical scheduling tool earns premium
  through precision and recoverability; a consumer journal earns it through calm and craft. Match
  the register to the domain before judging anything.
- **Constraints.** Team size, stack, release cadence, what is already planned. Recommendations that
  ignore these do not get built.

## Step 2: Gather evidence

Do these in order. The hands-on pass is non-negotiable — the entire method depends on contact with
the running product. An audit written from source code and screenshots will miss nearly everything
that matters, because the findings live in transitions, timing, and what happens when things go
wrong.

**A. The real-user hour.** Use the product the way its users do: real account, real data, real
device, real network. Do the core flow repeatedly, then wander. Capture a screenshot of everything
notable. Write down every moment of hesitation, re-reading, backtracking, or "wait, what happened?"
Do not fix or theorize yet — just collect. See `coherence.md` for the prompts that surface breaks
fastest.

**B. The state sweep.** For each surface in the core flow, drive it through the state matrix in
`state-coverage.md`: empty, first-run, loading, partial, success, error, offline, unauthorized,
expired, over-limit. Most of these take seconds to force with dev tools. Note which ones were
clearly never designed — unstyled defaults, missing copy, a spinner that never resolves.

**C. The break-it pass.** Run the protocol in `failure-and-recovery.md`. Kill the network
mid-submit, fail a payment, force a 500, revoke a permission, kill the app mid-form. Screenshot
every result. This pass typically produces the highest-severity findings in the whole audit,
because almost nobody designs these and the cost of leaving them is disproportionate.

**D. The coherence inventory.** Sweep the axes in `coherence.md` — language, navigation,
interaction, feedback vocabulary, visual system, density. Look for the same job done differently
in two places. Count the words used for the same concept.

**E. The code scan (if you have the repo).** Run the scanner for a fast map of where state
handling is thin:

```bash
python3 ../scripts/state_audit.py --path /path/to/repo
```

Treat every hit as a candidate and read the code before reporting it — the heuristics flag
components that legitimately delegate state to a parent. The value is in deciding where to look,
not in the percentage it prints.

**F. Mechanics review (if the product has any).** If there are streaks, points, badges,
leaderboards, or progress systems, assess them against `motivation-design.md`. Ask the two
diagnostic questions: would anyone do the underlying activity without the mechanic, and does the
metric it drives match the behavior the business needs?

**G. Ethics pass.** Walk the red-flag list in `ethics-and-regulation.md`. Dark patterns belong in
an audit for two reasons: they make a product feel cheap regardless of its craft, and in 2026
several carry real regulatory exposure. Report them as risk, not as moralizing.

## Step 3: Score

Score each dimension 0–5. The weights reflect how much each one moves the perception of premium
relative to how cheap it is to fix — they are a default, and worth adjusting if a product's domain
clearly demands it (say, coherence matters more in a tool used all day).

| # | Dimension | Weight | What a 5 looks like |
|---|---|---|---|
| 1 | **State coverage** | 25% | Every state designed and specific; user always knows what happened, that it is reversible, and what is next |
| 2 | **Coherence** | 20% | Reads as one product throughout; one pattern per job; language consistent |
| 3 | **Failure & recovery** | 20% | Failures are informative, preserve work, offer a real next step and a human |
| 4 | **Flow friction** | 15% | Smart defaults, value before asks, no dead ends, nothing blocks first use unnecessarily |
| 5 | **Motivation** | 10% | One well-chosen engine tied to real outcomes, or none and that is correct |
| 6 | **Surface craft** | 10% | Consistent system, purposeful motion, respects accessibility settings |

**Scoring anchors**, so scores mean the same thing across audits:

- **0** — absent. Not designed at all; unstyled defaults or nothing
- **1** — present by accident. Framework defaults, generic strings, no evident decisions
- **2** — inconsistent. Done well in a few places, missing or contradictory in most
- **3** — adequate. Covered, not distinctive; nothing embarrassing, nothing memorable
- **4** — considered. Deliberate decisions visible throughout, with gaps at the edges
- **5** — evidently lived in. Specific to this product's users in ways a competitor could not copy
  from the outside

Report the weighted total as a rough position — **below the commodity ceiling** (under ~2.5),
**at it** (2.5–3.5), or **above it** (3.5+) — rather than as a precise number. A product scoring
2.8 and one scoring 3.1 are in the same place; false precision invites arguing about the number
instead of fixing the findings.

## Step 4: Prioritize

Rank every finding on two axes:

**Severity** — does it break trust (user loses work, money, or confidence), cost effort every
session, or merely look unresolved?

**Cost** — a copy change, a component change, or a structural change?

Then sort into three buckets. The pattern that makes audits actionable is that the top bucket is
almost always copy and state work, because that is where severity is high and cost is low:

- **Now** — high severity, low cost. Failure-state copy, preserving form input, exact numbers and
  dates instead of vague strings, the missing escape hatch on the payment error. Days of work,
  disproportionate effect
- **Next** — high severity, higher cost. Consolidating three error patterns into one component,
  rebuilding the over-limit flow, adding an offline queue
- **Later** — lower severity or structural. The spacing scale, the motion system, the mechanic
  redesign

Cap the "Now" list at around five items. An audit that makes everything urgent has not done the
prioritization, which was the job.

## Step 5: Write it up

Use `../assets/audit-report-template.md`. The structure that lands:

1. **Verdict** — two or three sentences. Where the product sits relative to the commodity ceiling
   and why
2. **The one thing** — if they fix only one thing, this. Be specific and name the expected effect
3. **Scorecard** — the six dimensions with scores and a one-line justification each
4. **What is already working** — genuinely, with specifics, so it gets protected
5. **Findings** — grouped by dimension, each with: where it is, what happens, why it costs
   something, and the fix. Include the screenshot or exact copy string
6. **Prioritized plan** — Now / Next / Later, with rough effort
7. **What was not covered** — scope honesty: platforms, flows, or states you did not get to

Write findings as *observations with consequences*, not instructions. "The declined-payment screen
shows an error code and no next step; a user whose card fails has no way to tell whether to retry
or contact their bank, in the moment they are most worried about their money" is useful. "Add
better error handling" is not.

## Working from limited access

Often you get screenshots, a Figma file, or a URL and no account. Be explicit about what that
limits, because the highest-value findings live in exactly the places you cannot reach.

**What you can still assess well:** copy specificity, coherence across whatever surfaces you can
see, information hierarchy, the ethics red-flag list, visual system consistency, and whether
designed states exist in the design file at all (their absence in Figma is itself a strong signal —
if nobody drew the error state, nobody built it).

**What you cannot assess:** timing, transitions, perceived performance, recovery behavior, undo,
offline, and anything about what actually happens when something fails. These are most of the
premium signal.

Say so in the report's scope section, score only what you observed, and mark unscored dimensions as
*not assessed* rather than guessing. Then ask for what you need: a test account, a staging
environment, or a 30-minute screen share where someone drives while you direct them through the
break-it protocol. That last option is cheap and recovers most of what you are missing.
