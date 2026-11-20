# Changelog

All benchmark data carries a snapshot date; this log tracks data refreshes and structural changes.

## [0.5.0] — 2026-11-20

**Full data refresh.** Every third-party board was re-pulled on 2026-11-20. The canonical file is now
`data/scorecard-2026-11.md`; the old 2026-07 file was renamed rather than kept. §6 (Spellbook) and §8 (the
2026-09 first-party run) are carried over byte-for-byte. All seven skills move to 0.5.0.

- **legalbenchmarks.ai changed its method.** Since its 2026-08 cycle it runs models on an agentic harness, gives
  each two attempts per task, and counts a task only if both pass. "Task pass rate" replaces "reliability". The
  site says the new numbers are not comparable with earlier cycles, so no July figure can be diffed against a
  November one.
- **§1 Drafting:** Opus 5.5, Fable 5.1 and Meta's Muse Spark 1.3 tie at 48.4%. Muse costs $0.20/task against ~$1.50.
  **§2 Extraction:** Opus 5.5 leads at 76.7%, 10 points clear.
- **§3 rebuilt around agentic boards.** Research now ranks on **Vals Legal Research Bench** (§3A; Gemini 4 Neon
  56.25%, top nine within 2.9 points). New **§3B** covers agentic work with files through the Harvey LAB family:
  HLAB-Vals-1.1, Artificial Analysis LAB-AA v1.1 and Harvey's own baselines. **§3C** adds the Vals Legal Index.
  **Vals LegalBench is now a footnote (§3D):** its top ten sit within ~1.6 points and no longer separate models.
- **Correction:** the 2026-07 snapshot said Harvey's LAB had "no public scores yet". That was wrong. Harvey
  published baselines on 2026-05-26 (Opus 4.7 7.1%, the highest). They are now in §3B(iii).
- **The boards disagree by harness.** Claude 5.5 models lead single-pass drafting and extraction but rank
  28th–39th on HLAB-Vals-1.1. Added **caveat 9** (route on the board that matches your deployment). Why Claude
  drops on HLAB is untested, and the scorecard says so.
- **Newest ≠ best** (**caveat 10**): Fable 5.2 < Fable 5.1 on drafting, Opus 5 > Opus 5.5 on research, and
  Haiku 5.5 > Sonnet 5.5 on drafting and extraction. **Variant names are different systems** (**caveat 11**):
  Muse Spark 1.3 Max scores 55.29% on research and Muse Spark 1.3 scores 40.87%.
- **Caveat 3 rewritten:** legalbenchmarks.ai no longer names its graders. The July text named Claude Sonnet 4.6.
- **New §9 — legal-specific models as context, not picks:** OpenAI Astra for Law, Z.ai GLM-Legal, Harvey Tenet,
  and Thomson Reuters' Thomson 1.0. Each is listed with its access route and any independent score. The router
  names one as PRIMARY only when the user already has access.
- **§5 Translation:** WMT26 replaces WMT25. Claude was not entered, so the July Claude preference for
  register/tone is marked as older-model evidence. §8.3's Arabic legal-accuracy result is still scoped to Opus 5.
- **July qualitative findings retired or labelled.** "Flags contradictory instructions" (Opus 4.8), "best on
  scans" (Grok 4.5) and "flattens conditionals" (GPT 5.6 Sol) were observed on models no board still lists.
  They now appear only as *(July, historical)* and are not assumed to carry over to successors.
- **Council panels (§7) recomposed** from the new leaders, with a new agentic-file-work row.
- **Dispatcher:** "The one idea" now reads "the podium re-ranks by task *and* by harness". The guardrails gain
  the harness rule and the §9 access rule.

## [0.4.0] — 2026-09-21

*(Entry added retroactively in 0.5.0; the change shipped in commit `ce2dba5` without a CHANGELOG line.)*

- **`classify.py`** grounds the dispatcher's `CONFIDENCE:` line in a calibrated probability instead of the
  model's self-report. It returns the vertical plus `is_legal`, `is_composite`, a stakes score and an `ACTION`.
  It is optional: with no key or network it exits 2 and the dispatcher falls back to its table. The dispatcher
  gains `Bash` in `allowed-tools`; the vertical skills were unchanged.

## [0.3.0] — 2026-09-10

First **first-party measured run** on the scorecard. Adds newer models than any section here covered, and three
properties no public legal board measures. **No third-party rank changed; the §1–§7 snapshot stays 2026-07.**

- Added **§8 "First-party measured run — GPT-6 Astra vs Opus 5 vs Luna Pro (2026-09)"** to
  `data/scorecard-2026-07.md`. 41 prompts x 3 models across 20 practice areas, reasoning effort pinned to
  `medium`, quality/accuracy scored by an independent judge, **cost taken from what the provider actually
  billed** rather than estimated from tokens. Provenance is deliberately flagged as different in kind from
  §1–§5: no vendor filter, but small n and no independent reproduction.
- **§8.1 — price the answer, not the token.** GPT-6 Astra bills 2x Claude Opus 5's per-token rate and costs
  roughly *half* as much per answer, because it emits ~3.5x fewer tokens (5,201 vs 18,190). Measured cost per
  answer: Astra $0.2622 · Opus 5 $0.4566 · Luna Pro $0.0231. Added as **cross-cutting caveat 7** and folded
  into the dispatcher's Cost intake axis.
- **§8.2 — table stakes moved.** Structured output (11/11 fields), tool selection (100%, no over-triggering),
  refusal calibration (100% balanced) and rejection of obviously fabricated authorities (16/16) came back
  *identical and perfect across all three models*. They can no longer separate frontier models. Added as
  **cross-cutting caveat 8**, and the dispatcher now says so rather than routing on a solved axis.
