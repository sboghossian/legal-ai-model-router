# Changelog

All benchmark data carries a snapshot date; this log tracks data refreshes and structural changes.

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
