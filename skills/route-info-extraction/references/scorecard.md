# Info Extraction — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 2. Info Extraction

**Source:** legalbenchmarks.ai — "Data Extraction", **November 2026 cycle**, 27 models. About 30 tasks is
inferred from the 3.3-point step and is not stated. Documents are sent in **native, unconverted form**, so
file-reading is part of what is tested. The rubric is the same as §1.

| Rank | Model             | Provider  | Task pass | Criteria pass | Form  | Cost/task | Latency |
|-----:|-------------------|-----------|----------:|--------------:|------:|----------:|--------:|
| 1    | Claude Opus 5.5   | Anthropic | 76.7%     | 91.1%         | 82.2% | $2.71     | 3m 03s  |
| 2    | Claude Fable 5.2  | Anthropic | 66.7%     | 89.2%         | 79.3% | $5.90     | 3m 07s  |
| 3    | Claude Fable 5.1  | Anthropic | 63.3%     | 89.9%         | 70.6% | $1.15     | 3m 51s  |
| 4    | Claude Opus 5     | Anthropic | 56.7%     | 89.2%         | 67.2% | $0.75     | 4m 02s  |
| 4    | GPT-6 Astra       | OpenAI    | 56.7%     | 88.4%         | 83.5% | $0.93     | 2m 55s  |
| 4    | Qwen 3.8 Flash    | Qwen      | 56.7%     | 85.7%         | 64.4% | $0.03     | 8m 21s  |
| 4    | Claude Haiku 5.5  | Anthropic | 56.7%     | 82.3%         | 77.4% | $0.20     | 1m 41s  |
| 4    | Qwen 3.8 Max      | Qwen      | 56.7%     | 77.6%         | 62.2% | $1.51     | 6m 21s  |
| 4    | GLM-5.3           | Z.ai      | 56.7%     | 72.4%         | 67.2% | $0.12     | 3m 31s  |
| 10   | Muse Spark 1.3    | Meta      | 53.3%     | 86.5%         | 67.4% | $0.29     | 4m 35s  |
| 10   | Gemini 4 Argon    | Google    | 53.3%     | 86.2%         | 66.5% | $0.27     | ~4m 33s |
| 10   | GPT-6.1 Sol       | OpenAI    | 53.3%     | 84.5%         | 83.0% | $0.13     | 2m 22s  |
| 10   | Grok 4.6          | xAI       | 53.3%     | 78.3%         | 69.3% | $0.45     | 4m 28s  |
| 10   | Gemini 3.8 Flash  | Google    | 53.3%     | 71.7%         | 66.7% | $0.21     | 6m 11s  |
| 17   | GPT-5.6 Sol       | OpenAI    | 46.7%     | 82.0%         | 78.9% | $0.20     | 2m 51s  |
| 20   | Claude Sonnet 5.5 | Anthropic | 40.0%     | 83.3%         | 77.6% | $0.92     | 1m 54s  |

*(11 more rows on the live board, down to 20.0%.)*

**Truths / nots**
- **Opus 5.5 is the clear extraction leader**, 10 points ahead of #2. Fable 5.2 is second but costs **$5.90/task**,
  over 2x Opus 5.5 for 10 points less.
- **A seven-way tie at 56.7% makes cost the decider.** Qwen 3.8 Flash ($0.03), GLM-5.3 ($0.12), Haiku 5.5 ($0.20)
  and Opus 5 ($0.75) all pass the same share as GPT-6 Astra ($0.93). Qwen 3.8 Flash costs ~45x less than models it
  ties, but runs slowest (8m 21s).
- **GPT-6 Astra has the best extraction Form (83.5%)**, so its output needs the least reformatting. Nearly every
  model scores lower on Form for extraction than for drafting.
- **Sonnet 5.5 is a poor extraction pick**: 40.0% at $0.92, below Haiku 5.5 at a quarter of the price.
- **Even the leader misses.** Opus 5.5 fails at least one requirement on nearly a quarter of tasks. Verify key terms
  against the source.
- *(July, historical; not re-measured.)* GPT 5.6 Sol flattened conditional answers into absolutes, and Grok 4.5 had
  the best scanned-document handling. Neither claim has been tested on a current model. If your corpus is scans,
  test on your own documents.

**Related academic anchors (Wei Chen / Atticus Project):** **CUAD** (clause extraction, 510 contracts, 41 clause
types), **MAUD** (M&A reading comprehension, 92 question types), **ACORD** (clause retrieval, 1–5 relevance).
These are the open datasets the field uses for reproducible extraction and retrieval evaluation. No update was
found in this refresh.

---

## 8. First-party measured run (2026-09) — what it changes here

**Different provenance from the sections above:** a run we executed ourselves in 2026-09 — 41 prompts x 3
models (GPT-6 Astra, Claude Opus 5, GPT-5.6 Luna Pro), reasoning effort pinned, cost taken from the actual
bill. Newer models and properties no public board covers, but small n and no independent reproduction. Trust
it on direction and mechanism; trust the third-party sections on relative rank. Full text: canonical §8.

- **Price the answer, not the token (§8.1).** GPT-6 Astra bills 2x Claude Opus 5's per-token rate and costs
  roughly *half* as much per answer, because it emits ~3.5x fewer tokens. Measured cost per answer:
  Astra **$0.2622** · Opus 5 **$0.4566** · Luna Pro **$0.0231**. A cost axis that reads a price list and stops
  there gets this backwards; reasoning tokens bill at the completion rate whether or not they are shown.
