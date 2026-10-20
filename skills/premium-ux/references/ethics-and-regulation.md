# Ethics and regulation

> The gate. Run anything from levers 4 and 5 through this before shipping it.

This is not a disclaimer section. A product that feels manipulative does not feel premium — it
feels like a trap with good typography, and users detect it faster than teams expect. The feeling
of being *well treated* is a load-bearing part of what premium means, and it is the one thing
visual polish cannot fake.

There is also a practical argument. Every mechanic in this skill works by exploiting a real feature
of human judgment, which means it works equally well whether what you are selling is good. That
symmetry is exactly why the mechanics need a conscience attached: they are not self-limiting.

## The test

**Would the user, told exactly what you did and why, consider it help or a trick?**

That single question resolves most cases. Pre-filling the most common shipping option: "we guessed
what you'd want" — help. Pre-selecting the expensive one: "we guessed what we'd want" — trick.
Showing a real deletion date: help. Inventing one: trick.

Two useful backstops when the first question is close:

- **The reversal test.** Would you be comfortable if a competitor ran this on you, and if your
  users saw the internal doc proposing it?
- **The informed-user test.** Would a user who fully understood the mechanic still make the same
  choice? If the mechanic only works on the uninformed, it is extraction, not persuasion.

## The line, principle by principle

| Mechanic | Honest version | Dark pattern |
|---|---|---|
| Smart defaults | The most *suitable* choice is pre-selected | The most *profitable* choice is pre-selected; opt-outs pre-checked |
| Endowed progress | Counts something the user genuinely did | Credits fake progress; bar does not track real remaining work |
| Reciprocity | The free thing is useful on its own | The sample is engineered to be useless without paying |
| Ownership | Work survives signup; leaving is easy | Investment exists to trap; export is blocked or data is hostage |
| Loss framing | A real loss on a true timeline | Fabricated urgency, fake scarcity, confirm-shaming |
| Anchoring | Real, available, honestly-priced reference | "Was $200" never charged; decoys that exist only to be rejected |
| Streaks | Pausable, repairable, user-chosen goal | Cannot pause, influence, or escape |
| Variable reward | Variability over genuinely valuable outcomes | Manufactured variability driving spend; loot-box mechanics |
| Competition | Winnable cohorts, cheap acknowledgement | Global ranking that tells most users they lose |
| Notifications | Triggered by something that happened | Manufactured to re-engage, timed to exploit idle moments |

## Red flags in your own designs

Any of these means stop and reconsider, not "add a disclosure":

- A countdown timer that resets, or that is not tied to a real deadline
- Social proof that is not literally true ("12 people are viewing this")
- A dismiss button written to shame ("No thanks, I don't care about my data")
- Cancellation that is meaningfully harder than signup
- A free trial whose end date and charge amount are not stated plainly before the card is taken
- Any pre-checked consent, especially for marketing or data sharing
- Interface weight deliberately unequal between the two options (the one you want is a button, the
  other is faint 11px text)
- A mechanic whose internal justification is a behavioral metric with no corresponding user benefit
- Anything you would describe differently to a user than you do in a planning doc

That last one is the most reliable detector of all.

## The 2026 regulatory picture

Design choices that were growth tactics a few years ago are now enforcement surface. Treat this as
orientation rather than legal advice — if you are shipping any of this at scale, get counsel.

- **EU Digital Fairness Act** — heading toward a legislative proposal in late 2026, explicitly
  aimed at dark patterns, addictive design, and specifically addictive streak mechanics. This is
  the one that changes the calculus on engagement mechanics in Europe.
- **EU Digital Services Act** — already in force; prohibits dark patterns in interface design for
  in-scope services.
- **EU Consumer Rights / Unfair Commercial Practices Directive** — governs false reference pricing;
  "was $200" needs to have actually been $200.
- **GDPR / ePrivacy** — consent must be freely given and unbundled; pre-checked boxes and
  cookie-banner asymmetry are established violations.
- **US FTC** — active enforcement on negative-option billing and subscription cancellation
  ("click to cancel" style rules), deceptive reference pricing, and fake reviews and testimonials.
- **US state law** — California, Colorado, and Connecticut privacy statutes name dark patterns as
  invalidating consent. The 2024 Nevada Attorney General litigation involving Snapchat is a
  concrete signal that addictive mechanics aimed at minors carry real exposure.
- **Loot-box and virtual-currency rules** — regulated or restricted in Belgium, the Netherlands,
  and under scrutiny elsewhere; disclosure requirements are tightening broadly.
- **Minors** — UK Age Appropriate Design Code, the EU's work on minors, and various US state laws
  impose substantially stricter duties. If minors can use your product, assume the strictest reading
  of everything above.

## When asked to build something over the line

Say so once, plainly, with the specific concern and the regulatory exposure if relevant — then
offer the honest version of the same mechanic, which usually exists and usually performs nearly as
well. "Fake countdown" has an honest sibling in "real deadline, clearly stated." "Pre-checked
upsell" has one in "clearly recommended upsell with the reason given."

If the user considers it and still wants it, that is their call to make about their product; note it
and move on without relitigating. The exception is the narrow band where it is not a judgment call —
fabricated reviews, undisclosed charges, consent you did not actually obtain. Those are not
aggressive design, they are the kind of thing that ends companies, and declining to build them is
the right answer.
