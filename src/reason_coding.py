"""Reason coding helpers for auditor resignation disclosures."""

from __future__ import annotations


def classify_reason(reason_text: str) -> str:
    """Classify auditor resignation reason into a broad category.

    This rule-based classifier is only a first-pass tool. Final classification
    should be manually reviewed using the original disclosure text.
    """
    if not isinstance(reason_text, str) or not reason_text.strip():
        return "vague_unclear"

    text = reason_text.lower()

    serious_keywords = [
        "non-cooperation",
        "non cooperation",
        "lack of information",
        "information not provided",
        "unable to obtain",
        "audit evidence",
        "pending information",
        "unresolved",
        "management did not",
        "inability to complete",
        "limitation",
    ]
    fee_keywords = ["non-payment", "non payment", "fees", "fee dispute", "remuneration"]
    regulatory_keywords = ["rotation", "independence", "ineligible", "eligibility", "regulatory"]
    restructuring_keywords = ["merger", "amalgamation", "liquidation", "restructuring", "subsidiary"]
    generic_keywords = ["preoccupation", "personal", "other commitments", "health", "unable to devote"]

    if any(keyword in text for keyword in serious_keywords):
        return "serious"
    if any(keyword in text for keyword in fee_keywords):
        return "fee_related"
    if any(keyword in text for keyword in regulatory_keywords):
        return "regulatory_eligibility"
    if any(keyword in text for keyword in restructuring_keywords):
        return "business_restructuring"
    if any(keyword in text for keyword in generic_keywords):
        return "generic"

    return "vague_unclear"


def is_big4(auditor_name: str) -> int:
    """Return 1 if auditor name appears to be Big 4 affiliated."""
    if not isinstance(auditor_name, str):
        return 0

    text = auditor_name.lower()
    big4_keywords = ["deloitte", "pwc", "price waterhouse", "kpmg", "ernst", "ey", "s.r. batliboi"]
    return int(any(keyword in text for keyword in big4_keywords))
