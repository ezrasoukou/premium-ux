# Coherence

> Lever 2. The product as one thing experienced over months, not a set of screens reviewed one at a time.

## The mismatch

Teams review products one screen at a time, each looking great in isolation as a happy-path build
or a prototype. Users experience the product as a continuous thing: the person who opens your app
daily sees screen 80 sitting right next to screen 1. Inconsistency between them is not an
aesthetic complaint, it is a tax on every session.

It is sneakier than it sounds, because **people cannot reliably report this kind of friction.**
A University of York study moved a site's navigation bar from the left side to the right partway
through a task, changing nothing else. Time on that page more than doubled, and people kept moving
more slowly on subsequent pages even after the task moved on. Asked afterward, most had noticed
the change and still believed it had not slowed them much. It had slowed them a lot.

The practical consequence: if your product has this problem, it is costing you more than your
users will say out loud and more than your analytics will show. Nobody files a ticket saying "your
spacing is inconsistent and it costs me 300ms of reorientation per screen." They just find the
product tiring and eventually leave for one that is not.

AI tooling supercharges this. When an agent can spin up a new screen in a minute, it is very easy
to end up with 80 screens that do not quite agree — each individually defensible, collectively
exhausting.

## The one-hour real-user pass

The only reliable detector. Not a click-through, not a demo script.

1. Use real data and a real account, ideally one that has been around a while
2. Do the things your users actually do, in the order they actually do them
3. Do them on the device they use, at the network speed they have
4. Write down **every** point where it stops feeling like the same product — do not fix anything yet
5. Only then look at the list and find the patterns

Write the raw list first because the value is in the *clusters*, not the individual notes. Twelve
scattered annoyances usually reduce to three systemic decisions that were never made once.

Prompts that surface breaks quickly: Where did I have to re-learn something I already knew? Where
did the same concept have two names? Where did a button move? Where did I lose my place? Where did
tone change — playful here, bureaucratic there? Where did a flow I was doing get interrupted by
something the product wanted?

## What to inventory

When the walk produces a list, turn it into a systematic sweep. These are the axes along which
products silently fragment:

**Language** — one concept, one name, everywhere. Count the words you use for the same thing
(workspace/team/org, folder/project/collection, delete/remove/archive). Pick one. Also: tone,
capitalization style, person ("you" vs "we"), date formats, number and currency formatting,
pluralization, empty-state voice.

**Navigation and structure** — where primary actions live, where back goes, whether modals or
pages are used for the same weight of task, tab persistence, breadcrumb behavior, what the logo
does.

**Interaction** — tap targets, long-press availability, swipe actions, pull-to-refresh presence,
keyboard shortcuts, focus order, whether forms submit on Enter.

**Feedback vocabulary** — how success is shown (toast? inline? screen change?), how errors are
shown, where loading indicators live, how destructive actions are guarded, whether undo exists.
Pick one pattern per job and use it everywhere. Three toast styles is worse than one mediocre one.

**Visual system** — spacing scale, corner radii, shadow levels, type scale and weights, icon
family and weight, color roles (not just palette — which color means "destructive" vs "primary"),
motion durations and easing.

**Density and rhythm** — screens that are suddenly much tighter or looser than their neighbors
read as belonging to a different app.

## Fixing it

**Consolidate to one pattern per job, then enforce it structurally.** A written guideline decays;
a shared component does not. If "how we show an error" lives in a document, it will fragment within
two months. If it lives in one `<ErrorState>` component that is the only way to render an error,
it holds. Prefer tokens over values, components over conventions, and lint rules over review
comments — the goal is to make the inconsistent thing *harder to write* than the consistent one.

**Fix the rule, not the instance.** If a screen has the wrong spacing, the finding is "we have no
spacing scale" and the fix applies everywhere. Patching the one screen guarantees you will be back.

**Let the product's edge trickle down.** This is the part that cannot be systematized away, and
it is where premium actually accumulates. If your advantage is that you understand a specific job
deeply, that understanding should show up in hundreds of small decisions — which field is
pre-filled, which number is shown by default, what the empty state suggests, what the over-limit
message says. No component library and no model hands you those, because they are downstream of
knowing something about your users that nobody else knows. That is what people end up paying more
for: a product that has clearly been thought through by someone who cared, held together by
connective tissue that agrees with itself.
