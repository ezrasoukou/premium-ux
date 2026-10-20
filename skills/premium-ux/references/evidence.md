# Evidence

Every research claim this skill makes, where it comes from, and how much weight it can bear.

**Read this before quoting a number to a client, in a deck, or in a public post.** This skill was
built from three talks by working designers (credited in the repo README). Their arguments are
sound and the patterns hold up, but a talk compresses citations, and several figures repeated here
could not be independently verified while writing. Citing an unverified statistic to a client is
exactly the kind of unforced error that costs credibility — the patterns are strong enough that
you do not need to.

The practical rule: **argue the mechanism, cite the number only if you checked it.** "Failure
states are where trust is won, and most teams skip them" needs no citation. "Error recovery lifts
retention 79%" needs a verified source.

---

## Tier A — well-established findings

Safe to rely on, with the nuances noted. Primary sources given so you can cite the research rather
than a video about the research.

| Claim | Source | Note |
|---|---|---|
| Choice overload: 24 jams → ~3% purchase, 6 jams → ~30% | Iyengar & Lepper, 2000, *J. Personality & Social Psych.* | Famous but **contested** — see Contested below |
| Endowed progress: 10-stamp card with 2 pre-filled beat 8-stamp card | Nunes & Drèze, 2006, *J. Consumer Research* | Solid; the car-wash study is real |
| Goal-gradient effect: effort increases near a goal | Hull, 1932; Kivetz, Urminsky & Zheng, 2006 | Well replicated |
| Reciprocity as a primary driver of compliance | Cialdini, *Influence* (1984) | Robust across many studies |
| IKEA effect: self-assembly raises valuation | Norton, Mochon & Ariely, 2012, *J. Consumer Psych.* | Replicated |
| Endowment effect: ownership raises valuation | Kahneman, Knetsch & Thaler, 1990; Thaler, 1980 | Robust |
| Loss aversion: losses loom larger than gains | Kahneman & Tversky, 1979 (prospect theory); Nobel 2002 | Robust; the **"2×" multiplier is approximate** — see Contested |
| Status quo bias | Samuelson & Zeckhauser, 1988 | Well established |
| Anchoring and contrast effects on judgment | Tversky & Kahneman, 1974 | Among the most replicated effects in the field |
| Gestalt principle of closure | Classical Gestalt psychology (Wertheimer and after) | Established perceptual principle |
| Processing fluency: easier-to-process things are judged more favorably | Reber, Winkielman & Schwarz, 1998; Alter & Oppenheimer, 2009 (review) | Well supported |
| Autonomy, competence, relatedness as core motivational needs | Deci & Ryan, self-determination theory | The standard framework |
| Visibility of system status as a usability heuristic | Nielsen, 1994 | Foundational |
| ~32% of customers would leave a brand they love after one bad experience | PwC, *Experience Is Everything*, 2018 | This is the likely source of the "one bad experience" figure; verify the exact wording |

## Tier B — publicly documented product history

These happened and are reported in public sources. Verify current figures before quoting, since
user counts and company numbers age fast.

| Claim | Status |
|---|---|
| LinkedIn retired Community Top Voice gold badges (2024) | Publicly reported |
| Foursquare removed mayorships and badges (2014) | Publicly reported, tied to the Swarm split |
| Google News discontinued its badge system | Publicly reported |
| Chrome's offline T-Rex game, ~270M plays/month | Google-reported figure circa 2018 |
| Duolingo offers streak freezes and user-chosen goal levels | Observable in the product |
| Apple Watch activity rings are built on closure of three daily loops | Observable; the mechanic is as described |
| Strava segments produce cohort-scoped local leaderboards | Observable; the mechanic is as described |
| Peloton surfaces real-time output and auto-flags personal records | Observable |
| Chess.com uses ELO; Garmin uses training readiness / body battery | Observable |
| EU Digital Services Act prohibits dark patterns for in-scope services | In force |
| EU Digital Fairness Act targets dark patterns and addictive design | Real initiative in progress; **verify its current stage** before citing dates |
| Nevada Attorney General litigation involving Snapchat (2024) | Publicly reported |
| Loot-box restrictions in Belgium and the Netherlands | Publicly documented |
| US FTC enforcement on negative-option billing and deceptive pricing | Active and public |

## Tier C — asserted in the source talks, not independently verified

**Do not present these as established fact.** They are plausible and the arguments they support
stand without them. If one is load-bearing for a decision or a pitch, go find the primary source
first.

