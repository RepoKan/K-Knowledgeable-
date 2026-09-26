# K Knowledge Supporting Capability Registry R1

This registry is a sanitized routing index. It is not factual evidence and does not override Production source authority.

## Core payment engineering

- KTC Android payment source inspection and Production debugging
- SUNMI P3 / Android / vendor SDK integration
- Location / GPRS / SIM / Wi-Fi / Field 61 policy
- ISO8583 transaction lifecycle and message mapping
- EMV / CTLS / Field 55 / TLV handling
- TLE / TMS / host / network / session behavior
- Reversal / advice / settlement / persistence
- Security / PCI DSS / sensitive logging hygiene

## Project engineering governance

- GitHub repository and revision governance
- Notion KKL Base knowledge governance
- Skill and Agent operating-contract governance
- Master Source file promotion, SHA-256 deduplication, and provenance
- Conflict / HOLD / release-impact review
- Dynamic model selection under `KKS-MODEL-ROUTING-R1`
- Project-wide credit/quota stop enforcement and Freebuff rate-limit intent under `KKS-MODEL-CREDIT-LIMIT-GATE-R1`

## Requirements and integration analysis

- RFI and POS requirement analysis
- Alternative-payment and web-service integration analysis
- TMS and device architecture review
- Technical flow and artifact review

## Routing rule

Use the most specific available Skill or workflow for the task. For KTC payment-critical inspection, prefer the dedicated payment inspection workflow. Use the general Project inheritance workflow to bootstrap source identity, capability routing, retention, and synchronization.

For explicit model selection, apply `docs/governance/K_KNOWLEDGE_SUPPORTING_MODEL_ROUTING_R1.md`. For budget/rate-limit enforcement, also apply `docs/governance/K_KNOWLEDGE_SUPPORTING_MODEL_CREDIT_LIMIT_R1.md`. Route by job complexity and execution surface, verify the model is actually available in the active workspace/product, and prefer current capability tiers over stale hard-coded model names.

## Evidence rule

A capability entry only indicates where to look next. Production conclusions must still be supported by exact source, approved specification, vendor documentation, matched runtime evidence, or approved Project business rules according to the governing source-precedence policy.

Model choice is also routing metadata, not evidence. A stronger model cannot replace missing Production proof, approved specifications, runtime tests, or the applicable HOLD gate.
