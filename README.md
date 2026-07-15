# Legal AI Model Router

**OpenRouter for legal work.** A bundle of vendor-neutral [Claude Code](https://docs.claude.com/en/docs/claude-code)
skills that tell any LLM or router *which model to use for which legal task* — grounded in mid-2026 legal
benchmarks, not vibes or brand loyalty.

Ask "which model should I use to draft this clause / extract these obligations / research this issue / review
this contract / translate this statute?" and the matching skill runs a short intake (cost, speed, accuracy/
stakes, privacy/jurisdiction/language) and returns a concrete recommendation: **primary model, fallback, what
to avoid, and what a human must still verify.**

> ⚠️ This routes *models*. It is **not legal advice**, and it never replaces a qualified lawyer or, for
> translation, an accredited legal translator. Every recommendation ends with what a human must verify.

---

## The one idea

**No single model is best at legal work — the podium re-ranks by task.** On mid-2026 benchmarks:

- **Contract drafting** → Claude Opus 4.8 leads (and uniquely flags contradictory instructions).
- **Info extraction** → GPT 5.6 Sol leads (but flattens conditionals; weak on scans).
- **Legal reasoning** → the top 10 cluster within ~3 points, so **cost and speed decide**, not rank.
- **Contract review** → a *composite* (extraction + reasoning + drafting + conflict-detection); route by sub-task, then grade the result against a 7-class error acceptance test (Spellbook Labs SEC study).
- **Legal translation** → no clean benchmark exists; directional, human review mandatory.

Routing off a generalist leaderboard picks wrong. Route to the **task**, under the user's **constraints**, and
always name what a human must verify.

---

## What's inside

```
skills/
├── legal-ai-model-router/      # entry point — classifies the task, dispatches to a vertical
├── route-contract-drafting/    # generate / redline / rewrite contract language
├── route-info-extraction/      # pull clauses / dates / parties / obligations from documents
├── route-legal-research/       # issue-spot / apply rules / case analysis / memos / agentic research
├── route-contract-review/      # assess an existing agreement for risk / conflicts + redline
└── route-legal-translation/    # translate contracts / statutes / case law (incl. Arabic/MENA)
data/
└── scorecard-2026-07.md        # canonical dataset: all tables, methodology, caveats, live sources (SoT)
```

Each `route-*` skill is self-contained (its own `references/scorecard.md`) so you can install one vertical or
the whole bundle.

---

## Install

Clone, then copy the skills you want into your Claude Code skills directory:

```bash
git clone https://github.com/sboghossian/legal-ai-model-router.git
cd legal-ai-model-router

# whole bundle
cp -r skills/* ~/.claude/skills/

# or a single vertical
cp -r skills/route-contract-drafting ~/.claude/skills/
cp -r skills/legal-ai-model-router   ~/.claude/skills/   # recommended entry point
```

Then just ask in natural language — e.g. *"which model should I use to redline this NDA on a budget?"* — and
the router triggers. Or invoke directly: `/route-contract-drafting`.

The skills are plain Markdown instructions; they carry the benchmark data inline, so they work with any
Claude Code setup and need no API keys, network calls, or dependencies.

---

## How routing works

Every vertical uses the same four intake axes (inferred from your request; you're only asked what's missing,
batched and multiple-choice):

| Axis | Question | Default |
|------|----------|---------|
| **Accuracy / stakes** | How bad is a wrong answer? | High for anything client- or filing-facing |
| **Cost** | Willingness to pay per task / at volume | Balanced |
| **Speed** | Batch vs interactive vs real-time | Interactive |
| **Privacy / jurisdiction / language** | Cloud vs on-prem, which law, which language | US / English / cloud |

Output is uniform:

```
PRIMARY:    <model> — why, tied to your axes + the benchmark
FALLBACK:   <model> — when to switch
ESCALATE IF: <trigger> → <stronger model / human>
AVOID:      <model> — why, for THIS task
CONFIDENCE: low | med | high
VERIFY:     what a human must still check
```

---

## Evidence base

The data is triangulated from public benchmarks and independent research, all cited in
[`data/scorecard-2026-07.md`](data/scorecard-2026-07.md):

- **legalbenchmarks.ai** — Contract Drafting & Info Extraction (lawyer-checklist, all-pass grading).
- **Vals AI × Stanford CodeX — LegalBench** — legal reasoning across 124 models.
- **Harvey — Legal Agent Benchmark (LAB)** — task-design standard for agentic legal work.
- **Spellbook Labs — SEC contract-error study** — ~60% of 3,019 filed contracts carry a drafting issue
  (stable over 20 years; deal/M&A paper 12–15% high-risk). Ranks no models; it's the *acceptance test*
  contract review is graded against, and the risk prior that elevates M&A stakes.
- **Wei Chen / The Atticus Project** — CUAD, MAUD, ACORD; the "demand public benchmarking" thesis and the
  *capability ≠ controllability* principle.
- **WMT25, SwiLTra-Bench, ArabLegalEval** — the (thin) legal-translation evidence.
- **Artificial Analysis, LMArena, SWE-bench, HealthBench** — generalist cross-checks and the "verticals
  re-rank the podium" lesson.

### Honest limitations

- Numbers are a **point-in-time prior** (snapshot **2026-07**) from boards that change monthly and disagree.
- legalbenchmarks.ai is **English-only, US/UK-skewed, single-turn**, LLM-judge-graded. Vals LegalBench is
  multiple-choice reasoning. **Non-US, non-English, multi-turn, and long-horizon work is under-measured.**
- **Legal translation has no reliable public leaderboard** — that vertical is explicitly directional.
- **Hallucinated citations/clauses are the cardinal legal-AI risk.** Every route ends with a verify step.

---

## Updating the data

Benchmarks drift. When you refresh:

1. Edit **`data/scorecard-2026-07.md`** (the single source of truth) — update tables, bump the date, rename the
   file to the new month.
2. Re-slice the per-skill `references/scorecard.md` files from it.
3. Update the inline tables in each `SKILL.md` and note the change in `CHANGELOG.md`.

Live sources to re-pull are listed at the bottom of the scorecard.

---

## License

[AGPL-3.0-or-later](LICENSE). You're free to use, modify, and redistribute; derivative works and network
services must stay open under the same license.

## Disclaimer

Provided as-is, for informational and decision-support purposes only. It routes AI models; it does **not**
provide legal advice, and no model recommendation should be relied upon without review by a qualified legal
professional. Benchmark data may be inaccurate or outdated. Model names and scores reflect third-party
benchmarks and are used descriptively; no affiliation or endorsement is implied.
