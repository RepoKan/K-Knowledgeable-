# K Knowledge Supporting AI Governance

Use `KTC-PAYMENT-MASTER-R1` as the governing synchronization contract for KTC payment work.

## Repository boundary

This repository is public and sanitized. Never add KTC Production source, private specifications, credentials, cryptographic or signing material, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Production review contract

For Production-critical work:

1. Resolve the exact private Android source revision.
2. Resolve the exact private Knowledge Master revision.
3. Verify the Android repository pins the exact Knowledge Master SHA used for the review.
4. Resolve the applicable approved specification and matched runtime evidence when required.
5. Trace callers, callees, state, callbacks, persistence, SDK/kernel boundaries, ISO8583/host effects, reversal/advice and settlement impact as applicable.
6. Do not invent missing parameter names, thresholds, mappings, units, defaults, host contracts or security values.
7. Preserve source conflicts and apply the highest applicable authority.
8. If material evidence is missing, use `HOLD - IMPACT NOT PROVEN`.

## Three-source model

Synchronize by revision and provenance across:

- K Knowledge Supporting Project
- Notion KKL Base
- Private GitHub Android + Knowledge Master pair

Skill and agent instructions enforce the workflow but do not override exact Production source, approved specifications or matched Production evidence.

See `docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md` for the public governance pointer.
