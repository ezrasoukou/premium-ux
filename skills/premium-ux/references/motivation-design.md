# Motivation design

> Lever 5. Durable reasons to come back — and the mechanics that only look like reasons.

Reach for this lever only when **retention** is the actual problem. If the product's issue is that
people cannot tell what happened when they tapped a button, gamification will not help; it will add
a second thing to be confused by. Levers 1–3 first.

The headline finding across the research: the three mechanics every app adds first — points,
badges, leaderboards — are also the three most documented failures in product history. Meanwhile
Strava reached ~180 million registered users without a conventional badge in sight, and Apple drove
a ~49.5% behavior change in a 160,000-person study using one idea.

## What fails

### The PBL fallacy

Points, badges, and leaderboards are the default reach, and the record is bad:

- **LinkedIn** quietly retired its Community Top Voice gold badges in 2024. The internal read was
  that badge-motivated users produced quantity over quality — chasing the badge rather than sharing
  expertise.
- **Foursquare** scrapped mayorships and badges in 2014 after data showed gamification drove
  check-ins but not the discovery behavior the business actually needed.
- **Google News** killed its badge system for the same reason.

Yu-kai Chou's framing is the one to remember: **PBL is the scoreboard of a game, not the game
itself.** You would not walk into a baseball stadium, look at the scoreboard, and feel motivated to
play baseball. Most apps build the scoreboard and forget to build the game.

The diagnostic question: *if you removed the points tomorrow, would anyone still want to do the
underlying activity?* If no, the points are not motivating the behavior — they are substituting for
a reason to do it, and they will stop working as soon as novelty fades.

Note what each failure above has in common: the mechanic successfully drove a *measurable proxy*
while the behavior the business actually needed got worse. That is the signature failure mode, and
it is invisible if you only watch engagement.

### The S-curve: more mechanics reverse engagement

A 2025 peer-reviewed study in *Frontiers in Psychology* found gamification feature richness follows
an S-shaped curve. Adding features helps engagement — up to a point. **Past that point, more
features actively reverse it.**

The empirical case is Habitica, probably the most aggressively gamified productivity app ever
built: tasks are quests, habits are character stats, missing a task damages your HP. A peer-reviewed
study found that *100% of participants* experienced counterproductive effects — users got so
absorbed managing the game layer that the actual productive behavior got buried. This is cognitive
overload wearing engagement's costume.

If you are stacking streaks *plus* points *plus* badges *plus* challenges *plus* leaderboards, the
data says you are past the peak, not climbing it. The instinct when a mechanic underperforms is to
add another one. The correct move is usually to remove four and make one excellent.

### The streak trap

Research from the Decision Lab found that streaks shift from **motivational to obligational** the
longer they run. Users move from *I want to do this* to *I can't miss today.* The mechanic stops
being a reward and becomes a debt — and debts get defaulted on, loudly, usually taking the user
with them.

Snapchat is the canonical case. A 2023 Belgian study of nearly 2,500 adolescents found streak
frequency correlated with FOMO, problematic smartphone use, and reduced self-control around social
media. In 2024 the Nevada Attorney General filed litigation involving Snapchat. The EU's Digital
Fairness Act, heading toward a legislative proposal in late 2026, specifically targets addictive
streak mechanics.

So: if you ship a streak in 2026, know that the longer it runs the more it shifts toward
obligation, and that you are shipping into a space regulators are now actively watching.

**Streaks are not universally bad** — Duolingo has run hundreds of experiments on theirs and the
shipped version demonstrably retains users. Notice *how* they ship it: users choose their own goal
level, and they can buy a streak freeze. The mechanic is **wrapped in agency.** The design
researchers are flagging is the streak you cannot pause, cannot influence, and cannot escape.

If you ship one, ship the agency with it: a pause, a rest day, a repairable break, and a graceful
story for the day it ends — because it will end, and that moment determines whether the user
re-engages or uninstalls.

---

## What works

### Winnable micro-competition

Strava: ~180 million registered users, and an engagement ratio that is genuinely unusual — users
average about **1 hour of real-world activity per 2 minutes spent in the app.** That is not a
retention metric, it is closer to an influence metric. The app's success is measured in behavior
*outside* itself.

The mechanism doing most of the work is **segments** — any user-defined stretch of road or trail.
Run it and your time lands on a leaderboard sorted by age and gender cohort. That sounds like a
leaderboard, which this file just told you is broken. The difference is decisive: Strava did not
build one global leaderboard, it built **thousands of hyper-local micro-competitions.** The hill on
your morning route. The segment outside your office.

These competitions are *winnable*, and winnability is the strongest predictor of competitive
motivation (confirmed in a 2022 ScienceDirect study). A global leaderboard tells 99.9% of your
users they are losing; a local one tells almost everyone they have a shot. Social acknowledgement
compounds it — Strava's kudos measurably increase future run frequency, clubs grew 59% in 2024, and
the platform handed out 14 billion kudos in 2025.

