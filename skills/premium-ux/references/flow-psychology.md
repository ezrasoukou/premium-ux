# Flow psychology

> Lever 4. Removing effort and dead weight from the paths that matter.

Six principles, each with the before/after shape of the fix. They are most useful on signup,
onboarding, first-run, checkout, and upgrade — the paths where drop-off is measurable.

**Every one of these can be run honestly or dishonestly.** They work by exploiting real features
of human judgment, which means they work whether or not the thing being sold is good. Run each
through the gate in `ethics-and-regulation.md` before shipping. The test that matters: would the
user, told exactly what you did and why, consider it help or a trick?

---

## 1. Smart defaults

Every empty field is a decision you handed the user. Stack enough decisions and the most likely
outcome is no decision at all — they leave. This is decision fatigue, and the canonical
demonstration is the Columbia jam study: a grocery display of 24 flavors converted about 3% of
passers-by; cutting it to 6 raised purchases to roughly 30%. More choice is not better, it is
harder.

Meanwhile 70–90% of users in most products never change a default value. That is not laziness —
it is trust. A default reads as a *recommendation*: "this is what most people pick." It is one of
the most persuasive things in your interface, which is also why it carries an obligation.

- **Before:** a booking form with five empty fields and a `Search` button
- **After:** every field pre-filled with the most common choice, and the button reads
  `Search · 12 results` — the outcome is visible before the commitment

The user's job changes from "fill this out from scratch" to "scan and adjust what doesn't fit,"
which is a fundamentally easier task.

**Apply it:** pre-select the most common choice for every field. Show the consequence on the
button. Never make someone think when you already know the answer.

**The obligation:** a default is advice, so it must be advice you would give. Defaulting to the
most *profitable* option rather than the most *suitable* one is the single most common dark pattern
in commerce, and it is the fastest way to spend trust you will need later. Never default to a
paid upgrade, a data-sharing opt-in, or the expensive shipping option.

---

## 2. Endowed progress

The goal-gradient effect: the closer people feel to finishing, the faster they move. The useful
corollary is that **you choose where the starting line is.**

A Columbia car-wash study gave one group a loyalty card with 8 empty stamps and another a card with
10 stamps where 2 were already filled. Both required 8 washes. The group that started with 2 stamps
completed at nearly double the rate.

- **Before:** onboarding at `0% complete`, five empty steps. Accurate, and deflating — it says
  *you haven't started and there's a lot ahead*
- **After:** same form, same work, showing `20%` with the first step checked off. Account creation
  is counted as step one rather than treated as a separate event before the real thing begins

No extra work was done. The framing changed, and the feeling of momentum is what separates users
who finish onboarding from those who drop at the second screen. LinkedIn's profile strength meter
does this permanently — it is never at zero.

**Apply it:** never start a user at zero. Find something they have already done and count it.

**The obligation:** count something real. Crediting progress the user did not make, or showing a
bar that does not correspond to remaining work, is a lie that gets discovered at step four — and
the discovery costs more than the drop-off you prevented.

---

## 3. Reciprocity — give before you ask

Most products ask before they give. *Sign up to see your results. Create an account to continue.
Enter your email to unlock.* The user has received nothing and the product already wants something.

Blurring a finished result behind a signup wall is the clearest version: the user entered their
URL, waited for the scan, and the report is hidden behind a lock. It communicates *we are holding
your results hostage.* It is a restaurant asking for your credit card before showing you the menu —
you would walk out, and that is what users do.

- **Before:** analysis complete, results blurred, `Create an account to see your report`
- **After:** the real report, genuinely useful but not complete — the score, the top issues, what
  passed — and then: `Want the full breakdown with step-by-step fixes? Save your report.`

Reciprocity is the pull to return a favor, and Cialdini ranked it among the strongest drivers of
human behavior. Free samples have been reported to lift purchases dramatically. Costco gives away
food; Spotify gives away a month; Notion lets you use the whole product before paying. The signup
never feels like a wall because the user already has something worth coming back for.

**Apply it:** deliver real value before the first ask. The ask then lands as an upgrade rather than
a toll.

**The obligation:** the free thing has to actually be useful on its own. A sample engineered to be
useless without the paid tier is a bait-and-switch, and users read it immediately.

---

