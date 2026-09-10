# Changelog

All benchmark data carries a snapshot date; this log tracks data refreshes and structural changes.

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
