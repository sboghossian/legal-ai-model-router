# Legal Research & Analysis — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 3. Legal Research & Analysis

### 3A. Agentic legal research — Vals Legal Research Bench (primary routing signal)

**Source:** Vals AI — **Legal Research Bench**, updated **2026-11-18**. It evaluates agents on legal research
tasks across diverse areas of US law. **Metric:** all-pass accuracy, plus cost and duration per test.

| Rank | Model               | Provider  | All-pass | Cost/test | Duration |
|-----:|---------------------|-----------|---------:|----------:|---------:|
| 1    | Gemini 4 Neon       | Google    | 56.25%   | $7.37     | 35m40s   |
| 2    | Gemini 4 Carbon     | Google    | 55.77%   | $8.74     | 51m53s   |
| 3    | Muse Spark 1.3 Max  | Meta      | 55.29%   | $0.59     | 5m17s    |
| 4    | Claude Opus 5       | Anthropic | 55.29%   | $6.76     | 31m01s   |
| 5    | Claude Fable 5.1    | Anthropic | 55.29%   | $23.06    | 57m29s   |
| 6    | Gemini 4 Argon      | Google    | 54.81%   | $6.45     | 31m21s   |
| 7    | Astra for Law       | OpenAI    | 53.85%   | $2.75     | 16m45s   |
| 8    | Gemini 4 Hydrogen   | Google    | 53.85%   | $6.27     | 32m44s   |
| 9    | Wonder Full         | Meta      | 53.37%   | $3.60     | 27m34s   |
| 11   | Claude Opus 5.5     | Anthropic | 50.48%   | $23.61    | 1h52m    |
| 14   | GLM 5.3             | Z.ai      | 49.04%   | —         | —        |
| 17   | Claude Sonnet 5.5   | Anthropic | 48.08%   | $13.66    | 1h33m    |
| 22   | Claude Fable 5.2    | Anthropic | 46.15%   | $3.96     | 6m56s    |
| 32   | GPT-6.2 Astra       | OpenAI    | 42.79%   | $12.84    | 1h19m    |
| 34   | GLM Legal           | Z.ai      | 41.83%   | $0.05     | 39m49s   |

