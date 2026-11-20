# Legal Model Scorecard — data as of 2026-11

**This is the canonical dataset for the `legal-ai-model-router` skill bundle.** Every skill's
`references/scorecard.md` is a slice of this file. When you update benchmarks, update this file
first, bump the date, and re-slice the per-skill copies. See `../README.md` → "Updating the data".

> **Read this before trusting any number below.** These are point-in-time snapshots from public
> benchmarks that change monthly and disagree with each other. Use them as a **prior**, not a verdict.
> For any high-stakes matter, re-check the live sources (bottom of this file) and keep a human in the loop.

**Snapshot:** §1–§5 and §9 were re-pulled from the live boards on **2026-11-20**. §6 is unchanged (a 2026
study). §8 is a first-party run and keeps its own date, **2026-09**.

---

## What changed since the 2026-07 snapshot

- **legalbenchmarks.ai rebuilt its method.** In August 2026 it moved to an agentic harness. Each model now
  gets two attempts per task, and a task counts only if it passes both. The headline metric is now **task
  pass rate**, which replaces July's "reliability". The site says its results **are not comparable with
  earlier cycles**, so no July number below can be diffed against a November number.
- **Vals LegalBench is saturated.** The top three sit within 0.26 points. Legal research now ranks on
  **Vals Legal Research Bench**, an agentic, all-pass US research board. LegalBench is kept only as a footnote.
- **Harvey's Legal Agent Benchmark (LAB) has scores.** The July snapshot said "no public scores yet". That was
  already wrong: Harvey published baselines on 2026-05-26. There are now three LAB score sets on different
  versions and metrics (§3B). They cannot be compared with each other.
- **The boards now disagree on Claude.** Claude 5.5 models lead legalbenchmarks.ai drafting and extraction but
  sit in the bottom third of HLAB-Vals-1.1, Vals' agentic file-based legal board (§3B). The routing
  consequence is in caveat 9.
- **Legal-specific models have arrived.** They come from OpenAI, Harvey, Thomson Reuters and Z.ai. All are
  gated, product-only, or self-reported, so they appear in §9 as context and never as routing picks.
- **Every July model has been superseded or dropped from the boards.** Opus 4.8, Fable 5, Grok 4.5, Gemini 3.5
  Flash and Sonnet 4.6 no longer appear on legalbenchmarks.ai. The July qualitative findings (an observed
  willingness to flag contradictions, "best scanned-document handling", "flattens conditionals") were observed
  on *those* models. They are kept below only where marked **(July, historical)** and are **not** assumed to
  carry over to successors.

---

## How to read this

Each vertical reports the metric its source benchmark actually measures. They are **not** the same metric,
so scores are **not** comparable across verticals. A legalbenchmarks.ai "task pass rate" (every lawyer-written
criterion met in *both* attempts) is a far harsher scale than a Vals LegalBench "accuracy" (multiple-choice
legal reasoning).

**Board names are system names.** `Muse Spark 1.3` and `Muse Spark 1.3 Max`, `Qwen 3.8 Max` and
`Qwen 3.8 Max 0902`, and `GPT-6.2 Astra (High)` and `(Max)` are listed separately and score differently.
Several of these pairs differ by 10+ points. Never merge a row onto a sibling variant.

Model names reflect what the boards published on 2026-11-20. Vendors ship fast, and a name here may already be
superseded. The **archetype** (what a model is *for*) ages slower than its exact rank.

**§8 is different in kind.** §1–§5 report third-party leaderboards. §6–§7 are derived guidance that ranks no
models. §8 is a first-party run we executed ourselves in 2026-09, with small samples and no independent
reproduction. Trust §8 on *direction and mechanism* and §1–§5 on *relative rank*.

---

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

**This section ranks no new models.** It composes the per-task leaders from §1–§5 (2026-11 data) into **panels** for the
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
| **Contract drafting** (§1) | Opus 5.5 (Anthropic) + Muse Spark 1.3 (Meta) + GPT-6.1 Sol (OpenAI) | Opus and Muse tie at 48.4% from two providers; Muse costs $0.20/task. Sol passes only 25.8% of tasks but meets 86.3% of criteria at $0.11, so it is a cheap independent read. If Muse is not accessible, use GPT-6 Astra (87.1% criteria). Fable 5.1 is also tied, but it shares Opus's family and its blind spots. |
| **Info extraction** (§2) | Opus 5.5 (Anthropic) + GPT-6 Astra (OpenAI) + Qwen 3.8 Flash (Qwen, self-hostable) | Opus leads at 76.7%. Astra (56.7%) has the best extraction Form (83.5%). Qwen 3.8 Flash ties Astra at $0.03/task. Alternative third: Gemini 4 Argon (53.3%, 86.2% criteria). |
| **Legal research** (§3A) | Gemini 4 Neon (Google) + Opus 5 or Fable 5.1 (Anthropic) + Muse Spark 1.3 Max (Meta) | Three providers at 56.25 / 55.29 / 55.29, inside a top nine that spans 2.9 points, so rank is noise. Muse Max costs $0.59/test. Swap: Astra for Law (53.85%) if you already have access (§9). |
| **Agentic file work** (§3B) | Gemini 4 Argon (Google) + Muse Ember or Wonder (Meta) + GPT-6.2 Astra (OpenAI) | HLAB-Vals-1.1 task pass 27.08 / 25.00 (Wonder 23.75) / 16.25. A council does not lift a ceiling near 25%. Every deliverable gets human review. |
| **Contract review** (§4) | Opus 5.5 (Anthropic) + GPT-6 Astra (OpenAI) + Gemini 4 Argon (Google) | Opus leads extraction and redlines. Astra adds coverage and clean Form. Argon leads agentic file work, so it is the best third reader for a multi-document review. |
| **Legal translation** (§5) | Gemini 3.1 Pro / Gemini 4 (Google) + Claude Opus (Anthropic) + a language-specific system (Qwen, Cohere Aya, CUNI-AR-type) | Directional only. In WMT26 the Gemini line led general MT, language-specific systems reached the top cluster wherever they entered, and Claude was not entered. Never auto-merge. A human legal-linguist is mandatory. |

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