- **Table stakes moved (§8.2).** Structured output, tool selection, refusal calibration and rejection of
  obviously fabricated citations came back **identical and perfect across all three models**. They cannot
  separate frontier models any more. The live failure mode is subtler: a **correct citation attached to a
  misstated rule**, which a citation-existence check passes.
- **Structured extraction is fully commoditised (§8.2).** Strict JSON-schema extraction from a contract:
  **11/11 ground-truth fields, schema-valid, all three models.** Tool selection and arguments likewise 100%
  with no over-triggering. Route extraction on cost and latency — capability is no longer the variable.
- **Consistency (§8.4):** no model reproduced an identical answer across five seeded repeats. Pipelines that
  assume stable output across runs need a cache, not a seed.

---

## Cross-cutting caveats (bake these into every routing decision)

1. **Capability ≠ controllability** (Wei Chen, Atticus Project). A high benchmark score does not mean a model stays in scope, cites truthfully, or is safe to deploy unsupervised. Governance is a separate axis from raw performance.
2. **All-pass reality** (Harvey). A review that catches 8 of 10 risks is not 80% useful — it is materially incomplete. Route for reliability on high-stakes work, not average quality.
3. **Grading is imperfect, and less transparent than in July.** legalbenchmarks.ai's November board does **not name its graders**. The July snapshot named one LLM judge, Claude Sonnet 4.6. Vals Legal Research Bench uses an LLM judge, reported in its paper (arXiv 2610.00609) as GPT 5.4; this was not verified here. Harvey LAB-AA uses a three-judge panel that includes Claude Opus 5.5, so an Anthropic model helps grade Anthropic models. LLM-judged scores are not ground truth.
4. **Coverage is narrow.** legalbenchmarks.ai is English-only, US/UK-skewed, single-turn and private. It now runs two attempts per task, so it tests consistency a little. The Vals legal boards cover US law. WMT26 has no legal domain. **Non-US, non-English, multi-turn and civil-law work is under-measured.** The consistency gap is now measured rather than assumed — see §8.4: no frontier model reproduced an identical answer across repeats, with or without a seed.
5. **Benchmark drift & routing collapse.** Numbers here go stale monthly; and a router that always picks one dominant model has stopped routing. Re-validate when new frontier models ship.
6. **Silent quality regression.** Cost savings show up instantly on the bill; quality loss shows up days later in the work product. Gate any cost-driven downgrade behind a spot-check.
7. **Price the answer, not the token** (§8.1). Verbosity varies more between models than list price does — a model billing 2x per token can cost half as much per answer. Every `Cost/task` figure above is only comparable between models of similar output length, and reasoning tokens bill at the completion rate whether or not the reader sees them.
8. **Table stakes have moved** (§8.2). Structured output, tool selection, and rejecting obviously fabricated citations are now perfect across frontier models and cannot separate them. A routing rule or vendor claim resting on any of these is measuring a solved problem. The live failure mode is subtler: a **correct citation attached to a misstated rule** (§8.3), which a citation-existence checker passes.
9. **The boards disagree by harness, so route on the board that matches your deployment.** Claude 5.5 models lead single-pass drafting and extraction (§1–§2) and rank 28th–39th on agentic file work (§3B). If the model gets the documents in context and returns one answer, weight §1–§2. If it runs as an agent with tools, files and a long horizon, weight §3A–§3B. Why Claude drops on HLAB is **untested** (§3B).
10. **Newest ≠ best.** Fable 5.2 trails Fable 5.1 on drafting at twice the cost. Opus 5 beats Opus 5.5 on research at under a third of the cost. Haiku 5.5 beats Sonnet 5.5 on drafting and extraction. Never upgrade a route because a version number went up. Check the row.
11. **Variant names are different systems.** Muse Spark 1.3 Max scores 55.29% on Legal Research Bench and Muse Spark 1.3 scores 40.87%. Route on the exact name the board printed, and confirm that your API serves that variant.

---

## Live sources — re-check before high-stakes routing

- Contract Drafting & Info Extraction (agentic cycle, since 2026-08): https://www.legalbenchmarks.ai/leaderboard/models · method: https://www.legalbenchmarks.ai/methodology
- Agentic legal research (primary research signal): https://www.vals.ai/benchmarks/legal_research
- Agentic legal work with files (HLAB-Vals-1.1): https://www.vals.ai/benchmarks/hlab
- Composite by practice area (Vals Legal Index): https://www.vals.ai/benchmarks/legal_index
- Legal reasoning MCQ (LegalBench, saturated): https://www.vals.ai/benchmarks/legal_bench
- Harvey LAB-AA v1.1: https://artificialanalysis.ai/evaluations/harvey-lab-aa · Harvey's own results: https://www.harvey.ai/blog/legal-agent-benchmark-initial-results · task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- General MT (WMT26 Findings): https://aclanthology.org/2026.wmt-main.48.pdf
- §8 first-party run (2026-09) — harness, raw answers and per-suite scores: `legal-llm-benchmark/astra/`
  (`core_run.py`, `suites.py`, `analyse.py`); report: https://claude.ai/code/artifact/cb794fc9-b9e3-45f0-9437-8e3eccc88f7e
- Contract error base rates (SEC study): https://spellbook.com/labs
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://www.vals.ai/benchmarks/vals_index · https://artificialanalysis.ai/leaderboards/models
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-11 (boards re-pulled 2026-11-20).** If today is more than 2 months later, treat the ranks as suspect and re-pull the live boards.
