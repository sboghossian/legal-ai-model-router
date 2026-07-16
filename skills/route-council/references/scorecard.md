# Council / Consensus Mode — extended notes (data as of 2026-07)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

Council mode ranks **no new models**. It composes the per-task leaders that the drafting (§1), extraction
(§2), reasoning (§3), review (§4) and translation (§5) sections already establish, and adds the *rules* for
running 2–3 of them together on High-stakes work. Nothing here changes a single-model pick.

## 7. Council panels (composed from §1–§5)

Pick **cross-provider** members with **complementary blind spots**. Same-family models (e.g. Opus + Fable,
both Anthropic) share training and therefore correlated errors — their agreement is weaker evidence.

| Task type | Council panel (2–3, cross-provider) | Complementarity (from the scorecard) |
|-----------|-------------------------------------|--------------------------------------|
| **Contract drafting** (§1) | **Opus 4.8** (Anthropic) + **Grok 4.5** (xAI) + **Gemini 3.5 Flash** (Google) | Opus 67.6% & flags contradictions · Grok 58.8%, leaves sound language alone · Flash 55.9%, cheap independent read. Alt 3rd: Fable 5 (61.8%). |
| **Info extraction** (§2) | **GPT 5.6 Sol** (OpenAI) + **Opus 4.8** (Anthropic) + **Grok 4.5** (xAI, add when scans) | Sol 89.7% exhaustive but **flattens conditionals** & weak on scans · Opus 86.2% dependable, conditional-preserving · Grok **best scanned-doc handling**. |
| **Legal reasoning** (§3) | **Fable 5** (Anthropic) + **Gemini 3.1 Pro** (Google) + **GPT-5.6 Sol** (OpenAI) | Top 10 within ~2.9 pts (88.56 / 87.40 / 86.97) — rank is noise, so three near-tied cross-provider reads. Value swap: Gemini 3 Flash (86.86%, $0.5/$3, 4.67s). |
| **Contract review** (§4) | **Opus 4.8** (Anthropic) + **GPT 5.6 Sol** (OpenAI) + **Gemini 3 Flash / Fable 5** | Opus for conflict-detection + redlines · Sol for exhaustive clause coverage (verify conditionals) · third for independent risk reasoning. |
| **Legal translation** (§5) | **Gemini** (Google) + **Claude Opus** (Anthropic) + **Qwen-MT / Cohere Aya** (Arabic, self-hostable) | Directional only — no benchmark. Gemini won 14/16 WMT25 pairs + long context · Claude preferred for register/tone. Human legal-linguist mandatory. |

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
4. **Length still bites.** Advertised context ≠ effective context; past ~200K tokens most members degrade
   (only Gemini 3 Deep Think holds near 1M). For 100pp+ docs, run each member chunk + map-reduce, then reconcile.
5. **Routing collapse guard.** A router that always picks one dominant model has stopped routing (§caveat 5).
   Council is the counter-move for the High-stakes tail — not a default for everything.

## Grounding it leans on (see the canonical scorecard for full sourcing)

- **All-pass reality** (Harvey Legal Agent Benchmark) — why recall tasks take the union, not a vote.
- **Contract error base rates** (Spellbook Labs SEC study, §6) — the 7-class acceptance test the pooled
  review is graded on, and the M&A risk prior that auto-triggers council.
- **Capability ≠ controllability** (Wei Chen / Atticus Project) — a convincing consensus is not permission to
  ship unsupervised.
- **Verticals re-rank the podium** (§Generalist context) — why the panel is task-specific, never a fixed trio.

---

## Live sources — re-check before high-stakes routing

- Contract Drafting & Info Extraction: https://www.legalbenchmarks.ai/leaderboard (+ /research/phase-2-research)
- Legal reasoning (LegalBench, 124 models, live): https://www.vals.ai/benchmarks/legal_bench
- Agentic legal task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- Contract error base rates (SEC study): https://spellbook.com/labs
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
