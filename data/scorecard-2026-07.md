# Legal Model Scorecard — data as of 2026-07

**This is the canonical dataset for the `legal-ai-model-router` skill bundle.** Every skill's
`references/scorecard.md` is a slice of this file. When you update benchmarks, update this file
first, bump the date, and re-slice the per-skill copies. See `../README.md` → "Updating the data".

> **Read this before trusting any number below.** These are point-in-time snapshots from public
> benchmarks that change monthly and disagree with each other. Use them as a **prior**, not a verdict.
> For any high-stakes matter, re-check the live sources (bottom of this file) and keep a human in the loop.

---

## How to read this

Each vertical reports the metric its source benchmark actually measures. They are **not** the same metric,
so scores are **not** comparable across verticals. "Reliability" on legalbenchmarks.ai (all-pass on a
lawyer checklist) is a far harsher scale than "accuracy" on Vals LegalBench (multiple-choice legal reasoning).

Model names reflect what the benchmarks published as of the snapshot date. Vendors ship fast; a name here
may already be superseded. The **archetype** (what a model is *for*) ages slower than its exact rank.

**§8 is different in kind from §1–§7.** Sections 1–5 report third-party leaderboards; §6–§7 are derived
guidance that ranks no models; **§8 is a first-party run we executed ourselves in 2026-09** — newer models,
measured costs, and properties no public board covers (consistency, reasoning-effort economics, non-English
legal accuracy), but small samples and no independent reproduction. Weight it accordingly: trust §8 on
*direction and mechanism*, trust §1–§5 on *relative rank*.

---

## 1. Contract Drafting

**Source:** legalbenchmarks.ai — "Contract Drafting" (34 tasks, 3rd installment, refreshed monthly).
**Metric:** `Reliability` = share of tasks passed *fully* correct on a lawyer-written checklist (binary;
one miss fails the whole task). `Usefulness` = 1–3 mean (clarity / length / structure). Cost = $/task.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | Claude Opus 4.8  | Anthropic | 67.6%       | 2.67       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 61.8%       | 2.66       | ~$0.63    |
| 3    | Grok 4.5         | xAI       | 58.8%       | 2.61       | ~$0.19    |
| 4    | Gemini 3.5 Flash | Google    | 55.9%       | 2.60       | ~$0.08    |
| 5    | Claude Sonnet 4.6| Anthropic | 50.0%       | 2.63       | $0.13     |
| 5    | Gemini 3.1 Pro   | Google    | 50.0%       | 2.69       | $0.07     |
| 7    | GPT 5.6 Sol      | OpenAI    | 44.1%       | 2.75       | ~$0.19    |
| 7    | Qwen 3.7 Max     | Alibaba   | 44.1%       | 2.67       | ~$0.03    |
| 9    | GPT-5.5          | OpenAI    | 41.2%       | 2.77       | $0.15     |
| 10   | DeepSeek V4 Pro  | DeepSeek  | 26.5%       | 2.68       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 26.5%       | 2.55       | ~$0.01    |

**Truths / nots**
- **Opus 4.8** — best all-round drafter; uniquely willing to *flag contradictory instructions* instead of drafting through them. Truth: highest reliability. Not: not the cheapest.
- **Fable 5** — ties Opus on quality but ~2.2× the cost/task without beating it. Not: overpriced for drafting.
- **Grok 4.5** — best non-Anthropic drafter, cheapest of the top 4; uniquely good at *leaving already-sound language untouched* (fewer gratuitous rewrites). Strong value pick.
- **GPT 5.6 Sol** — **highest usefulness (2.75) is a trap:** "more polished than accurate." >50% of its drafts miss ≥1 instruction hidden behind clean prose. Do not route drafting here on the strength of readability.
- **All models** — weak at conflict detection; GPT 5.6 Sol is the worst at silently drafting through contradictions.

---

## 2. Info Extraction

