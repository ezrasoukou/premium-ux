---
name: premium-ux
description: "Build apps that feel premium and audit shipped products for what makes them feel cheap. Use this whenever the user wants a product to feel premium, expensive, high-end, polished, or 'less like AI slop'; asks why their app feels cheap, generic, janky, thrown-together, or unfinished; wants a UX review, design audit, product critique, or polish pass; is designing onboarding, empty/loading/error states, paywalls, pricing, upgrade prompts, or failure and recovery flows; is adding streaks, points, badges, leaderboards, progress rings, or any gamification or retention mechanic; or is trying to justify charging more for a product that looks like its competitors. Works for both greenfield building and already-shipped products, and includes a scored audit rubric plus a state-coverage scanner."
metadata:
  version: "1.0.0"
  license: MIT
---

# Premium UX

## The core idea: the commodity ceiling

The brain has no premium detector. It keeps score of **evidence that a product is good**, and
that score is what reads as "premium."

Packaging research has a useful split: *the look gets you picked, evidence of quality gets you
called premium.* Pretty and premium were never the same thing. This matters more every month,
because any founder can now point an agent at the best design references in existence and ship
something that looks decent in a day. Decent-looking is the **floor**, and the floor rises for
everyone simultaneously — whatever an AI tool learns this quarter, every competitor gets the same
week. The ceiling is made of something else.

What sits above the ceiling is the accumulated weight of hundreds of small decisions that only
someone who actually used the product would have made. That is the thing no component library,
design system, or model hands you out of the box, and it is why one app can charge 5× another that
screenshots identically.

**So when someone asks to make a product feel premium, do not start with gradients.** Surface
craft is real but it is the cheapest layer to copy and the first thing a competitor matches. Work
the levers in the order below — it is roughly inverse to the order most teams reach for.

## The lever order

| # | Lever | What it fixes | Reference |
|---|---|---|---|
| 1 | **State coverage** | User never wonders "did that work? can I undo? what now?" | `references/state-coverage.md` |
| 2 | **Coherence** | 80 screens that feel like one product, not 80 prototypes | `references/coherence.md` |
| 3 | **Failure & recovery** | The moments that decide whether people trust you | `references/failure-and-recovery.md` |
| 4 | **Flow friction** | Effort, decisions, and dead ends removed from core paths | `references/flow-psychology.md` |
| 5 | **Motivation engine** | Durable reasons to come back (only if retention is the problem) | `references/motivation-design.md` |
| 6 | **Surface craft** | Motion, type, spacing, haptics, sound | last — and the most copyable |

Levers 1–3 are where almost all unclaimed premium value sits, because they are unglamorous and
most teams skip them. That is exactly what makes them cheap to win.

Before shipping anything from levers 4 and 5, run it past `references/ethics-and-regulation.md`.
Several of the most effective patterns here are one design decision away from being a dark pattern,
and in 2026 some are a regulatory exposure too. A product that feels manipulative does not feel
premium — it feels like a trap with good typography.

## Pick a mode

**Audit mode** — there is a shipped or in-progress product to review. Go to
`references/audit-playbook.md` and follow it. It has the scored rubric, the evidence-gathering
protocol, and the report format. Do not skip the hands-on pass: the whole method depends on
actually using the product and breaking it, not reading its source and theorizing.

**Build mode** — something new is being designed or a feature is being added. Follow the loop below.

If it is ambiguous, ask which one. The work is genuinely different: audit produces a prioritized
diagnosis, build produces a design.

## Build mode loop

**1. Name the job and the premium thesis.**
What does this product do that justifies paying more? One sentence. Everything downstream should
be traceable to it. If there is no answer, the real problem is positioning, not UI — say so plainly
rather than polishing around it.

**2. Map the core flow end to end.**
List every screen and every transition in the one path that matters most. Not the whole app — the
spine. Most premium failures live in the transitions, not the screens.

**3. Enumerate states before building any of them.**
For each surface, write out its states — empty, first-run, loading, partial, success, error,
offline, unauthorized, expired, over-limit, destructive-confirm, undo. The full matrix and what
each one owes the user is in `references/state-coverage.md`. Doing this *before* building is
the single highest-leverage habit in this whole skill, because retrofitting states means
rewriting components.

**4. Build the happy path and its states together.**
Not "happy path now, states later." Later never arrives, and the states are the product's
character. A component that takes `data` but has no shape for loading/error/empty is not done.

**5. Apply flow psychology to the paths with drop-off.**
Smart defaults, endowed progress, give-before-ask, build-before-signup. See
`references/flow-psychology.md`. Check each against the ethics gate.

