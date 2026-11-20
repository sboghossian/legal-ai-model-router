# Contract Review — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 4. Contract Review

**No single public benchmark isolates "contract review."** It is a *composite* skill: find the clauses
(**Info Extraction**, §2), judge risk and deviation from standard (**legal reasoning**, §3), propose redlines
(**Contract Drafting**, §1), and catch internal contradictions (**conflict detection**). Route by composing
those tables and weighting toward the sub-task that dominates the specific review.

**Derived guidance (composite, not a measured leaderboard)**
- **Extraction-heavy review** (find every clause of type X, build an obligations matrix): weight §2. **Opus 5.5** leads
  by 10 points. If cost matters, the 56.7% tier (Haiku 5.5, Opus 5, GPT-6 Astra, Qwen 3.8 Flash) is the step down.
- **Risk/deviation analysis** (is this indemnity market? what's the exposure?): weight §3A. The top nine are within
  ~3 points. **Muse Spark 1.3 Max** is the value pick if accessible; **Opus 5 / Gemini 4 Neon** are the safe picks.
- **Redline drafting** (rewrite to protect the client): weight §1. **Opus 5.5** or **Fable 5.1**, or **Muse Spark 1.3** at
  ~1/7 the cost.
- **Review as an agentic, multi-file job** (a data room, a folder of ancillaries, deliverables written back to
  docx/xlsx): weight §3B. **Gemini 4 Argon** leads HLAB, and Claude 5.5 models rank low there. Test on your own harness
  before trusting either.
- **Conflict detection across a long agreement:** no current board isolates it. *(July, historical: Opus 4.8 was the
  documented standout and GPT 5.6 Sol the worst.)* Treat conflict detection as **unmeasured on current models**. Rely on
  the §6 acceptance test, where three of seven classes *are* conflict detection.
- **Long agreements (100+ pages):** advertised context of 1M tokens is now common (Claude 5.5, Gemini 4, Kimi K3).
  Advertised is not effective. §8.2 measured a 9/9 multi-hop pass at 25k/100k/200k tokens for three 2026-09 models only.
  Past ~200K, chunk and map-reduce unless you have measured your model at that depth.
- **Acceptance test (model-agnostic):** whichever model you route, grade its output against the 7 Spellbook error classes
  (§6) on an *all-pass* basis, and auto-elevate purchase/M&A stakes to High.

---

## Spellbook — contract error base rates (the review acceptance test)

**Not a model leaderboard.** It ranks no LLMs and changes no pick. It measures the *target* of review — how
flawed human-drafted contracts are — and so it defines the acceptance test a routed model must pass and a
risk prior for setting stakes.

- **Source:** Spellbook Labs, "Humans Hallucinate Too / 60% of SEC-Filed Contracts Contain Errors" — https://spellbook.com/labs. **3,019** material-contract exhibits on EDGAR, **500+** public companies, filings **2005–2026**, analyzed with Spellbook's own Review tool. Vendor self-published: trust the *direction* (contracts are error-prone), calibrate on the exact percentages loosely.
- **The 7 error classes a reviewer must catch (verbatim):** clear drafting mistakes · internal inconsistencies · undefined terms · broken cross-references · broken definitions · ambiguities · clauses that may not work as written.
- **Base rates:** ~60% of contracts had ≥1 issue; ~3.1% high-risk overall; stable at **~1.1–1.3 issues/contract across 20 years** (AI-era drafting no cleaner); company spread 0.18→3.30.
- **Contract-type risk prior:** note purchase agreements ~15% high-risk, stock & asset purchase agreements ~12% — deal/M&A paper runs ~4–5× the baseline. Default those to **High stakes**.
- **Routing consequence:** grade the routed model's output against the 7 classes on an **all-pass** basis. Three of them (internal inconsistencies, broken cross-refs, broken definitions) *are* the conflict-detection failure mode, which no current board measures. *(July, historical: Opus 4.8 led conflict-sensitive review and GPT 5.6 Sol was the one to avoid; not re-measured on successors.)*

---

## Generalist context (why not to route off a generalist leaderboard)

- **The verticals re-rank the podium.** On the generalist Vals Index (v2.2, 2026-11-18), Claude Fable 5.2 ranks
  **#1 (71.31%)**. On the legal boards it ranks **#7 on drafting, #22 on legal research and #24 on the Legal
  Index**. Gemini 4 Neon (70.87%), Sonnet 5.5 (70.85%) and Opus 5.5 (70.14%) sit within 1.2 points of it on the
  generalist board but far apart on the legal ones. Never route a legal task off a generalist board.
- **1M-token context is now standard** (Claude 5.5, Gemini 4, Kimi K3), but advertised context is not effective
  context. §8.2 measured multi-hop recall only up to 200k tokens. Above that, measure your own model or chunk.
- **The cost floor is open-weight.** On legalbenchmarks.ai, Qwen 3.8 Flash costs $0.03/task and ties GPT-6 Astra on
  extraction, and DeepSeek V4 Flash costs $0.01/task on drafting. That matters for on-prem, privacy and
  high-volume triage. Reliability is uneven, though: Qwen 3.8 Flash meets only 49.1% of drafting criteria.
- **Scaffold ≠ model.** The split between §1–§2 and §3B is the legal version of this effect: the same Claude
  models lead single-pass work and trail agentic file work. Judge the *system* (model + harness + tools).

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
- **Long-context multi-hop is solved, and priced very differently (§8.2).** A liability cap, an overriding
  carve-out, a compounding escalator and a governing-law clause planted at four depths of one agreement, tested
  at 25k/100k/200k tokens: **every model resolved the full precedence chain at every depth** — but the
  identical answer cost **$2.01 (Astra) vs $0.15 (Luna Pro)**. Route long-document review on cost, not capability.
- **The failure mode that survives (§8.3):** a correct citation attached to a misstated rule. The acceptance
  test above assumes the reviewer checks the *proposition* against the source, not the existence of the source.

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