**The design rule: engineer the size of the competition rather than inflating empty metrics.** Make
the pool small enough that winning is plausible — by geography, cohort, time window, team, or skill
band.

### Completion drive

The most underrated pattern in consumer tech, and the one to reach for first.

Apple Watch's activity rings: three rings (move, exercise, stand), close all three to complete your
day. One principle from cognitive psychology does the work — the **Gestalt principle of closure**.
The brain is wired to perceive an incomplete pattern as demanding completion. A 90%-filled circle
is an open loop, and the brain wants to close it.

Reported results: ~49.5% behavior change across 160,000 people, and users who regularly close
rings being 48% less likely to report poor sleep quality. The mechanic produces **real-world
positive outcomes**, not engagement theater — the ring closing means you actually moved.

The engine is *anticipation toward closure*, which is structurally different from a streak's *fear
of loss*. A closed ring is a complete thing; a broken streak is a loss. One resets cleanly every
day with no accumulated debt, which is precisely why it does not collapse at day 31.

If you can choose which lever your product runs on, **completion drive is the strongest default.**
Requirements: a visibly incomplete representation, a clearly defined "done," a cycle short enough
to complete reliably (daily usually), and — critically — completion that maps to something the user
genuinely wanted to accomplish.

### Variable reward magnitude

The gap between *knowing* a reward is coming and not knowing *how big* it is. Anticipation, not
loss aversion.

The pack-opening flow in the card game Gameblazers is the clean illustration, in three stages:

1. **Anticipation** — you tap a pack with no idea what is inside. Could be junk, could be the rare
   you have chased for weeks
2. **Reveal** — cards flip *one at a time.* Each card resets the anticipation cycle. Same data, but
   one moment becomes five
3. **Celebration** — a rare hits and the screen reacts: glow, motion, haptics

That staging is why you tap the next pack. Note that stage 2 creates value out of *pacing alone* —
the same information delivered at once is a list; delivered sequentially it is an experience. This
generalizes well beyond games: results revealing progressively, an analysis that streams its
findings, a report that builds.

Compare the emotional engines: **streaks run on fear of losing what you built; variable rewards run
on the pull toward what is next.** Same surface behavior, opposite machinery. One burns out, the
other recharges itself.

Use with care — this is also the mechanism underneath loot boxes and slot machines. The honest
version attaches variability to something with real underlying value (you genuinely wanted the
cards, the insight, the match). The dishonest version manufactures variability to drive
compulsion toward spending. See `ethics-and-regulation.md`; several jurisdictions now regulate
loot-box mechanics directly.

### Competence feedback over badge theater

The most important finding for anyone building for the long term. A 2024 Springer Nature
meta-analysis found that gamification reliably improves users' sense of **autonomy** and
**relatedness** — but has *minimal* impact on **competence**, which is the psychological need most
tied to durable intrinsic motivation.

So most apps engineer recognition and forget to engineer mastery. That is the actual reason PBL
fails: a badge says *you did a thing*, which stops mattering. Competence feedback says *you got
better at a thing*, which compounds.

Peloton is the clean counterexample. Members using the social and output features work out ~15%
more frequently, but the mechanism is not competition, it is competence feedback: output measured
in real time, personal records auto-flagged, and a 100-ride badge that means something precisely
because it represents 100 actual rides. That is not theater, it is evidence of skill development.
Chess.com runs the same play with ELO. Garmin does it with training readiness and body battery.

**The rule: build mechanics that signal the user got better at the actual thing, not mechanics that
signal they opened the app a lot.**

Ask of every mechanic: *does this tell the user something true about their own capability?* If yes,
it will still work in year three. If it only tells them they showed up, it will not.

---

## Choosing an engine

Pick **one** primary engine and build it properly. Stacking is the S-curve failure.

| If the product is about… | Use | Shape |
|---|---|---|
| A daily behavior with a natural "done" | Completion drive | Visible open loop, daily cycle, real-world outcome |
| A skill that improves measurably | Competence feedback | Real-time output, auto-flagged PRs, honest rating |
| An activity with a social dimension | Winnable micro-competition | Small cohorts, local pools, cheap acknowledgement |
| Discovery or collection with real value | Variable reward magnitude | Staged reveal, paced, honest underlying value |
| A habit the user explicitly wants to hold | Streak **with agency** | Chosen goal, freezes, rest days, graceful break |

Then validate against the two questions that catch most mistakes:

1. **Would anyone still do the underlying activity if the mechanic vanished?** If no, build the
   game, not the scoreboard.
2. **Does the metric the mechanic drives match the behavior the business actually needs?** LinkedIn,
   Foursquare, and Google News all failed this one — the mechanic worked and the business got worse.