| Claim | Why it needs checking |
|---|---|
| Researchers gave identical design tasks to five AI building tools in mid-2026; ~25% of stated design reasoning never reached the interface; the gap named "design theater" | Could not locate the study. The *pattern* — scaffolded UIs missing status, undo, and recovery — is independently obvious from using the tools, so argue that directly |
| University of York (2009): moving a nav bar mid-task more than doubled time on page, with carryover and underreporting | Could not verify specifics. Consistency research broadly supports the direction; the exact figures need the paper |
| Packaging studies (2010, 2021) distinguishing "gets picked" from "called premium" | Could not locate. The premium/pretty distinction is sound on its own |
| 2007 review establishing the service recovery paradox | Likely de Matos, Henrique & Rossi (2007) meta-analysis in *J. Service Research*. The effect is real but **conditional** — see Contested |
| Apple Watch: ~49.5% behavior change across 160,000 people | Specific figure, source unverified |
| Ring-closers ~48% less likely to report poor sleep quality | Specific figure, source unverified; correlational in any case |
| Strava: ~180M registered users; ~1h activity per 2 min in app; clubs +59% in 2024; 14B kudos in 2025 | Company-reported marketing figures; verify against the current Year in Sport report |
| 2022 ScienceDirect study establishing winnability as the strongest predictor of competitive motivation | Could not verify the specific study |
| 2025 *Frontiers in Psychology* study finding an S-shaped gamification richness curve | Could not verify |
| Habitica study in which 100% of participants experienced counterproductive effects | A 100% result implies a very small sample. Find the paper and check n before citing |
| 2024 Springer Nature meta-analysis: gamification improves autonomy and relatedness but not competence | Plausible and consistent with SDT literature; verify the specific paper |
| Decision Lab research on streaks shifting from motivational to obligational | Industry research; verify |
| 2023 Belgian study of ~2,500 adolescents linking streak frequency to FOMO and problematic use | Likely real; verify the citation |
| Peloton: social/output users work out ~15% more frequently | Company-reported; verify |
| 70–90% of users never change default values | Widely repeated, rarely sourced. Directionally right, treat as folklore |
| Free samples increasing purchases "up to 2,000%" | Circulated figure with dubious provenance. Do not cite |
| Kudos measurably increase future run frequency | Plausible; verify |

## Tier D — agency case studies from the source talks

First-hand client work described by the speakers. Useful as illustration, not as evidence — n=1,
self-reported, and with no public write-up to check.

- **Undertone** (audio app): mic test ending in "too short to count as a session" with nothing to
  show; two separate generic over-limit screens consolidated into one specific pattern with a
  count and a renewal date
- **Crypto card client**: declined-payment alert with a balance prompt and an inline contact-support
  button; reported +60% new accounts and +79% in money loaded onto cards, attributed to this plus
  "a few other design moves"
- **Gameblazers**: three-stage pack-opening flow (anticipation → staged reveal → celebration)

Both numeric claims are attributed to bundled changes, so they cannot be assigned to any single
design decision. Use them as narrative illustration of a shape that works — never as effect sizes.

## Contested and nuanced

Where the honest answer is more complicated than the talks suggest. Knowing these makes you more
credible, not less — and the first two are the kind of thing a sharp client will raise.

**Choice overload (the jam study).** The original result is real, but subsequent meta-analyses
(notably Scheibehenne, Greifeneder & Todd, 2010) found the aggregate effect near zero and highly
dependent on moderators — expertise, preference clarity, time pressure, and how the options are
organized. The practical lesson survives intact: *reduce the number of decisions you hand someone
in a flow, and structure the ones that remain.* The dramatic 3%-vs-30% framing does not generalize.
Lead with the mechanism rather than the number.

**Loss aversion magnitude.** The direction is robust; the oft-quoted "exactly twice" is a
convenient rounding of coefficients that vary roughly 1.5–2.5 by domain, and the effect's
universality has been actively debated (e.g. Gal & Rucker, 2018). "Losses weigh more than
equivalent gains" is safe. "Precisely 2×" is not.

**Service recovery paradox.** Meta-analytic work finds it is *not* reliable across contexts — it
depends on failure severity, whether it is a first failure, and attribution of blame. Recovery
reliably reduces damage; it does not reliably leave customers *better off* than if nothing had gone
wrong. Design excellent recovery because failures are inevitable and trust is recoverable, not
because failing is a growth strategy.

**Gamification effect sizes generally.** Heavily moderated by context, population, and duration,
with substantial publication bias and a well-documented novelty decay — many positive effects
shrink or reverse over months. Short-horizon gamification studies should be read with that in mind,
which is a large part of why `motivation-design.md` pushes toward competence feedback and
completion drive over extrinsic scorekeeping.

**AI design tool capability.** Any specific claim about what current tools do or do not produce
dates quickly. The structural argument is the durable one and does not depend on a benchmark:
whatever tooling learns becomes available to every competitor at once, so it raises the floor
rather than creating an advantage.