## 4. Ownership — let them build before they commit

The IKEA effect: people value what they assembled more than an identical pre-made thing, because
the labor changed its worth to them. The weaker but easier **endowment effect** needs no labor at
all — merely feeling that something is yours is enough.

- **Before:** email, password, `Sign up`. Nothing on this screen belongs to the user. They have
  created nothing and chosen nothing, so closing the tab costs nothing
- **After:** they are already building before any account exists — choosing their name, their
  title, their color, their layout. Each choice makes it more theirs. The button says `Continue`,
  not `Sign up`, because by now leaving does not feel like skipping a form, it feels like
  abandoning something they made

Duolingo is the clean example: by the time a signup screen appears you have picked a language, set
a goal, and finished your first lesson. You have ten minutes invested and you are not throwing it
away.

**Apply it:** move the account creation *after* the first unit of value, and make the pre-account
experience produce something the user authored.

**The obligation:** the work must survive the signup. If the user builds something and the account
step loses it, you have inverted the principle into a betrayal. And the product must be genuinely
abandonable — investment that exists to trap rather than to reward is a different mechanic wearing
this one's clothes.

---

## 5. Loss framing

Kahneman's Nobel-recognized work established that the pain of losing something is roughly twice as
powerful as the pleasure of gaining the equivalent. So every feature framed as a potential *gain*
is using the weaker motivator.

- **Before:** a storage upgrade screen — nice icon, feature list, `Upgrade now`, and beneath it
  the easiest escape hatch ever written: `Maybe later`. Nothing is at stake; ignoring it changes
  nothing. The screen has zero psychological weight
- **After:** the same product and goal, but it shows what the user is about to lose — their actual
  files, by name, with the date they will be deleted. The dismiss option reads `I'll risk it`

Status quo bias means people are wired to protect what they already have. To get action, make the
cost of inaction concrete.

**Apply it:** where you are asking someone to act to protect something, show what they will lose
rather than selling what they would gain.

**The obligation — read this one carefully.** This principle has the shortest distance to
manipulation of any in this file, and it is the one most likely to get you in trouble.

The line is whether **the loss is real and the timeline is true.** Files that will genuinely be
deleted on a real date, named accurately — that is informing someone of a consequence they would
want to know about, and withholding it would be the actual failure. A fabricated countdown, an
invented scarcity, a "3 people are viewing this" that is not true, or a confirm-shaming dismiss
button that mocks the user — those are deceptive practices, and in several jurisdictions they are
now enforcement targets rather than growth tactics. `I'll risk it` is honest if there is a real
risk. It is a dark pattern if there is not.

---

## 6. Contrast and anchoring

The brain evaluates every number relative to the one it just processed. Absolute judgment is rare.

- **Before:** a protection plan on its own page at `$50/month`. The user does the math — $600 a
  year — and declines
- **After:** the identical offer directly below the $1,900 laptop they just added to the cart,
  labeled `just 2.6%`. Nothing about the offer changed; everything about how it feels did. After
  processing $1,900, $50 barely registers

Restaurants put a $90 steak on the menu to make the $40 salmon look sensible. Estate agents show
the overpriced house first.

**Apply it:** never show a cost in isolation. Decide deliberately what the user sees first, because
that first number becomes the ruler they measure everything else against. The same logic applies to
plan ordering, feature comparison tables, and where you place the annual/monthly toggle.

**The obligation:** anchoring with a real, available, honestly-priced option is ordinary
merchandising. Anchoring against a "was $200" that was never charged, a decoy plan that exists only
to be rejected, or a strikethrough price with no history is false reference pricing — which is
specifically regulated in the EU, the UK, and under FTC guidance in the US.

---

## The synthesis

Users are not making the logical decisions a spec assumes. Defaults read as recommendations. The
first number sets the ruler. A gift creates a debt. Building something makes it yours. Progress
creates momentum.

Which is exactly why these need a conscience attached. Each principle amplifies whatever you point
it at — a good product or a bad one, equally well. Used to help someone reach a decision they will
be glad they made, they are craft. Used to extract a decision they would not have made informed,
they are the thing that makes a product feel cheap no matter how good it looks. Premium is partly
a feeling of being *well treated*, and no amount of visual polish survives a user realizing they
were played.
