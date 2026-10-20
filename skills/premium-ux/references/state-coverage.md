# State coverage

> Lever 1. The highest-leverage and least glamorous premium work.

## Why this is lever one

Every moment a user spends wondering *did that work?* or *can I get back?* is cognitive work your
product charged them for. The brain judges what is easy to take in more kindly — a well-replicated
effect usually called processing fluency — so a product that resolves every question before it
forms is literally perceived as better, not just more convenient.

The inverse is the common case. A real example: an audio app let you test your microphone, and
when you hit stop it told you the clip was too short to count as a session. No playback, no
result, nothing to show for it. One founder's summary of how that felt to their users:

> "I was expecting anything instead of nothing. That right there is where we lose them."

Nothing was broken. The feature worked as specified. The product still leaked users, because the
state at the end of that interaction was *absence*, and absence reads as failure.

Research on AI design tools found that roughly a quarter of the design reasoning the tools stated
confidently never made it into the generated interface — and the omissions clustered hard on
exactly this: system status, undo, error recovery. The gap has a name, **design theater**. It
means scaffolded products are systematically born missing their states, and that the gap is
reliably where unclaimed premium value sits.

## The three questions

Walk your core flow and check, at every single step, that the user knows:

1. **What just happened** — the system never leaves an action unacknowledged
2. **That they can take it back** — or that they were told clearly before it became permanent
3. **What to do next** — no dead ends, including on success

Most state failures are one of these three missing. If you do nothing else from this skill, do
this walk. It takes an hour and it is the difference between a product that feels thrown together
and one that feels tended.

## The state matrix

For every surface that touches data, enumerate these before building. Not all apply to every
surface — the point is to decide deliberately rather than discover later.

| State | What it owes the user |
|---|---|
| **First-run** | What this screen is for, and the single first action worth taking |
| **Empty (never had data)** | Teach the feature; offer the first action. Not a shrug illustration |
| **Empty (had data, now none)** | Make clear it is *cleared*, not *broken*; offer undo if deletion caused it |
| **Loading (first)** | Skeleton matching the real layout, so nothing jumps when content lands |
| **Loading (refresh)** | Keep existing content visible; show refresh subtly. Never blank out good data |
| **Partial / streaming** | Show what has arrived; make clear more is coming |
| **Success** | Confirm what happened, in specifics, and offer the next step |
| **Error (recoverable)** | What happened, why, what to do, retry — plus a path to a human |
| **Error (unrecoverable)** | Honest statement, preserved user input, escape route |
| **Offline** | Which features still work; queue writes rather than losing them |
| **Stale** | Say when the data is from, rather than silently showing old numbers as current |
| **Unauthorized / permission denied** | Why it is blocked and exactly how to unblock it |
| **Expired / over-limit** | The count, the limit, and the exact date or action that resets it |
| **Destructive confirm** | Prefer undo. If confirming, name the specific consequence |
| **Undo window** | Visible, reachable, and long enough to notice the mistake |
| **Rate limited / queued** | Position or wait time, not a dead spinner |
| **Validation error** | Inline, next to the field, written in terms of what to do, input preserved |
| **Search: no results** | Echo the query, suggest a relaxation, offer a reset |

A component that accepts `data` but has no shape for loading, error, and empty is not finished.
Treating those three as part of the component's contract — rather than something the consumer
handles — is what keeps coverage from decaying as the app grows.

## Copy patterns

Specificity is the cheapest premium signal there is, and vagueness is the most common tell of a
product nobody lived in.

**Over-limit.** The same app above sent users who ran out of sessions to one of two different
screens, both saying "You've used all your sessions." No count. No date. The fix was not visual:

- Before: `You've used all your sessions`
- After: a `2 of 2 sessions used` badge + `You've used both sessions this month` + `Renews March 1`

That is a line of copy and a small badge. At scale it is the difference between a product that
feels like it is tracking your account and one that feels like it is guessing.

**The pattern generalizes.** Replace every vague state string with the specifics the system
already knows:

| Vague | Specific |
|---|---|
| Something went wrong | Couldn't save your note — you're offline. We'll retry automatically. |
| Upload failed | `report.pdf` is 24 MB; the limit is 10 MB. |
| Session expired | You were signed out after 30 days. Sign in to pick up where you left off. |
| No results | Nothing matches "wireless hedaphones". Try "headphones"? |
| Processing… | Transcribing 12 of 48 minutes — about 2 minutes left. |
| Limit reached | 5 of 5 projects used. Archive one, or upgrade for unlimited. |

If a message could be pasted into any other app without editing, it is not carrying information.

## How to verify coverage

**In the running product.** For each surface: load it with no data, with one item, with a
realistic amount, with a pathological amount (long names, missing images, huge numbers, right-to-left
text), while offline, while rate limited, and while signed out. Most of these take seconds with
dev tools and reveal more than a code read.

**In the codebase.** `scripts/state_audit.py` finds data-fetching sites missing loading/error/empty
branches, generic error strings, and swallowed exceptions. It is a fast way to decide where to
look, but every hit needs a human read — heuristics flag components that legitimately delegate
state to a parent.

## The durability argument

AI tooling will get better at generating these states; that is a safe prediction. But whatever a
tool learns, every competitor gets at the same time, so it becomes the new floor, not an advantage.
What stays yours is thinking through every state *for your specific users and their specific job* —
the over-limit message that names the renewal date because you know that is the question that
drives your support tickets. That reasoning does not generalize into a model's weights, which is
precisely why it keeps its value.
