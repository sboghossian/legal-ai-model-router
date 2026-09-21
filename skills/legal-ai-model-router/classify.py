#!/usr/bin/env python3
"""
Step 1 of the router, with a calibrated number instead of a guess.

    python3 classify.py "Review this Arabic MSA and redline it"
    python3 classify.py --json "…"
    cat task.txt | python3 classify.py -

Classifies a legal task into one of the five verticals and returns a real
confidence, plus two gates: whether this is a legal task at all, and whether it
spans more than one vertical and needs decomposing.

Why this exists. Claude already classifies well off the five-row table in
SKILL.md — that is not the gap. The gap is that `CONFIDENCE: low|med|high` in
the Step 3 output is prose the model writes about itself, and a router's most
important decision is knowing when to distrust its own classification. This
replaces that self-report with a measured probability from Jev, TypeSafe's
System One model, for about $0.00002 a call.

It is an enhancement, never a dependency. No key, no network, a bad response:
print the reason, exit 2, and the caller falls back to reading the table. A
vendor-neutral router that hard-fails on one vendor's outage is not vendor
neutral.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-1.13.0"
TIMEOUT = 20

VERTICALS = {
    "contract_drafting":
        "Generate, redline or rewrite contract language from instructions",
    "info_extraction":
        "Pull clauses, dates, parties, obligations or fields out of documents",
    "legal_research":
        "Issue-spot, apply rules, analyse case law, write a memo, agentic research",
    "contract_review":
        "Assess an existing agreement for risk, deviations or conflicts, plus redline",
    "legal_translation":
        "Translate contracts, statutes or case law across languages",
}

SKILL_FOR = {
    "contract_drafting": "route-contract-drafting",
    "info_extraction": "route-info-extraction",
    "legal_research": "route-legal-research",
    "contract_review": "route-contract-review",
    "legal_translation": "route-legal-translation",
}

QUESTIONS = {
    "vertical": {
        "type": "choice",
        "instructions": "Which legal-AI task vertical does this request belong to? "
                        "If it spans several, pick the one the requester most wants done.",
        "criteria": VERTICALS,
    },
    # The gate. Measured 2026-09-21: out-of-scope requests separate cleanly here
    # (0.03 vs 0.37) and do NOT separate on vertical confidence (0.43 vs 0.61).
    # Threshold this, not the choice.
    "is_legal": {
        "type": "noul",
        "instructions": "This request is a legal task — it concerns law, legal "
                        "documents, legal process, or legal analysis.",
    },
    # First draft of this question read "spans more than one vertical and should
    # be decomposed" and was badly calibrated: 0.27 on a genuinely composite
    # Arabic "review this then translate it". Naming the two-deliverables test
    # explicitly, and giving both criteria sides, is what fixed it.
    "is_composite": {
        "type": "noul",
        "instructions": "The requester is asking for TWO OR MORE separate "
                        "deliverables that different specialists would produce — "
                        "for example a risk review AND a translation, or an "
                        "extraction AND an opinion on what was extracted.",
        "criteria": {
            "true": "More than one distinct work product is requested, whether "
                    "joined by 'and', 'then', 'after that', or listed separately.",
            # Reviewing a contract and redlining it is ONE deliverable, not two:
            # route-contract-review owns the extraction + reasoning + drafting
            # blend outright (SKILL.md Step 1). Without this carve-out the model
            # reads "review and redline" as two jobs — correctly in the abstract,
            # wrongly for this router's taxonomy — and sends it to decompose.
            "false": "One work product is requested, even if producing it takes "
                     "several internal steps or touches several documents. "
                     "Assessing a contract and redlining it is ONE deliverable. "
                     "So is extracting fields in order to answer one question "
                     "about them.",
        },
    },
    "stakes": {
        "type": "score",
        "instructions": "How high are the stakes if the output is wrong or incomplete?",
        "criteria": [
            "Low: internal draft, non-binding, easily corrected",
            "Medium: external but reviewed by a qualified human before use",
            "High: client- or filing-facing, signable, or an M&A/purchase agreement",
        ],
    },
}

# Thresholds. Measured, not guessed — see the run recorded on GRO-1841.
NOT_LEGAL_BELOW = 0.10      # is_legal under this: not a legal task
ASK_THE_USER_BELOW = 0.70   # vertical confidence under this: confirm, don't assume
COMPOSITE_ABOVE = 0.50      # decompose and route each sub-task


class Unavailable(Exception):
    """The calibrated path is not available. Fall back to the table."""


def ask(state: str, api_key: str) -> dict:
    payload = {"model": MODEL, "state": state, "questions": QUESTIONS}
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}",
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        raise Unavailable(
            f"HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:160]}"
        ) from exc
    except urllib.error.URLError as exc:
        raise Unavailable(f"could not reach TypeSafe: {exc.reason}") from exc
    except (TimeoutError, OSError) as exc:
        raise Unavailable(f"request failed: {exc}") from exc


def classify(task: str, api_key: str | None = None) -> dict:
    key = api_key or os.environ.get("TYPESAFE_API_KEY")
    if not key:
        raise Unavailable("TYPESAFE_API_KEY is not set")
    if not task.strip():
        raise Unavailable("empty task")

    answers = ask(task.strip(), key).get("answers", {})
    try:
        vertical = answers["vertical"]["choice"]
        confidence = float(answers["vertical"]["confidence"])
        is_legal = float(answers["is_legal"]["noul"])
        composite = float(answers["is_composite"]["noul"])
        stakes = float(answers["stakes"]["score"])
    except (KeyError, TypeError, ValueError) as exc:
        raise Unavailable(f"unexpected response shape: {exc}") from exc

    if is_legal < NOT_LEGAL_BELOW:
        action = "not-legal"
    elif composite > COMPOSITE_ABOVE:
        action = "decompose"
    elif confidence < ASK_THE_USER_BELOW:
        action = "confirm-with-user"
    else:
        action = "route"

    return {
        "vertical": vertical,
        "skill": SKILL_FOR.get(vertical),
        "confidence": round(confidence, 2),
        "is_legal": round(is_legal, 2),
        "is_composite": round(composite, 2),
        "stakes_score": round(stakes, 2),
        "stakes": ["Low", "Medium", "High"][min(2, max(0, round(stakes)))],
        "action": action,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify a legal task into a vertical, with calibrated confidence.",
        epilog="Exit 0 classified · 2 unavailable, fall back to the table in SKILL.md.",
    )
    parser.add_argument("task", help="the task description, or - for stdin")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    task = sys.stdin.read() if args.task == "-" else args.task

    try:
        result = classify(task)
    except Unavailable as exc:
        print(f"classify: unavailable — {exc}", file=sys.stderr)
        print("classify: fall back to the Step 1 table in SKILL.md", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"VERTICAL:   {result['vertical']}  (p={result['confidence']})")
    print(f"SKILL:      {result['skill']}")
    print(f"STAKES:     {result['stakes']}  (score={result['stakes_score']})")
    print(f"IS LEGAL:   {result['is_legal']}")
    print(f"COMPOSITE:  {result['is_composite']}")
    print(f"ACTION:     {result['action']}")
    if result["action"] == "not-legal":
        print("\n  Not a legal task. Say so; this bundle does not apply.")
    elif result["action"] == "decompose":
        print("\n  Composite. Route each sub-task separately and give a per-step pick.")
    elif result["action"] == "confirm-with-user":
        print("\n  Low confidence. Confirm the vertical with the user before routing.")
    if result["stakes"] == "High":
        print("  High stakes — consider route-council instead of a single model.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
