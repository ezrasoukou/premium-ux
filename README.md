# premium-ux

An open-source [Claude Code](https://claude.com/claude-code) skill for building apps that feel
premium — and for auditing shipped products to find out why they don't.

Pretty and premium were never the same thing. Anyone can now point an agent at the best design
references in existence and ship something that looks decent in a day, which means decent-looking
is the **floor**, and the floor rises for everyone at once. This skill is about the ceiling: the
accumulated weight of small decisions that only someone who actually used the product would have
made.

## What it does

**Build mode** — a loop for designing features so the unglamorous parts get designed too: state
enumeration before implementation, flow psychology applied honestly, a break-it-on-purpose pass,
and a real-user hour.

**Audit mode** — a protocol for reviewing an existing product: evidence gathering, a weighted
scorecard across six dimensions, and a prioritized Now/Next/Later plan written as observations with
consequences rather than a list of complaints.

The opinionated part is the **lever order**, which is roughly inverse to the order most teams reach
for:

| # | Lever | Weight in audit |
|---|---|---|
| 1 | State coverage — does the user always know what happened, that it's reversible, and what's next | 25% |
| 2 | Coherence — 80 screens that feel like one product | 20% |
| 3 | Failure & recovery — the moments that decide whether people trust you | 20% |
| 4 | Flow friction — defaults, progress, give-before-ask | 15% |
| 5 | Motivation engine — only if retention is the actual problem | 10% |
| 6 | Surface craft — motion, type, spacing, haptics | 10% |

Levers 1–3 are where almost all unclaimed premium value sits, because they're unglamorous and most
teams skip them. That's exactly what makes them cheap to win. Surface craft is real, but it's the
first thing a competitor matches.

## Install

**As a plugin** (recommended — gets updates):

```
/plugin marketplace add ezrasoukou/premium-ux
/plugin install premium-ux
```

**As a plain skill** — copy the skill directory into your skills folder:

```bash
# personal, available everywhere
git clone https://github.com/ezrasoukou/premium-ux
cp -r premium-ux/skills/premium-ux ~/.claude/skills/

# or per-project, checked into the repo
cp -r premium-ux/skills/premium-ux .claude/skills/
```

Works in Claude Code, and the `SKILL.md` is readable enough to paste into any other agent or use
as a human checklist.

## Usage

It triggers on its own for requests like these, or invoke it with `/premium-ux`:

- "make this feel more premium"
- "why does my app feel cheap?"
- "review my onboarding flow"
- "audit this product's UX"
- "should I add streaks to boost retention?"
- "we want to charge more but we look like everyone else"

The included scanner finds data-fetching code that looks like it never got its loading, error, or
empty states, plus generic error copy and swallowed exceptions:

```bash
python3 ~/.claude/skills/premium-ux/scripts/state_audit.py --path .
```

Zero dependencies, Python 3.8+. It's a heuristic grep that tells you where to look, not a list of
confirmed findings.

## What's inside

```
skills/premium-ux/
├── SKILL.md                         doctrine, lever order, both mode workflows, premium tells
├── references/
│   ├── state-coverage.md            the state matrix and what each state owes the user
│   ├── coherence.md                 finding and fixing the "80 screens that disagree" problem
│   ├── failure-and-recovery.md      the break-it protocol and recovery copy formula
│   ├── flow-psychology.md           defaults, endowed progress, reciprocity, ownership,
│   │                                loss framing, anchoring — with the honest/dark line on each
│   ├── motivation-design.md         what retains vs. what's theater; choosing one engine
│   ├── ethics-and-regulation.md     the persuasion/manipulation gate and 2026 legal exposure
│   ├── audit-playbook.md            audit protocol, scored rubric, report structure
│   └── evidence.md                  every claim, its source, and how much weight it can bear
├── scripts/state_audit.py           state-coverage scanner
└── assets/audit-report-template.md  fill-in audit report
```

## On the research

`references/evidence.md` sorts every claim in the skill into tiers: well-established findings with
primary citations, publicly documented product history, figures asserted in the source talks that
could not be independently verified, and single-client case studies. It also flags where the honest
answer is more complicated than the popular version — choice overload's replication problems, the
real range on loss aversion's "2×", the conditionality of the service recovery paradox.

**Read it before quoting a statistic to a client.** The patterns are strong enough that you don't
need an unverified number, and citing one is an unforced credibility error.

## Credits

Built from three talks by working designers. The synthesis, the lever ordering, the audit rubric,
the ethics gate, and the scanner are this repo's; the underlying arguments are theirs and are worth
watching in full:

- [**The Psychology of Premium Apps**](https://www.youtube.com/watch?v=8EAYZe6y3I8) — Tim Gabe.
  The commodity ceiling, design theater, and the three places premium evidence lives.
- [**I Studied 500+ Gamified Apps (Here's What Actually Works)**](https://www.youtube.com/watch?v=LXX_qOA5D8E)
  — Tim Gabe. The PBL fallacy, the S-curve, the streak trap, completion drive, competence feedback.
- [**The UX Psychology Behind Apps People Can't Stop Using**](https://www.youtube.com/watch?v=2TlIg3VokY8)
  — UX Peak. Smart defaults, endowed progress, reciprocity, the IKEA effect, loss framing, contrast.

The ethics and regulation material is a deliberate addition. Several of the most effective patterns
in these talks are one decision away from being a dark pattern, and a product that feels
manipulative doesn't feel premium — it feels like a trap with good typography.

## Contributing

Issues and pull requests welcome. The things that would help most:

- **Verified citations** for anything in Tier C of `evidence.md` — primary sources for the figures,
  or confirmation that one doesn't hold up
- **Scanner coverage** for stacks it handles thinly (Vue, Svelte, Compose, SwiftUI patterns it
  misses) and false positives it should stop reporting
- **Counterexamples** — products that score well on this rubric and still feel cheap, or vice
  versa. Those are the most useful bug reports a design skill can get

Keep `SKILL.md` under ~500 lines; depth belongs in `references/`.

## License

MIT — see [LICENSE](LICENSE).