- **§8.3 — the one axis that did separate.** On six MENA/French provisions asked in the local language,
  **Claude Opus 5 scored 6/6 legally correct against 4/6 for both OpenAI models, which failed the same two
  items.** Every error was a **correct citation attached to a misstated rule** — a failure mode a
  citation-existence checker passes. Cross-referenced into §5 (Legal Translation), whose guidance was
  previously proxy-based only; this is a direct legal-accuracy measurement pointing the same way.
- **§8.4 — consistency is not purchasable.** Five seeded repeats per prompt: **no model reproduced an
  identical answer** (similarity 0.47–0.78); Claude Opus 5 does not accept a `seed` at all, while both OpenAI
  models do. Caveat 4's "no drift/consistency testing" now cites a measurement instead of an absence.
- **§8.5 — a reasoning-effort dial is a cost lever, not a quality lever.** High effort scored *worse* than low
  (8.83/8.67 vs 9.00/8.86) for 12x the reasoning tokens and 1.5x the cost.
- **§8.6 — negative result, deliberately published.** No per-practice-area ranking is included: at 1–3 prompts
  per area the spread between models was ~0.5 points out of 20 with outright ties, which would be noise dressed
  as guidance. It sharpens rather than contradicts the bundle's thesis — the podium re-ranks **between
  verticals**, not between practice areas inside one vertical.
- Re-sliced all six `references/scorecard.md` files with the parts of §8 that bear on each vertical.
  `route-council` keeps its bespoke caveats list and gains the point that matters most to it: **both OpenAI
  models failed the same items the same way, so a same-lineage panel would have returned unanimous and wrong —
  cross-provider composition is the mechanism, not a nicety.**
- Versions: dispatcher and `route-council` → 0.3.0; the five verticals → 0.2.0.

## [0.2.0] — 2026-07-16

New capability — **council / consensus mode**. No model ranks changed; the benchmark snapshot stays **2026-07**.

- Added a sixth skill, **`route-council`**, the High-stakes escalation of a single-model route: convene the top
  **2–3 cross-provider** models, run them independently (no cross-talk), score their agreement, and either
  synthesize a consensus or escalate to a human on material disagreement — never a silent pick. Ships with its
  own `references/scorecard.md`, so it installs standalone like every vertical.
- Panels **re-rank by task**, composed from the existing scorecard leaders (drafting → Opus 4.8 + Grok 4.5 +
  Gemini 3.5 Flash; extraction → GPT 5.6 Sol + Opus 4.8 + Grok 4.5; reasoning → Fable 5 + Gemini 3.1 Pro +
  GPT-5.6 Sol; review → Opus 4.8 + GPT 5.6 Sol + Gemini 3 Flash/Fable 5; translation → Gemini + Opus + Qwen/Aya).
- Two reconciliation modes: recall-critical work takes the **union** of findings (all-pass — never vote a
  singleton away); judgment work treats **agreement as confidence** and **disagreement as escalate-to-human**.
- Output keeps the base contract and adds **CONVENED / CONSENSUS / DISSENT / RECONCILE** plus a calibrated
  CONFIDENCE (unanimous → HIGH · isolated dissent → MED · material disagreement → LOW). Confidence = model
  agreement, not correctness — the human verify step stays mandatory.
- Added **§7 "Council / Consensus Mode"** to `data/scorecard-2026-07.md` (composed picks + reconciliation rules;
  ranks no new models). `legal-ai-model-router`: added **Step 2.5** escalating High-stakes routes to the council.
  README: `route-council` in the tree + a "Council mode" section.

## [0.1.1] — 2026-07-15

Grounding update — no model ranks changed.

- Added **§6 "Contract Error Base Rates"** to `data/scorecard-2026-07.md`, sourced from the Spellbook Labs
  SEC contract-error study (3,019 filed contracts, 500+ companies, 2005–2026). It ranks no models — it defines
  the *target* of contract review — so it changes no model pick.
- `route-contract-review`: turned the study into a **7-class acceptance test** (all-pass) and a contract-type
  **risk prior** that auto-elevates purchase/M&A stakes to High; threaded into intake and the VERIFY output.
- `route-contract-drafting`: added a "draft to prevent these 7 error classes" note + VERIFY self-check.
- `legal-ai-model-router`: one grounding guardrail line. README evidence base + CHANGELOG updated.

## [0.1.0] — 2026-07-14

Initial release. Benchmark data snapshot: **2026-07**.

- Five vertical routing skills: `route-contract-drafting`, `route-info-extraction`, `route-legal-research`,
  `route-contract-review`, `route-legal-translation`.
- Top-level dispatcher skill: `legal-ai-model-router`.
- Canonical dataset `data/scorecard-2026-07.md` triangulated from legalbenchmarks.ai (Contract Drafting +
  Info Extraction), Vals AI × Stanford CodeX LegalBench (124 models), Harvey Legal Agent Benchmark,
  Wei Chen / Atticus Project (CUAD/MAUD/ACORD), WMT25 + SwiLTra-Bench + ArabLegalEval (translation), and
  generalist cross-checks (Artificial Analysis, LMArena, SWE-bench, HealthBench).
- Four-axis intake (accuracy/stakes, cost, speed, privacy/jurisdiction/language).
- AGPL-3.0.

### Known gaps
- Legal translation has no reliable public leaderboard — that vertical is directional, not benchmark-backed.
- Underlying legal benchmarks skew English / US-UK, single-turn. Non-US, non-English, multi-turn, and
  long-horizon work is under-measured.
