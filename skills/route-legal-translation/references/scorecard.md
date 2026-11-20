# Legal Translation — extended notes (data as of 2026-11; §8 first-party run 2026-09)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-11.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 5. Legal Translation

**This is still the weakest-evidenced vertical. Treat it as directional.** There is **no legal-translation leaderboard
for frontier LLMs**, and this refresh found **no Arabic–English legal-translation benchmark**. Guidance is
triangulated from general MT evaluation, dedicated legal-MT studies, and the §8.3 legal-accuracy measurement.
**Certified/sworn translation always requires a qualified human translator. The LLM is a first-draft engine here,
never the signatory.**

**General translation quality — WMT26 (Findings, October 2026, human-evaluated, 23 language pairs, no legal domain)**
- **Best overall:** Wayfinder (an agent built on Gemini 3.1 Pro) reached the top cluster in **17 of 23** pairs. Next
  were **Gemini 3.1 Pro (15)**, TRIVE (14) and Lumen (13, a small constrained system). The Gemini line dominates
  general MT again, as in WMT25.
- **English→Egyptian Arabic, the only Arabic pair:** Wayfinder 83.9, **Gemini 3.1 Pro 83.7**, human post-editing 83.4,
  CUNI-AR 83.2 (a language-specific system), Lumen 83.1, **GPT 5.5 80.8**. **No standalone Claude baseline was entered**,
  so WMT26 says nothing about Claude either way.
- **WMT26's own warning:** LLM-based systems showed a marked tendency toward hallucination and semantic detachment
  from the source, which aggregated human scores largely fail to expose. For legal text, that is the dangerous failure.
- **Language-specific systems** (Grammatist, LiLa, CUNI-AR) reached the top participant cluster in every direction they
  entered. That supports the *self-hostable specialist* lane below.
- *(July, directional, not re-measured):* professional translators preferred Claude for tone/register in
  German/Japanese/Korean/Dutch/Italian. Gemini led Chinese/Brazilian-Portuguese/Ukrainian.

**Legal-translation-specific evidence (thin but real)**
- **SwiLTra-Bench** (arXiv 2503.01372), Swiss statutes and case law (DE/FR/IT/Romansh): **general-purpose LLMs still
  trail specialized legal-MT systems** on terminology equivalence, statutory register and precedent-preserving
  translation. A 2026-07 follow-up by the same author scored **open models only**, so it gives no frontier ranking.
- **Legal-terminology MT** (WMT26 main track, Italian→German varieties, reported): once indirect exposure to the test
  material is removed, even the best models "collapse toward small models". Legal terminology is where MT benchmarks
  overstate quality.
- **EU EUR-Lex** explicitly tells users **not** to rely on its own MT for legislation. Only the human-verified
  official-language texts are authentic.
- Glossaries fix *terminology consistency* but not **negation accuracy**, **jurisdiction-concept mapping** (common-law
  "discovery" has no civil-law equivalent), **cross-reference integrity**, or **legal effect**.

**Arabic / MENA**
- **No Arabic legal-*translation* benchmark exists.** It is still a genuine gap. Arabic legal *reasoning* benchmarks
  exist (**ArabLegalEval**, **ALARB**, plus 2026 additions on Islamic inheritance and Moroccan law), but none test
  current frontier models for routing.
- **Same legal question, different language, different answer** (reported, ArabicNLP 2026, older models): models
  scored markedly lower on identical bar-exam-style questions asked in Arabic than in English. Ask in the language
  of the law *and* check the answer against the source text.
- **Mistral is a documented Arabic weak point** (July evidence; WMT26 En→Egyptian Arabic also placed Mistral Medium
  3.5 low). **Qwen** and **Cohere Aya** remain the strongest *self-hostable* Arabic options. Language-specific fine-tunes
  (the CUNI-AR pattern) can match frontier general MT.
- **RTL is a UI problem, not a model problem.**
- **Direct legal-accuracy measurement (§8.3, 2026-09, n=6):** on Saudi, UAE, Qatari, Egyptian and French provisions
  asked in the local language, **Claude Opus 5 scored 6/6 legally correct, while GPT-6 Astra and GPT-5.6 Luna Pro both
  scored 4/6**, failing the *same two* items. This was measured on Opus 5, **not Opus 5.5**. Do not extend it to newer
  models without re-running.

**Routing metric:** none published. Route on the proxies above. **Human legal-linguist review is mandatory, not
optional**; that is documented industry consensus, not a hedge.

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
- **Non-English legal substance is where they separated (§8.3).** Six provisions across Saudi, UAE, Qatar,
  Egypt and France, asked in the local language: **Claude Opus 5 6/6 legally correct; GPT-6 Astra and GPT-5.6
  Luna Pro both 4/6**, failing the *same two* items. All three replied in the right language and cited the
  right provision every time — fidelity and retrieval were perfect, only the substance was wrong. A shared
  failure across two models of one lineage is a blind spot, not noise. This is a legal-accuracy measurement
  rather than a translation-quality proxy, and it agrees with the §5 proxies: **prefer Claude for MENA and
  civil-law substance, and keep human legal-linguist review mandatory.**

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
