# Contract Review — extended notes (data as of 2026-07; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 4. Contract Review

**No single public benchmark isolates "contract review."** It is a *composite* skill = find the clauses
(**Info Extraction**, §2) + judge risk/deviation from standard (**legal reasoning**, §3) + propose redlines
(**Contract Drafting**, §1) + catch internal contradictions (**conflict detection**). Route by composing
those three tables and weighting toward the sub-task that dominates the specific review.

**Derived guidance (composite, not a measured leaderboard)**
- **Extraction-heavy review** (find every clause of type X, build an obligations matrix): weight §2 → **GPT 5.6 Sol** leads, but **verify conditionals** (it flattens them) and **Opus 4.8** if you need the safer, more dependable read.
- **Risk/deviation analysis** (is this indemnity market? what's the exposure?): weight §3 → top cluster is a wash on accuracy; pick **Gemini 3 Flash** for cost/speed or **Fable 5 / Opus 4.8** for the safest reasoning.
- **Redline drafting** (rewrite to protect the client): weight §1 → **Opus 4.8** (best drafter *and* best at flagging contradictions) or **Grok 4.5** (leaves sound language alone, cheaper).
- **Conflict detection across a long agreement**: **Opus 4.8** is the documented standout; **avoid GPT 5.6 Sol** (worst at silently drafting through contradictions).
- **Long agreements (100+ pages):** advertised context ≠ effective context. Only **Gemini 3 Deep Think** holds quality near 1M tokens; most models degrade past ~200–400K. Chunk + map-reduce for the rest.

## Spellbook — contract error base rates (the review acceptance test)

**Not a model leaderboard.** It ranks no LLMs and changes no pick. It measures the *target* of review — how
flawed human-drafted contracts are — and so it defines the acceptance test a routed model must pass and a
risk prior for setting stakes.

- **Source:** Spellbook Labs, "Humans Hallucinate Too / 60% of SEC-Filed Contracts Contain Errors" — https://spellbook.com/labs. **3,019** material-contract exhibits on EDGAR, **500+** public companies, filings **2005–2026**, analyzed with Spellbook's own Review tool. Vendor self-published: trust the *direction* (contracts are error-prone), calibrate on the exact percentages loosely.
- **The 7 error classes a reviewer must catch (verbatim):** clear drafting mistakes · internal inconsistencies · undefined terms · broken cross-references · broken definitions · ambiguities · clauses that may not work as written.
- **Base rates:** ~60% of contracts had ≥1 issue; ~3.1% high-risk overall; stable at **~1.1–1.3 issues/contract across 20 years** (AI-era drafting no cleaner); company spread 0.18→3.30.
- **Contract-type risk prior:** note purchase agreements ~15% high-risk, stock & asset purchase agreements ~12% — deal/M&A paper runs ~4–5× the baseline. Default those to **High stakes**.
- **Routing consequence:** grade the routed model's output against the 7 classes on an **all-pass** basis. Three of them (internal inconsistencies, broken cross-refs, broken definitions) *are* the conflict-detection failure mode → **Opus 4.8** for conflict-sensitive review, **avoid GPT 5.6 Sol** there.

---

## Generalist context (why not to route off a generalist leaderboard)

- **Verticals re-rank the podium.** The Artificial Analysis intelligence-index leader (Fable 5 ~60, GPT-5.6 Sol ~58–59, Opus 4.8 ~56) is *not* the leader on every legal cut — e.g. Opus 4.8 tops Contract Drafting while GPT 5.6 Sol tops Info Extraction. Never route a legal task off a generalist board.
- **Saturation hides gaps.** GPQA/AIME sit at 94–100% for the top tier — zero routing signal. **HLE** (~53% Fable 5, ~50% Grok 4 Heavy, ~46% Opus 4.8) is the one reasoning test still separating models.
- **Advertised vs effective context diverges 30–60 points past ~200K tokens.** Only Gemini 3 Deep Think holds near its 1M spec.
- **Cost floor:** Chinese open-weight models (DeepSeek V4 Flash ~$0.06/M, Qwen) are 10–50× cheaper than closed frontier — relevant for on-prem/privacy and high-volume triage, at a reliability cost on legal tasks.
- **Scaffold ≠ model** on agentic benchmarks (GAIA scores swing ~30 pts by harness). Judge the *system*, not the model, for agentic legal research.

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
- Contract error base rates (SEC study): https://spellbook.com/labs
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
- §8 first-party run (2026-09) — harness, raw answers and per-suite scores: `legal-llm-benchmark/astra/`
  (`core_run.py`, `suites.py`, `analyse.py`); report: https://claude.ai/code/artifact/cb794fc9-b9e3-45f0-9437-8e3eccc88f7e
