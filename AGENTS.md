# K Knowledge Supporting Agent Governance

## Master rule

Use `KTC-PAYMENT-MASTER-R1` as the sanitized governance baseline for KTC payment inspection workflows.

## Source synchronization

Treat the following as synchronized operational sources by revision and provenance, not as equal authorities:

1. K Knowledge Supporting Project
2. Notion KKL Base
3. Private GitHub Android + Knowledge Master pair

The exact Production source and approved evidence retain authority according to the master source-precedence rule. Skill and agent instructions enforce the process; they do not become authoritative Production evidence themselves.

## Public repository boundary

This repository is public. Keep only sanitized governance, architecture, connector guidance, and pointers here. Do not add private KTC source, private specifications, credentials, payment/signing keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Agent review gate

For Production-critical analysis:

- Identify exact source and Knowledge Master revisions.
- Verify the Android repository pins the exact Knowledge Master SHA used by the review.
- Identify applicable specification/runtime evidence when required.
- Trace relevant callers/callees/state/callbacks/persistence/SDK/EMV/CTLS/ISO8583/network/reversal/settlement effects.
- Never invent missing parameter semantics.
- Preserve conflicts and missing evidence.
- Use `HOLD - IMPACT NOT PROVEN` whenever material Production impact cannot be proven.

See `docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md`.
