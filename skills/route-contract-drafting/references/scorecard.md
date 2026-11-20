# Contract Drafting — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 1. Contract Drafting

**Source:** legalbenchmarks.ai — "Contract Workflows", **November 2026 cycle**, 27 models. The board does not
print a task count. About 31 tasks is inferred from the 3.2-point step between pass rates, and is not stated.
**Metric:** `Task pass` is the share of tasks where every applicable lawyer-written criterion is met in **both**
of two independent attempts. `Criteria pass` is the share of individual criteria met. `Form` is binary
clarity/length/structure checks passed in both attempts. Cost and latency are **per task on an agentic
harness** (15-minute cap, fixed tool-call budget, no internet). They are not comparable to July's per-task cost.

| Rank | Model             | Provider  | Task pass | Criteria pass | Form  | Cost/task | Latency |
|-----:|-------------------|-----------|----------:|--------------:|------:|----------:|--------:|
| 1    | Claude Opus 5.5   | Anthropic | 48.4%     | 91.7%         | 93.9% | $1.47     | 3m 03s  |
| 1    | Claude Fable 5.1  | Anthropic | 48.4%     | 90.7%         | 89.7% | $1.50     | 3m 51s  |
| 1    | Muse Spark 1.3    | Meta      | 48.4%     | 87.4%         | 87.8% | $0.20     | 4m 35s  |
| 4    | Claude Opus 5     | Anthropic | 45.2%     | 90.1%         | 90.8% | $0.90     | 4m 02s  |
| 5    | Qwen 3.8 Flash    | Qwen      | 38.7%     | 49.1%         | 67.7% | $0.03     | 8m 21s  |
| 6    | Claude Haiku 5.5  | Anthropic | 35.5%     | 76.9%         | 83.1% | $0.16     | 1m 41s  |
| 7    | Claude Fable 5.2  | Anthropic | 32.3%     | 88.7%         | 90.9% | $2.98     | 3m 07s  |
| 8    | Claude Sonnet 5.5 | Anthropic | 29.0%     | 85.3%         | 91.1% | $0.98     | 1m 54s  |
| 8    | Qwen 3.8 Max      | Qwen      | 29.0%     | 32.2%         | 64.2% | $0.39     | 6m 21s  |
| 10   | GPT-6 Astra       | OpenAI    | 25.8%     | 87.1%         | 91.9% | $1.13     | 2m 55s  |
| 10   | GPT-6.1 Sol       | OpenAI    | 25.8%     | 86.3%         | 90.8% | $0.11     | 2m 22s  |
| 10   | Gemini 3.8 Flash  | Google    | 25.8%     | 65.9%         | 76.4% | $0.22     | 6m 11s  |
| 10   | Grok 4.6          | xAI       | 25.8%     | 62.2%         | 76.8% | $0.28     | 4m 28s  |
| 10   | Mistral Large 4   | Mistral   | 25.8%     | 30.6%         | 63.4% | $0.09     | 5m 11s  |
| 10   | Gemini 4 Argon    | Google    | 25.8%     | 30.5%         | 60.3% | $0.26     | ~4m 33s |
| 16   | GPT-5.6 Sol       | OpenAI    | 22.6%     | 84.8%         | 89.2% | $0.18     | 2m 51s  |
| 16   | Kimi K3           | Moonshot  | 22.6%     | 78.8%         | 84.7% | $0.26     | 2m 10s  |
| 20   | DeepSeek V4 Pro   | DeepSeek  | 19.4%     | 78.6%         | 88.3% | $0.08     | 3m 58s  |

*(9 more rows on the live board, down to 9.7%.)*

**Truths / nots**
- **Three-way tie at the top, at very different prices.** Opus 5.5 and Fable 5.1 cost ~$1.50/task. **Muse Spark
  1.3 matches them at $0.20**, which the board itself calls ~86% cheaper. **Check API access to Muse Spark 1.3
  before routing to it**; it is not confirmed here.
- **Newer is not better inside a family.** Fable 5.2 (32.3%, $2.98) scores below Fable 5.1 (48.4%, $1.50) at
  twice the cost. Haiku 5.5 (35.5%, $0.16) beats Sonnet 5.5 (29.0%, $0.98) on drafting. Route on the row, not the
  version number.
- **Polished is not finished.** GPT-6 Astra meets 87.1% of criteria and has a high Form score (91.9%), yet
  completes only about a quarter of tasks end to end. That is the board's own takeaway. One missed requirement
  fails the task, so review against the full instruction set rather than the prose. *(July, historical: GPT 5.6 Sol showed the same
  "more polished than accurate" pattern.)*
- **A high task pass can rest on narrow coverage.** Qwen 3.8 Flash ranks #5 on task pass while meeting only
  49.1% of criteria, and Gemini 4 Argon and Mistral Large 4 sit near 30% criteria pass. **Read the criteria
  column before trusting a rank.**
- **No model drafts unsupervised.** The best result still leaves more than half of workflows short of at least one
  requirement.
- *(July, historical; not re-measured on successors.)* Opus 4.8 was uniquely willing to flag contradictory
  instructions rather than draft through them, and Grok 4.5 left already-sound language untouched. No current
  board isolates conflict detection.

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
- **The reasoning-effort dial is a cost lever, not a quality lever (§8.5).** GPT-6 Astra, ten prompts per
  setting: low **9.00** quality / 8.86 accuracy at $0.157; medium 9.00 / **9.00** at $0.247; high **8.83 /
  8.67** at $0.238. **High effort scored worse than low** for 12x the reasoning tokens. Turning the dial up is
  not a substitute for routing to a better model, and leaving it at a provider default is how a model spends
  its whole token budget thinking and returns an empty answer.
- **Verbosity is the cost driver (§8.1):** 5,201 output tokens (Astra) vs 18,190 (Opus 5) for comparable
  substance. Length is not thoroughness, and it is what you pay for.

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
