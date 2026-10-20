# Failure and recovery

> Lever 3. Where premium stops being an opinion.

## The asymmetry

Most people do not abandon a product because of its home screen. Survey data suggests roughly a
third of people will walk away after a *single* bad experience. Failure moments carry
disproportionate weight, and they are the moments teams design last or not at all.

They are also the moments where the upside is largest. The **service recovery paradox** — the
subject of a substantial 2007 review of the literature — describes an effect where a failure that
gets handled really well can leave people as satisfied as if nothing had gone wrong, sometimes
more. The failure becomes the evidence. "This went south and they caught me" is a far stronger
trust signal than a session where nothing happened, because it is a demonstration rather than a
claim.

This is the cheapest premium in the whole skill, for a structural reason: almost everyone skips it.
Getting it right requires actually using the product and breaking it, which is work that AI
tooling has been consistently bad at because it requires contact with the running system rather
than with its description.

## The break-it protocol

Set aside a session, open the product, and do these on purpose. Capture a screenshot of every
result — the screenshots are the audit findings.

**Network**
- Turn off Wi-Fi mid-flow, especially mid-submit and mid-upload
- Throttle to slow 3G and redo your core flow
- Drop the connection *during* a write and see what the UI believes afterward
- Return from offline and check whether queued work completed or vanished

**Server and data**
- Force a 500, a 403, a 404, and a timeout on your main endpoints
- Return an empty array where the UI expects items
- Return a field as `null` that the UI assumes exists
- Return 10,000 items where the UI expects 10
- Send pathological content: very long names, emoji, right-to-left text, missing images, zero and
  negative numbers, far-future and far-past dates

**Money and limits**
- Fail a payment. Then fail it *after* the charge appears to have started
- Hit every quota and limit
- Let a subscription expire; let a card expire
- Double-submit a payment and verify idempotency

**Identity and permissions**
- Expire the session mid-task
- Revoke a permission the app already had (camera, notifications, location, files)
- Deny every permission at the prompt and keep using the app
- Sign in on a second device and act on both

**Lifecycle**
- Background and kill the app mid-form, then reopen
- Rotate the device, resize the window, change system font size, enable reduce-motion
- Follow a deep link while signed out
- Refresh the browser mid-flow

Then **design every state you found as carefully as the success screens.** That sentence is the
whole lever.

## The recovery copy formula

A good failure message answers four things, in this order, in plain language:

1. **What happened** — in the user's terms, not the system's
2. **Why** — if knowing helps them act, or if not knowing will make them blame themselves
3. **What to do now** — one clear action, as a button where possible
4. **The escape hatch** — a path to a human, always, for anything involving money, data loss,
   or identity

A worked example. A crypto card client's support lead pointed out that people are trusting the app
with their own money, so they need to feel safe every time they spend or deposit. His description
of a declined transaction:

> "There's just zero information on what you should do. You're just left alone."

The question became: how do we make people feel confident in the scariest moment? What shipped was
not elaborate — when a payment is declined, an alert tells you to check your balance, with a
*contact support* button right there in the alert. That, with a few other design moves, preceded a
60% increase in new accounts and a 79% increase in money loaded onto cards.

The lesson is not the specific numbers, it is the shape: the fix was one sentence of diagnosis and
one button, placed at the exact moment of fear. Failure states are cheap to fix and expensive to
leave alone.

**Anti-patterns**
- A raw error code with no human sentence beside it
- "Something went wrong" when the system knows exactly what went wrong
- Blaming the user for a system failure, or the reverse — taking blame so vaguely that the user
  cannot tell whether to retry
- Clearing the user's input as part of showing the error
- A retry button that retries the same thing the same way with no explanation of what changed
- No way to reach a person when real money or real data is involved
- A dead end: an error screen whose only option is the back button

## Preserve, then recover

The most valuable thing a failure state can do is **not lose the user's work.** Before writing any
copy, check that the failure path preserves form input, draft content, uploaded files, scroll
position, and selection. A beautifully worded error on top of a cleared form is still a product
that just took ten minutes from someone.

Where the system can recover without asking, it should: retry idempotently with backoff, queue
writes made offline, and tell the user what it did rather than asking them to do it again.

## Delight at the bottom

In 2014 Chrome turned its offline error page into a pixel dinosaur that becomes a running game when
you press space. Four years after launch it was reportedly being played around 270 million times a
month. A pure failure became something people sought out.

This is a genuinely underrated premium driver, with two conditions attached. Delight comes **after**
information, never instead of it: a charming animation on a screen that fails to say what happened
is an insult with good art direction. And it scales with the stakes — a playful empty state is
welcome, a playful failed-payment screen is not. The worse the moment, the more the user needs
competence and the less they want personality.

Match the register to the stakes: whimsy for inconvenience, calm precision for fear.