*(More rows on the live board. Muse Spark 1.3, the non-Max variant, is #39 at 40.87%. Do not merge it with the Max row.)*

**Truths / nots**
- **The top nine sit within 2.9 points**, so rank inside that band is noise. Pick on cost, speed and access.
- **Muse Spark 1.3 Max is the value story**: tied #3 at **$0.59 and 5 minutes**, against $6–23 and 30–60 minutes for
  the models it ties. Confirm API access before routing to it.
- **Opus 5 beats Opus 5.5 here** (55.29% vs 50.48%) at under a third of the cost and duration. Newest is not best.
- **No model clears 57% all-pass.** Agentic legal research is far from solved. Every output needs authority checking.

### 3B. Agentic legal work with files — Harvey LAB family

Harvey's **Legal Agent Benchmark (LAB)** is long-horizon legal work built from real client matters: 24 practice
areas, documents, spreadsheets and presentations, all-pass grading. **Three score sets exist, on different versions,
harnesses and metrics, and none is comparable to another.**

**(i) HLAB-Vals-1.1 — Vals, updated 2026-11-18, 43 models, 120-task holdout, task pass rate (±CI as printed).**

| Rank | Model             | Provider  | Task pass      | Cost/test |
|-----:|-------------------|-----------|---------------:|----------:|
| 1    | Gemini 4 Argon    | Google    | 27.08% ±3.74   | $10.55    |
| 2    | Muse Ember        | Meta      | 25.00% ±3.69   | $0.12     |
| 3    | Muse Spark Open   | Meta      | 25.00% ±3.60   | $13.63    |
| 4    | Wonder            | Meta      | 23.75% ±3.65   | $7.08     |
| 5    | Wonder Full       | Meta      | 23.33% ±3.55   | $5.41     |
| 8    | Gemini 4 Neon     | Google    | 19.58% ±3.31   | $5.97     |
| 9    | Grok 4.7          | xAI       | 18.33% ±3.18   | $10.75    |
| 12   | GPT-6.2 Astra     | OpenAI    | 16.25% ±3.08   | $7.33     |
| 13   | Mistral Large 4   | Mistral   | 15.83% ±3.13   | $0.73     |
| 28   | Claude Sonnet 5.5 | Anthropic | 10.42%         | $17.71    |
| 29   | Claude Opus 5.5   | Anthropic | 9.17%          | $21.81    |
| 36   | Claude Fable 5.2  | Anthropic | 5.00%          | $19.37    |
| 39   | Claude Haiku 5.5  | Anthropic | 4.17%          | $4.26     |

**(ii) Harvey LAB-AA v1.1 — Artificial Analysis, built with Harvey, 120 private tasks.** The headline is a
**hallucination-gated all-pass rate**: a task is zeroed if its deliverable contains a material hallucination checked
against the source documents. Judges are a three-model panel (GPT-6 Sol, Grok 4.7, Claude Opus 5.5). Top three as
printed: **Astra for Law 6.2 (Max) 20.8%**, GPT-6.2 Astra (Max) 15.0%, GPT-6.2 Astra (High) 13.3%. Astra for Law is
a legal-specific product (§9). This refresh did not confirm whether its run used an integrated legal search index the
others lacked. v1.1 scores are not comparable with v1.0.

**(iii) Harvey's own holdout baselines, 2026-05-26 (vendor-run, historical).** Claude Opus 4.7 7.1%, Sonnet 4.6
5.4%, Opus 4.6 4.2%, GPT-5.5 2.1%, Gemini 3.5 Flash 0.8%. These are the scores the July snapshot missed.

**Truths / nots**
- **This is the board where Claude falls.** Gemini 4 Argon and Meta's Muse/Wonder line lead. Claude 5.5 models sit at
  ranks 28–39, at the highest cost per test on the board. This is the opposite of §1–§2, where Claude leads (caveat 9).
- **Why is untested.** 🧪 Plausible causes include harness/tool-call fit, the per-test time budget, or file-format
  handling (docx/xlsx/pptx). None of these is measured here. Do not state a cause as fact.
- **Every score is low.** The best system completes about a quarter of tasks. Long-horizon legal agent work is not
  production-ready on any model.
- **Muse Ember is the cost outlier**: #2 at **$0.12/test** against $10.55 for #1.

### 3C. Composite — Vals Legal Index (context, not a routing table)

**Source:** Vals AI — **Vals Legal Index v1**, released 2026-10-23, updated **2026-11-18**, 43 models. It blends Legal
Research Bench, HLAB-Vals-1.1 (criteria pass, not task pass) and Tax Agent Bench, weighting practice areas by
**2022 US law-office revenue**. Business & Commercial carries 40.5% of the weight.

Top five: **Gemini 4 Neon 78.36%** ($6.10/test), Wonder Full 77.86% ($3.72), Gemini 4 Argon 76.78% ($6.82), Gemini
4 Carbon 75.93% ($7.20), **Muse Ember 75.69% ($0.07)**. Claude: Opus 5.5 #12 at 72.37% (**$19.94/test**), Haiku 5.5 #20
70.29%, Fable 5.2 #24 69.17%, Sonnet 5.5 #31 68.02%.

Useful for a **firm-wide default**, because it weights by where legal revenue sits. It is not useful for routing a
single task. Vals' own read is that the top is tight and the order is not settled, and that **no single model leads
every practice area.**

### 3D. Legal reasoning MCQ — Vals LegalBench (saturated; footnote only)

Vals × Stanford LegalBench, updated **2026-10-13**: Claude Fable 5 88.56%, Claude Fable 5.1 88.51%, Gemini 4 Argon
88.30%, Wonder Full 87.42%, Gemini 3.1 Pro Preview 87.40%, Gemini 3.7 Flash 87.26% (**$1.5/$7.5 per M, 2.23s**) … #10 GPT-5.6 Sol 86.97%.
**The top ten sit within ~1.6 points.** That gives no routing signal on quality. If you need fast single-turn reasoning at
volume, the board's useful information is cost and latency (Gemini 3.7 / 3.8 Flash). Claude 5.5 models were not
listed when read.

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

## 9. Legal-specific models — context, not picks

Since the July snapshot, four vendors have shipped models built or tuned for legal work. **None is a default
routing pick.** Each is gated, sold only inside its own product, or backed mainly by its maker's own numbers. The router
names one as PRIMARY **only when the user says they already have access**. Even then, choose it on the
independent scores below and not on the launch claims.

| Model | Vendor | Access *(reported)* | Independent scores (read 2026-11-20) | Vendor's own claims *(not verified)* |
|-------|--------|---------------------|---------------------------------------|---------------------------------------|
| **Astra for Law** (6.2 since 2026-11-17) | OpenAI | Trusted Access programme, or ChatGPT Enterprise on request | Vals Legal Research Bench **#7, 53.85%, $2.75/test**. Harvey LAB-AA v1.1 **#1, 20.8%** (Max). | 0.03 material hallucinations per task vs 0.59 for Claude Opus 5.5 |
| **GLM-Legal** | Z.ai | Gated beta since 2026-10-12 | Vals LegalBench **86.23%** at $0.075/$0.25 per M. Legal Research Bench **#34, 41.83%, $0.05/test**. | An HLAB score of 19.17% is reported but was not confirmed here |
| **Harvey Tenet** | Harvey | Inside Harvey only; research preview since 2026-08-20; post-trained on Kimi K3 | None | Harvey's own evaluations only |
| **Thomson 1.0** | Thomson Reuters | Inside CoCounsel only, since 2026-08 | None | TR's own evaluations only |

- **Legora** has no model of its own. **SaulLM** has had no release since 2024.
- **Read Astra for Law's scores in context.** It leads LAB-AA but ranks #7 on research. This refresh did not
  confirm whether its LAB-AA run had a legal search index that the general models lacked. Treat its lead as a lead for
  the *product*, not proof that legal tuning beats general models.
- **GLM-Legal is the cheap specialist.** It sits near the top of saturated LegalBench at very low cost, but is
  mid-table on agentic research. Use it for high-volume single-turn legal reasoning if you have beta access. Do not use it for research.

**New evaluation work to watch (all reported, none re-run here).** These are citation-hallucination benchmarks
(LegalCiteBench; LePhantomCite, arXiv 2606.21155; PARCEL), civil-law evaluations (Colombian law, arXiv 2610.03639,
where free-text correctness stays at or below 0.45; BenGER for German), and Stanford CRFM's **HELM Arabic
Enterprise** (May 2026, UAE law). None of them yet ranks enough current frontier models to drive a route.

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