**6. Break it on purpose.**
Turn off the network mid-flow. Fail a payment. Empty every list. Revoke a permission. Kill the app
during a write. Send a 500. Then design what you found as carefully as the success screens. Protocol
in `references/failure-and-recovery.md`.

**7. Use it for an hour as a real user.**
Not a click-through — a real session with real data. Write down every point where it stops feeling
like the same product. This is the only reliable way to find coherence breaks, because people are
measurably bad at reporting friction they just experienced.

**8. Then** do the surface pass.

## Premium tells

These are the details that make people say "this feels expensive" without being able to say why.
They share a property: each one requires having actually used the thing. Treat this as a checklist
to pull from, not a mandate to ship all of it.

**Feedback and reversibility**
- Optimistic updates that roll back visibly and explain themselves when the write fails
- Undo instead of "Are you sure?" wherever undo is possible — confirmation dialogs push the cost of
  your uncertainty onto the user
- Every destructive action either reversible or genuinely confirmed, never a silent commit
- Haptic/sound on *commit*, not on tap — rewarding the outcome, not the gesture

**Continuity**
- Scroll position, filters, tabs, and half-typed input survive navigation and backgrounding
- Form state survives a validation error — never clear a form the user filled
- Deep links and refreshes land in the same place the in-app path does
- Skeletons match the final layout so content does not jump when it arrives

**Honest, specific copy**
- Exact numbers and dates over vague phrasing: "2 of 2 sessions used · renews March 1" beats
  "You've used all your sessions"
- Errors that name what happened, why, and the next action — with an escape hatch to a human
- Never show a raw error code without a human sentence next to it
- Empty states that teach the feature and offer the first action, not a shrug illustration

**Respect**
- Honors reduce-motion, dynamic type, dark mode, and safe areas without layout breaking
- Keyboard never covers the field being typed into or the button that submits
- Nothing blocks first use that could be asked for later; permissions requested in context, with
  the reason, at the moment the value is visible
- Works offline or degrades honestly, and queues writes rather than losing them
- No interstitial, upsell, or rating prompt during a task the user is mid-way through

**Performance as a feeling**
- Instant response to every tap, even if the real work is still running
- Perceived speed over measured speed: show the frame, stream the content
- No layout shift after load; no spinner for something already cached

## Common failure modes to watch for in your own work

- **Starting with the surface.** If asked to "make it premium" and the first instinct is a color
  palette, re-read the lever order. Deliver the diagnosis the user needs, not the one that is fun.
- **Design theater.** Confidently explaining a design rationale that never actually made it into
  the built interface. Research on AI design tools found roughly a quarter of stated reasoning never
  materialized, and the skipped parts were consistently the unglamorous ones — system status, undo,
  error recovery. Check that what you described is what you built.
- **Screen-by-screen tunnel vision.** Reviewing each screen in isolation while the user experiences
  screen 80 next to screen 1.
- **Stacking mechanics.** Adding streaks *and* points *and* badges *and* challenges. Engagement
  reverses past a certain feature density. See `references/motivation-design.md`.
- **Polishing a product with no edge.** If the product has no real advantage, no amount of state
  coverage creates one. Say that rather than quietly shipping polish.

## Reference map

Load what the task needs; these are written to be read independently.

- `references/state-coverage.md` — the state matrix, what each state owes the user, copy patterns
- `references/coherence.md` — finding and fixing the "80 screens that disagree" problem
- `references/failure-and-recovery.md` — the break-it protocol, recovery copy formula, turning
  failure into the moment people trust you
- `references/flow-psychology.md` — defaults, endowed progress, reciprocity, ownership, loss
  framing, anchoring — with before/after patterns
- `references/motivation-design.md` — what actually retains (winnable competition, completion
  drive, variable reward, competence feedback) vs. what is theater (points/badges/leaderboards,
  runaway streaks)
- `references/ethics-and-regulation.md` — the persuasion/manipulation line, dark-pattern red
  flags, 2026 regulatory exposure
- `references/audit-playbook.md` — audit mode: protocol, scored rubric, report format
- `references/evidence.md` — every research claim in this skill, its source, and how well
  established it is. **Read this before quoting a statistic to anyone.** Several figures come from
  the source talks and are not independently verified.

## Tooling

`scripts/state_audit.py` scans a codebase for data-fetching sites that appear to be missing
loading, error, or empty handling, and flags generic error copy and swallowed exceptions.

```bash
python3 scripts/state_audit.py --path /path/to/repo
python3 scripts/state_audit.py --path . --format json --out findings.json
```

It is a heuristic grep, not a type checker: it finds candidates fast across a large codebase, and
every hit needs a human read before it goes in a report. Use it to decide where to look, then look.
Its coverage percentage is a conversation starter, not a score to optimize.
