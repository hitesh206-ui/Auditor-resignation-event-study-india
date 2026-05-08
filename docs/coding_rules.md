# Auditor Resignation Reason Coding Rules

## Purpose

This document defines how auditor resignation reasons will be classified for empirical analysis.

## Reason Categories

### 1. Generic
Use this category when the disclosure cites non-specific or routine reasons.

Examples:

- preoccupation
- personal reasons
- other commitments
- health reasons
- inability to devote time

### 2. Serious
Use this category when the reason indicates potential audit limitations, governance concerns, or management-auditor conflict.

Examples:

- non-availability of information
- lack of cooperation from management
- inability to obtain audit evidence
- unresolved audit matters
- inability to complete audit
- pending information from company
- concerns over financial statements

### 3. Fee-related
Use this category when the resignation is linked to non-payment or dispute over audit fees.

Examples:

- non-payment of fees
- fee dispute
- outstanding audit remuneration

### 4. Regulatory / Eligibility
Use this category when resignation is due to auditor rotation, independence, ineligibility, or regulatory constraints.

Examples:

- rotation requirement
- independence issue
- ineligibility
- regulatory compliance

### 5. Vague / Unclear
Use this category when the disclosure does not provide a meaningful reason.

Examples:

- reason not clearly stated
- no specific reason provided
- insufficient disclosure

### 6. Business Restructuring
Use this category when resignation is linked to restructuring rather than a governance concern.

Examples:

- merger
- liquidation
- subsidiary restructuring
- company no longer requires audit due to restructuring

## Dummy Variables

- serious_reason_dummy = 1 if category is Serious
- vague_reason_dummy = 1 if category is Vague / Unclear
- fee_related_dummy = 1 if category is Fee-related
- regulatory_dummy = 1 if category is Regulatory / Eligibility

## Coding Principle

When in doubt, preserve the original reason text and mark the category as `Vague / Unclear`. Do not over-interpret the disclosure.
