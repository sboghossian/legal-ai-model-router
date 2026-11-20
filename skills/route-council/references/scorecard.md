# Council / Consensus Mode — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

Council mode ranks **no new models**. It composes the per-task leaders that the drafting (§1), extraction
(§2), research and agentic work (§3), review (§4) and translation (§5) sections already establish, and adds the *rules* for
running 2–3 of them together on High-stakes work. Nothing here changes a single-model pick.

## 7. Council panels (composed from §1–§5, 2026-11 data)

Pick **cross-provider** members with **complementary blind spots**. Same-family models (e.g. Opus + Fable,
both Anthropic) share training and therefore correlated errors — their agreement is weaker evidence.

| Task type | Council panel (2–3, cross-provider) | Complementarity (from the scorecard) |
|-----------|-------------------------------------|--------------------------------------|
| **Contract drafting** (§1) | Opus 5.5 (Anthropic) + Muse Spark 1.3 (Meta) + GPT-6.1 Sol (OpenAI) | Opus and Muse tie at 48.4% from two providers; Muse costs $0.20/task. Sol passes only 25.8% of tasks but meets 86.3% of criteria at $0.11, so it is a cheap independent read. If Muse is not accessible, use GPT-6 Astra (87.1% criteria). Fable 5.1 is also tied, but it shares Opus's family and its blind spots. |
| **Info extraction** (§2) | Opus 5.5 (Anthropic) + GPT-6 Astra (OpenAI) + Qwen 3.8 Flash (Qwen, self-hostable) | Opus leads at 76.7%. Astra (56.7%) has the best extraction Form (83.5%). Qwen 3.8 Flash ties Astra at $0.03/task. Alternative third: Gemini 4 Argon (53.3%, 86.2% criteria). |
| **Legal research** (§3A) | Gemini 4 Neon (Google) + Opus 5 or Fable 5.1 (Anthropic) + Muse Spark 1.3 Max (Meta) | Three providers at 56.25 / 55.29 / 55.29, inside a top nine that spans 2.9 points, so rank is noise. Muse Max costs $0.59/test. Swap: Astra for Law (53.85%) if you already have access (§9). |
| **Agentic file work** (§3B) | Gemini 4 Argon (Google) + Muse Ember or Wonder (Meta) + GPT-6.2 Astra (OpenAI) | HLAB-Vals-1.1 task pass 27.08 / 25.00 (Wonder 23.75) / 16.25. A council does not lift a ceiling near 25%. Every deliverable gets human review. |
| **Contract review** (§4) | Opus 5.5 (Anthropic) + GPT-6 Astra (OpenAI) + Gemini 4 Argon (Google) | Opus leads extraction and redlines. Astra adds coverage and clean Form. Argon leads agentic file work, so it is the best third reader for a multi-document review. |
| **Legal translation** (§5) | Gemini 3.1 Pro / Gemini 4 (Google) + Claude Opus (Anthropic) + a language-specific system (Qwen, Cohere Aya, CUNI-AR-type) | Directional only. In WMT26 the Gemini line led general MT, language-specific systems reached the top cluster wherever they entered, and Claude was not entered. Never auto-merge. A human legal-linguist is mandatory. |

## Reconciliation — two modes

- **Recall-critical / all-pass** (extraction, review, conflict detection): value = **UNION**. Every item any
  member flags is a candidate; **never majority-vote a singleton away** (Harvey all-pass reality — 8/10 caught
  is incomplete, not "80% good"). Disagreement is a *find*, not noise.
- **Judgment / single-answer** (a reasoning conclusion, a drafting/translation choice): value =
  **corroboration**. Agreement raises confidence; **material disagreement → escalate to a human**. Do not
  average conflicting legal conclusions.

## Agreement → confidence (calibrated, no false precision)

| Agreement level | Confidence | Action |
|-----------------|:----------:|--------|
| **Unanimous** (same finding set / conclusion / substantive draft) | HIGH | Synthesize consensus; human still runs the acceptance test. |
| **Isolated dissent** (one member differs on one item) | MED | Keep the singleton (union) or investigate the point — never drop it. Human adjudicates. |
| **Material disagreement** (conflicting conclusions / non-overlapping sets) | LOW | Escalate — present every position, no silent pick. |

## Cross-cutting caveats specific to council

1. **Confidence = agreement, not correctness.** Correlated blind spots yield *confident wrong* consensus (all
   members flatten the same conditional, or mis-cite the same rule). Council raises confidence; it never
   certifies truth. Human VERIFY stays mandatory.
2. **Independence is the asset.** Cross-provider members give more independent errors than a same-family pair;
   run members without cross-talk (herding collapses the panel to one opinion). If constraints force a
   same-family or self-hostable-only panel, state the weakened independence.
3. **Cost & latency.** Council is **2–3× compute + slower**. It exists only for High stakes; never council
   low-stakes triage, high-volume batch, or real-time work.
4. **Length still bites.** 1M-token context is now common, but advertised context ≠ effective context, and
   §8.2 measured recall only to 200k tokens. For 100pp+ docs, run each member chunk + map-reduce, then reconcile.
5. **Harness decides the panel.** The same Claude models lead single-pass drafting and extraction and trail
   agentic file work (§3B, caveat 9). Convene from the row that matches how the members will run.
6. **Routing collapse guard.** A router that always picks one dominant model has stopped routing (§caveat 5).
   Council is the counter-move for the High-stakes tail — not a default for everything.

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
- **Do not convene a council on a solved axis (§8.2).** Structured output, tool use, refusal calibration and
  fabricated-citation rejection are now identical and perfect across frontier models — a panel on any of these
  buys unanimous agreement and tells you nothing. Reserve the council for axes that actually separate.
- **Agreement is not correctness, and there is now a measurement behind that (§8.3).** Both OpenAI models
  failed the *same two* MENA/French items in the *same way* — a correct citation attached to a wrong rule. A
  two-model panel drawn from one lineage would have returned unanimous, confident and wrong. **Cross-provider
  composition is not a nicety; it is the entire mechanism.**
- **Repeat runs of one model are not a panel (§8.4).** No model reproduced its own answer across five seeded
  repeats (similarity 0.47–0.78), so self-consistency sampling measures sampling noise, not agreement.

---

## Grounding it leans on (see the canonical scorecard for full sourcing)

- **All-pass reality** (Harvey Legal Agent Benchmark) — why recall tasks take the union, not a vote.
- **Contract error base rates** (Spellbook Labs SEC study, §6) — the 7-class acceptance test the pooled
  review is graded on, and the M&A risk prior that auto-triggers council.
- **Capability ≠ controllability** (Wei Chen / Atticus Project) — a convincing consensus is not permission to
  ship unsupervised.
- **Verticals re-rank the podium** (§Generalist context) — why the panel is task-specific, never a fixed trio.

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
