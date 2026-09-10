# Legal Research & Analysis — extended notes (data as of 2026-07; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 3. Legal Research & Analysis

**Source A:** Vals AI — **LegalBench** (Stanford CodeX partnership; 124 models; updated 2026-07-09).
Measures legal *reasoning* across six task types: issue-spotting, rule-recall, rule-conclusion,
rule-application, interpretation, rhetorical understanding. **Metric:** accuracy (± CI). Cost per M tokens.

| Rank | Model                        | Provider  | Accuracy      | Cost In/Out (per M) | Latency |
|-----:|------------------------------|-----------|--------------:|--------------------:|--------:|
| 1    | Claude Fable 5               | Anthropic | 88.56% ±0.33  | $10 / $50           | 8.96s   |
| 2    | Gemini 3.1 Pro Preview (2/26)| Google    | 87.40% ±0.33  | $2 / $12            | 10.06s  |
| 3    | Gemini 3 Pro (11/25)         | Google    | 87.03% ±0.37  | $2 / $12            | 8.33s   |
| 4    | GPT-5.6 Sol                  | OpenAI    | 86.97% ±0.41  | $5 / $30            | 6.20s   |
| 5    | Gemini 3 Flash (12/25)       | Google    | 86.86% ±0.36  | $0.5 / $3           | 4.67s   |
| 6    | GPT-5.5                      | OpenAI    | 86.52% ±0.41  | $5 / $30            | 18.14s  |
| 7    | GPT-5.4 (xhigh)              | OpenAI    | 86.04% ±0.41  | $2.5 / $15          | 27.79s  |
| 8    | GPT-5                        | OpenAI    | 86.02% ±0.38  | $1.25 / $10         | 18.59s  |
| 9    | Grok 4.5                     | xAI       | 85.97% ±0.41  | $2 / $6             | 67.88s  |
| 10   | GPT-5.1                      | OpenAI    | 85.68% ±0.40  | $1.25 / $10         | 7.05s   |

*(114 more models below the top 10 on the live board.)*

**Truths / nots**
- **The top 10 sit inside ~2.9 percentage points.** On this benchmark, "which model is #1" is mostly noise — pick on cost/speed/constraints, not the leaderboard rank.
- **Gemini 3 Flash is the value story:** 86.86% at **$0.5/$3 and 4.67s** — near-top accuracy, cheapest and fastest in the top tier.
- **Fable 5** leads accuracy but is the most expensive here ($10/$50).
- **Grok 4.5** is competitive on accuracy but **catastrophically slow (67.88s)** — do not put it in an interactive research loop.
- Vals' own caveat: performance varies a lot task-to-task, and even top models mis-cite the wrong rule on FRCP-style Rule-QA. **There is still significant room for improvement for models in law.**

**Source B:** Harvey — **Legal Agent Benchmark (LAB)** (1,200+ agent tasks, 24 practice areas, 75,000+
expert rubric criteria, **all-pass grading**, built from real client matters; long-horizon agentic work).
**No public scores yet** (baselines "coming"). Use LAB as the *task-design standard* for agentic legal
research (multi-step, review-quality output), not as a scoreboard. Its predecessor **BigLaw Bench** covered
short-horizon reasoning (read a contract, answer a question).

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
- **Consistency is not purchasable (§8.4).** Three prompts, five repeats, fixed seed where accepted: **no
  model reproduced an identical answer** — Astra 0.78 mean similarity, Luna Pro 0.73, Opus 5 0.47 (Opus 5 does
  not accept a `seed`). Reproducible research output needs caching or a fixed retrieval layer above the model.
- **Non-English substance (§8.3):** Opus 5 6/6 on MENA/French provisions vs 4/6 for both OpenAI models, every
  error being a correct citation attached to a wrong rule. Verify the proposition, not the cite.
- **No per-practice-area re-ranking was detectable (§8.6)** at 1–3 prompts per area. The podium re-ranks
  between *verticals*, not between practice areas inside general legal Q&A.

---

## Cross-cutting caveats (bake these into every routing decision)

1. **Capability ≠ controllability** (Wei Chen, Atticus Project). A high benchmark score does not mean a model stays in scope, cites truthfully, or is safe to deploy unsupervised. Governance is a separate axis from raw performance.
2. **All-pass reality** (Harvey). A review that catches 8 of 10 risks is not 80% useful — it is materially incomplete. Route for reliability on high-stakes work, not average quality.
3. **Grading is imperfect.** legalbenchmarks.ai reliability is scored by a *single* LLM judge (Claude Sonnet 4.6); usefulness by a 2-judge panel (~82% agreement). Their own bias check: Sonnet tops neither board and Anthropic models rank lowest on length — evidence against self-grading favoritism, but LLM-judged scores are still not ground truth.
4. **Coverage is narrow.** legalbenchmarks.ai is English-only, US/UK-skewed, single-turn, one run per task (no drift/consistency testing), with a private task set. Vals LegalBench is multiple-choice reasoning, not drafting. **Non-US, non-English, multi-turn, and long-horizon work is under-measured.** The consistency gap is now measured rather than assumed — see §8.4: no frontier model reproduced an identical answer across repeats, with or without a seed.
5. **Benchmark drift & routing collapse.** Numbers here go stale monthly; and a router that always picks one dominant model has stopped routing. Re-validate when new frontier models ship.
6. **Silent quality regression.** Cost savings show up instantly on the bill; quality loss shows up days later in the work product. Gate any cost-driven downgrade behind a spot-check.
7. **Price the answer, not the token** (§8.1). Verbosity varies more between models than list price does — a model billing 2x per token can cost half as much per answer. Every `Cost/task` figure above is only comparable between models of similar output length, and reasoning tokens bill at the completion rate whether or not the reader sees them.
8. **Table stakes have moved** (§8.2). Structured output, tool selection, and rejecting obviously fabricated citations are now perfect across frontier models and cannot separate them. A routing rule or vendor claim resting on any of these is measuring a solved problem. The live failure mode is subtler: a **correct citation attached to a misstated rule** (§8.3), which a citation-existence checker passes.

---

## Live sources — re-check before high-stakes routing

- Contract Drafting & Info Extraction: https://www.legalbenchmarks.ai/leaderboard (+ /research/phase-2-research)
- Legal reasoning (LegalBench, 124 models, live): https://www.vals.ai/benchmarks/legal_bench
- Agentic legal task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
- §8 first-party run (2026-09) — harness, raw answers and per-suite scores: `legal-llm-benchmark/astra/`
  (`core_run.py`, `suites.py`, `analyse.py`); report: https://claude.ai/code/artifact/cb794fc9-b9e3-45f0-9437-8e3eccc88f7e
