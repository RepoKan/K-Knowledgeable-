# KTC Payment Three-Source Master Rule R1

Status: SANITIZED PUBLIC GOVERNANCE POINTER  
Master Rule ID: `KTC-PAYMENT-MASTER-R1`  
Project: K Knowledge Supporting

## Purpose

Define the synchronization boundary between three operational sources without publishing restricted KTC material:

1. K Knowledge Supporting Project — active project decisions and approved business clarifications.
2. Notion KKL Base — human control plane for provenance, conflicts/HOLD, inspection and release/impact records.
3. Private GitHub pair — exact Android source plus the private Knowledge Master pinned by exact Git SHA.

The Skill and Agent enforce this governance model. They are not additional authority sources.

## Source precedence

Use the highest applicable authority for Production conclusions:

1. exact Production source
2. approved KTC specification
3. official vendor/platform documentation
4. matched Production runtime evidence
5. approved project business rules / explicit clarification
6. derived project or curated knowledge
7. general AI knowledge

Do not use last-write-wins. Preserve conflicts. Missing material evidence must result in `HOLD - IMPACT NOT PROVEN`.

## Production-ready synchronization gate

A rule may be marked synchronized for Production use only when:

- the project rule revision is identified;
- the matching Notion KKL Base record is present with provenance/status;
- `RepoKan/KTC-Knowledge-Master` exists as a private repository at an exact commit SHA;
- `RepoKan/KTC-EDC-P3-Android` exists as a private repository at an exact source SHA;
- the Android repository pins the exact Knowledge Master SHA used for inspection/release;
- no unresolved higher-authority conflict changes the rule behavior.

Until those private remote checks succeed, the overall state is `PARTIAL`; Production application remains on HOLD when the missing revision is material.

## Public repository boundary

This repository is public and contains sanitized governance only. Do not commit KTC Production source, private specifications, credentials, payment or signing keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Operational components

- Reusable review Skill: `ktc-payment-inspector` — maintained outside this public repository when it contains project-specific business detail.
- Agent contract: private Knowledge Master `agent/AGENT_OPERATING_CONTRACT.md` plus private Android `AGENTS.md` / repository instructions.
- Canonical private governance: private Knowledge Master `governance/THREE_SOURCE_MASTER_RULE_R1.md`.
- Human control plane: Notion KKL Base Master Rule page.
