# Changelog

All benchmark data carries a snapshot date; this log tracks data refreshes and structural changes.

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