**Source:** legalbenchmarks.ai — "Info Extraction" (29 tasks). Documents sent in **native, unconverted form**,
so file-reading (incl. scanned docs) is part of what's tested. Same two-axis rubric as drafting.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | GPT 5.6 Sol      | OpenAI    | 89.7%       | 2.78       | ~$0.19    |
| 2    | Claude Opus 4.8  | Anthropic | 86.2%       | 2.54       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 86.2%       | 2.51       | ~$0.63    |
| 4    | GPT-5.5          | OpenAI    | 82.8%       | 2.62       | $0.15     |
| 5    | Grok 4.5         | xAI       | 79.3%       | 2.70       | ~$0.19    |
| 6    | Claude Sonnet 4.6| Anthropic | 72.4%       | 2.47       | $0.13     |
| 7    | Gemini 3.1 Pro   | Google    | 65.5%       | 2.51       | $0.07     |
| 7    | Gemini 3.5 Flash | Google    | 65.5%       | 2.76       | ~$0.08    |
| 9    | DeepSeek V4 Pro  | DeepSeek  | 62.1%       | 2.37       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 58.6%       | 2.75       | ~$0.01    |
| 11   | Qwen 3.7 Max     | Alibaba   | 55.2%       | 2.55       | ~$0.03    |

**Truths / nots**
- **GPT 5.6 Sol** — best at *exhaustive clause retrieval* and *cross-document comparison*. Blind spots: **scanned documents**, and **flattening conditional answers into absolutes** ("if X then Y" → "Y"). Verify conditionals.
- **Opus 4.8 / Fable 5** — most dependable pair (tied #2), but the **most verbose** answers tested; you pay in output tokens and post-processing.
- **Grok 4.5** — **best scanned-document handling of any model**, but under-returns on completeness ("almost all" instead of all). Route here for image-heavy/OCR-adjacent extraction, then double-check coverage.
- **Cheap tier (Qwen 3.7 Max, GPT-5.4-mini, DeepSeek V4 Pro)** — bottom of reliability (55–62%). Fine for low-stakes triage, not for extraction you'll rely on.

**Related academic anchors (Wei Chen / Atticus Project):** **CUAD** (clause extraction, 510 contracts, 41 clause types), **MAUD** (M&A reading comprehension, 92 question types), **ACORD** (clause retrieval, 1–5 relevance). These are the open datasets the field uses when it wants reproducible extraction/retrieval evaluation.

---

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
- **Acceptance test (model-agnostic):** whichever model you route, grade its output against the 7 Spellbook error classes (§6) on an *all-pass* basis, and auto-elevate purchase/M&A stakes to High.

---

## 5. Legal Translation

**Weakest public-benchmark coverage of the five verticals — treat this section as directional, not
benchmark-backed the way §1–§3 are.** There is **no clean legal-translation leaderboard** for frontier
LLMs. Guidance is triangulated from (a) general MT benchmarks that don't touch legal text, (b) multilingual-
reasoning benchmarks used as a proxy, and (c) dedicated legal-MT studies. **Certified/sworn translation
always requires a qualified human translator — the LLM is a first-draft engine here, never the signatory.**

**General translation quality**
- **WMT25** (field's rigor standard): human eval → **Gemini** family won (topped 14/16 language pairs);
  GPT and Cohere Command-A close; DeepSeek/Claude second tier. Rankings are **metric-dependent** — a
  separate methodology put GPT-5, Grok 4, Claude Opus, Gemini in a different order. No settled "leader."
- **Per-language split (directional):** Claude leads German/Japanese/Korean/Dutch/Italian and is
  **preferred by professional translators for tone/register**; Gemini leads Chinese/Brazilian-Portuguese/
  Ukrainian and carries the larger context window for long documents.

**Multilingual reasoning (proxy when no legal-MT number exists)**
- Roughly: **Gemini 3.1 Pro** tops raw multilingual knowledge (~94 MMLU, approx.), **GPT-5.x** close and
  strongest on MMLU-ProX, **Claude Opus** a strong #3 with notably good multilingual math (MGSM).
- This is reasoning *in* a language, not translation *quality* — a proxy, not a substitute.

**Legal-translation-specific evidence (thin but real)**
- **SwiLTra-Bench** (arXiv 2503.01372) — the most rigorous dedicated legal-MT benchmark found (Swiss
  statutes/case-law, DE/FR/IT/Romansh). Finding: **general-purpose LLMs still trail specialized legal-MT
  systems** on terminology equivalence, statutory register, and precedent-preserving case-law translation.
- **EU EUR-Lex** explicitly tells users **not** to rely on its own MT tool for legislation — only the
  human-verified official-language texts are authentic. Institutional distrust of legal MT is stated, direct.
- Glossaries fix *terminology consistency* but not **negation accuracy**, **jurisdiction-concept mapping**
  (common-law "discovery"/"plea bargain" have no civil-law equivalent), **cross-reference integrity**, or
  **legal effect**. These are the failure modes that make legal MT dangerous.

**Arabic / MENA**
- **No Arabic legal-*translation* benchmark exists** — a genuine gap. Arabic legal *reasoning* benchmarks
  exist (**ArabLegalEval**, **ALARB**); tellingly, ArabLegalEval was built by machine-translating English
  LegalBench into Arabic *then* expert-verifying — an implicit admission that raw MT needs human check.
- General Arabic reasoning: **Gemini 3.1 Pro / 3 Pro** lead (~93), **Claude Opus** close (~91–92). Claude's
  Arabic prose is reported (soft/qualitative) as more natural.
- **Mistral is a documented Arabic weak point.** **Qwen** (Qwen-MT line) and **Cohere Aya** are purpose-built
  multilingual and are the strongest *self-hostable* Arabic options.
- **RTL is a UI problem, not a model problem** — output text is fine; display alignment is a front-end
  concern (relevant only if you build your own Arabic UI on the API).
- **Direct legal-accuracy measurement (§8.3, 2026-09, n=6):** on Saudi, UAE, Qatari, Egyptian and French
  provisions asked in the local language, **Claude Opus 5 scored 6/6 legally correct; GPT-6 Astra and
  GPT-5.6 Luna Pro both 4/6** — failing the *same two* items. All three replied in the right language and
  cited the right provision every time; only the substance was wrong. Small n, but it is a measurement of
  legal correctness rather than a translation-quality proxy, and it agrees with the proxies above.

**Routing metric:** none published. Route on the proxies above; **human legal-linguist review is mandatory,
not optional** — that is documented industry consensus, not a hedge.

---

## 6. Contract Error Base Rates — the review acceptance test (Spellbook Labs)

**This section ranks no models and cannot change a model pick.** Every other section measures a *model*;
this one measures the *target* — how often, and how badly, human-drafted contracts are flawed. That defines
the **acceptance test** a routed reviewer must pass (§4) and a **contract-type risk prior** for setting stakes.

**Source:** Spellbook Labs — empirical study of drafting-error prevalence in SEC-filed material contracts
("Humans Hallucinate Too" / "60% of SEC-Filed Contracts Contain Errors"), https://spellbook.com/labs.
**Scope:** 3,019 material-contract exhibits filed on EDGAR, 500+ public companies, filings 2005–2026, analyzed
with Spellbook's own Review tool. Self-published by a contract-review vendor — trust the *direction* of the
finding (contracts are error-prone; review has real work to do), not the exact percentages, as ground truth.

**The 7 error classes a reviewer must catch (verbatim):**
clear drafting mistakes · internal inconsistencies · undefined terms · broken cross-references ·
broken definitions · ambiguities · clauses that may not work as written.

**Base rates**
- **~60%** ("six in ten") of contracts contained ≥1 drafting issue.
- **~3.1%** high-risk issue rate across the full dataset.
- Per-contract issue count **stable at ~1.1–1.3 across the 20 years** — AI-era drafting is no cleaner.
- Company-level spread: **0.18 → 3.30** issues per contract.
- **Contract-type risk prior:** note purchase agreements **~15%** high-risk, stock & asset purchase agreements **~12%** — deal/M&A paper runs ~4–5× the baseline.

**How the router uses it**
1. **Acceptance test, model-agnostic.** Grade the routed model's output against the 7 classes on an *all-pass* basis (catching 6 of 7 is materially incomplete, not "86% good"). Three of them — internal inconsistencies, broken cross-references, broken definitions — *are* the conflict-detection failure mode, reinforcing why **Opus 4.8** leads conflict-sensitive review and **GPT 5.6 Sol** is the one to avoid there (§4).
2. **Stakes prior by contract type.** Purchase / M&A agreements start at elevated risk (12–15% vs 3.1%). Default them to **High** stakes and route the safe pick, whatever the user said about cost.

**Caveat:** US public-company filings, one vendor's tool. Not a controlled benchmark and not multi-jurisdictional — directional grounding for *what review must catch*, not a measured score.

---

## 7. Council / Consensus Mode — composed picks, no new benchmark

**This section ranks no new models.** It composes the per-task leaders from §1–§5 into **panels** for the
`route-council` skill and documents the rules for running 2–3 of them together on **High-stakes** work. It
changes no single-model pick — it only says which models to convene when one pick isn't enough, and how to
reconcile them.

**When to convene:** stakes = **High** *and* the task is signable/filing-facing, recall-critical (full review,
obligations extraction, conflict detection), a **purchase/M&A agreement** (§6 risk prior auto-elevates these),
or a contested judgment you want independently corroborated. **Do not council** low-stakes triage, high-volume
batch, or real-time work — council is **2–3× compute + slower**.

**Panels (cross-provider, complementary blind spots — same-family pairs share correlated errors):**

| Task type | Council panel (2–3) | Complementarity |
|-----------|---------------------|-----------------|
| **Contract drafting** (§1) | Opus 4.8 (Anthropic) + Grok 4.5 (xAI) + Gemini 3.5 Flash (Google) | Opus 67.6% & flags contradictions · Grok 58.8%, leaves sound language alone · Flash 55.9% cheap third read (alt: Fable 5). |
| **Info extraction** (§2) | GPT 5.6 Sol (OpenAI) + Opus 4.8 (Anthropic) + Grok 4.5 (xAI, when scans) | Sol 89.7% exhaustive but flattens conditionals & weak scans · Opus 86.2% dependable · Grok best scanned-doc handling. |
| **Legal reasoning** (§3) | Fable 5 (Anthropic) + Gemini 3.1 Pro (Google) + GPT-5.6 Sol (OpenAI) | Top 10 within ~2.9 pts (88.56/87.40/86.97) — rank is noise; three near-tied cross-provider reads. Value swap: Gemini 3 Flash. |
| **Contract review** (§4) | Opus 4.8 (Anthropic) + GPT 5.6 Sol (OpenAI) + Gemini 3 Flash / Fable 5 | Opus conflict-detection + redlines · Sol clause coverage · third for independent risk reasoning. |
| **Legal translation** (§5) | Gemini (Google) + Claude Opus (Anthropic) + Qwen-MT / Cohere Aya (Arabic, self-hostable) | Directional, no benchmark. Never auto-merge; human legal-linguist mandatory. |

**Reconciliation — two modes:**
- **Recall-critical / all-pass** (extraction, review, conflict detection) → take the **UNION** of findings;
  every item any member flags is a candidate. **Never majority-vote a singleton away** (Harvey all-pass reality).
- **Judgment / single-answer** (a conclusion, a drafting/translation choice) → **agreement raises confidence;
  material disagreement → escalate to a human**. Do not average conflicting legal conclusions.

**Agreement → confidence (calibrated):** Unanimous → **HIGH** (synthesize; human still runs the acceptance
test) · Isolated dissent → **MED** (keep/investigate the singleton, never drop it) · Material disagreement →
**LOW** (escalate, present every position, **no silent pick**).

**Non-negotiable:** confidence = model **agreement**, not correctness — correlated blind spots yield *confident
wrong* consensus (all members flatten the same conditional, or mis-cite the same rule). Council raises
confidence; the human verify step stays mandatory. (Full skill: `skills/route-council/`.)

---

## 8. First-party measured run — GPT-6 Astra vs Opus 5 vs Luna Pro (2026-09)

**Snapshot date for this section is 2026-09; §1–§7 remain the 2026-07 third-party snapshot.** This is the
only section on this scorecard produced by running the models ourselves rather than reading a public
leaderboard, so its provenance is different in both directions: nothing here is filtered through a vendor's
own eval, and nothing here has been reproduced by anyone else. **n is small. Read the shape, not the decimals.**

**Method:** 41 prompts answered by all three models, drawn round-robin across 20 practice areas; reasoning
effort pinned to `medium` for every model with a 32k ceiling none of them hit; quality/accuracy scored 1–10
by an independent judge (Claude Sonnet 5); cost taken from what OpenRouter actually billed, not estimated
from token counts. Harness and raw data: `legal-llm-benchmark/astra/`.

| Model | Slug | List price in/out | **Cost per answer** | Output tokens | Substance /20 | Hallucination flags | Latency |
|-------|------|------------------:|--------------------:|--------------:|--------------:|--------------------:|--------:|
| GPT-6 Astra | `openai/gpt-6-astra` | $10 / $50 per M | $0.2622 | 5,201 | **17.63** | **0.0%** | 159s |
| Claude Opus 5 | `anthropic/claude-opus-5` | $5 / $25 per M | $0.4566 | 18,190 | 17.22 | 16.2% | 264s |
| GPT-5.6 Luna Pro | `openai/gpt-5.6-luna-pro` | $0.20 / $1.20 per M | **$0.0231** | 16,356 | 16.95 | 12.2% | **83s** |

"Substance" = judged quality + accuracy out of 20. It deliberately excludes the speed term that a composite
score would fold in — on the composite, the fastest model wins instead, which is a different question.

### 8.1 Cost per token is the wrong unit — use cost per answer

**GPT-6 Astra bills 2x Claude Opus 5's per-token rate and costs roughly half as much per answer**, because it
emits ~3.5x fewer tokens to say the same thing. Any routing rule that reads a price list and stops there gets
this backwards. Two consequences for the `Cost/task` columns in §1–§4: they are only comparable between models
of similar verbosity, and reasoning tokens — which the reader never sees — bill at the full completion rate and
belong in the figure.

**Practical rule:** when a cost axis decides a route, price the *answer*, not the token. Measure it once per
model on your own representative prompts; verbosity varies more between models than price does.

### 8.2 Where the models actually separated

Five properties came back **identical across all three models** and therefore cannot inform a route:

- **Fabricated-authority rejection: 16/16 for every model.** Eight real authorities and eight invented ones
  (a UAE algorithmic-accountability law never enacted, a CJEU judgment never handed down, a Bribery Act
  section never drafted, a real GDPR article cited for the wrong subject). Zero confabulation, zero
  over-refusal. **A hallucination-rate claim built on obvious fake citations no longer separates frontier
  models** — the remaining citation risk is subtler than this test can see (see §8.3).
- **Refusal calibration: 100% balanced.** Six requests a lawyer must decline and six near-adjacent legitimate
  ones; every model refused all of the first and answered all of the second.
- **Structured output: 11/11 ground-truth fields, schema-valid, all three.**
- **Tool calling: 100% correct tool and arguments, no over-triggering, all three.**
- **Long-context multi-hop: 9/9.** A liability cap, an overriding carve-out, a compounding escalator and a
  governing-law clause planted at four depths of a document, tested at 25k / 100k / 200k tokens. Every model
  resolved the full precedence chain at every depth — **but it cost $2.01 (Astra) versus $0.15 (Luna Pro) to
  reach an identical answer.**

**Routing consequence:** structured output, tool use and basic citation honesty have become table stakes.
Any routing rule, roadmap item or vendor claim still premised on these being differentiators is out of date.

### 8.3 The one axis that did separate: non-English, non-common-law substance

Six questions across five jurisdictions in the language a local practitioner would use (Saudi and UAE labour
law and Qatari data transfer in Arabic, French limitation periods and unfair-terms doctrine in French,
Egyptian data-transfer licensing in English):

| Model | Replied in the right language | Cited the right provision | **Legally correct** |
|-------|------------------------------:|--------------------------:|--------------------:|
| Claude Opus 5 | 6/6 | 6/6 | **6/6** |
| GPT-6 Astra | 6/6 | 6/6 | 4/6 |
| GPT-5.6 Luna Pro | 6/6 | 6/6 | 4/6 |

Two things matter more than the ratio:

1. **Both OpenAI models failed the same two items** — Saudi Labour Law Art. 75 notice periods and Egyptian
   PDPL cross-border consent. A shared failure across two models of one lineage is a lineage blind spot, not
   sampling noise, and it will not be fixed by switching between them.
2. **Every wrong answer cited the correct article number and then misstated the rule.** Language fidelity was
   perfect and provision retrieval was perfect; only the substance was wrong. **A citation-checking verifier
   passes this failure mode.** Catching it requires checking the proposition against the source, not the
   existence of the source.

**Routing consequence:** this is a direct, if small, legal-accuracy datapoint behind §5's otherwise
proxy-based guidance, and it points the same way — for MENA and civil-law substance, prefer Claude, and treat
any model's output as first-draft pending human legal-linguist review.

### 8.4 Consistency: not purchasable from any of them

Caveat 4 below notes that public benchmarks run one attempt per task and never test drift. We tested it: three
prompts, five repeats each, fixed seed where accepted.

| Model | Accepts a seed | Identical repeats | Mean word-level similarity |
|-------|---------------:|------------------:|---------------------------:|
| GPT-6 Astra | yes | **0/3** | 0.78 |
| GPT-5.6 Luna Pro | yes | **0/3** | 0.73 |
| Claude Opus 5 | **no** | **0/3** | 0.47 |

**Not one model reproduced an identical answer, seed or no seed.** Any consistency guarantee has to be built
above the model — caching, a fixed retrieval layer, human sign-off — never assumed from a parameter.

**Note the parameter asymmetry, which bit this run before it was caught:** Opus 5 accepts `temperature` but not
`seed`; both OpenAI models are the reverse. OpenRouter drops unsupported parameters *silently*, so a harness
that sends one request body to every model believes it pinned knobs that were never attached.

### 8.5 A reasoning-effort dial is a cost lever, not a quality lever

Astra exposes `reasoning_effort`. Ten prompts at each setting:

| Effort | Quality | Accuracy | Reasoning tokens | Cost/answer | Latency |
|--------|--------:|---------:|-----------------:|------------:|--------:|
| low    | **9.00** | 8.86 | 239 | **$0.157** | **79s** |
| medium | **9.00** | **9.00** | 1,735 | $0.247 | 146s |
| high   | 8.83 | 8.67 | 2,976 | $0.238 | 145s |

**High effort scored *worse* than low effort on both axes** for 12x the reasoning tokens, 1.5x the cost and
1.8x the latency. Turning the dial up is not a substitute for routing to a better model, and on these tasks it
was not even neutral. Pin the setting explicitly — leaving it at a provider default is how a model spends its
whole token budget thinking and returns an empty answer.

### 8.6 Negative result — the podium did not re-rank by practice area

This bundle's core thesis is that the podium re-ranks by task. **Within general legal Q&A it did not.** Across
all 20 practice areas the per-area sample was 1–3 prompts and the spread between models was typically 0.5
points out of 20, with outright ties in several areas. No per-practice-area ranking is published here because
**the data does not support one** — it would be noise dressed as guidance.

Read this as a sharpening of the thesis, not a contradiction of it: the re-ranking this bundle documents is
**between verticals** — drafting vs extraction vs research vs review vs translation, which measure genuinely
different capabilities — not between practice areas inside a single vertical. Route on the vertical and on the
axes in §8.1–§8.5; do not expect a different model for M&A than for employment law on the strength of anything
measured here.

---

## Generalist context (why not to route off a generalist leaderboard)

- **Verticals re-rank the podium.** The Artificial Analysis intelligence-index leader (Fable 5 ~60, GPT-5.6 Sol ~58–59, Opus 4.8 ~56) is *not* the leader on every legal cut — e.g. Opus 4.8 tops Contract Drafting while GPT 5.6 Sol tops Info Extraction. Never route a legal task off a generalist board.
- **Saturation hides gaps.** GPQA/AIME sit at 94–100% for the top tier — zero routing signal. **HLE** (~53% Fable 5, ~50% Grok 4 Heavy, ~46% Opus 4.8) is the one reasoning test still separating models.
- **Advertised vs effective context diverges 30–60 points past ~200K tokens.** Only Gemini 3 Deep Think holds near its 1M spec.
- **Cost floor:** Chinese open-weight models (DeepSeek V4 Flash ~$0.06/M, Qwen) are 10–50× cheaper than closed frontier — relevant for on-prem/privacy and high-volume triage, at a reliability cost on legal tasks.
- **Scaffold ≠ model** on agentic benchmarks (GAIA scores swing ~30 pts by harness). Judge the *system*, not the model, for agentic legal research.

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
- §8 first-party run (2026-09) — harness, raw answers and per-suite scores: `legal-llm-benchmark/astra/`
  (`core_run.py`, `suites.py`, `analyse.py`); report: https://claude.ai/code/artifact/cb794fc9-b9e3-45f0-9437-8e3eccc88f7e
- Agentic legal task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- Contract error base rates (SEC study): https://spellbook.com/labs
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
