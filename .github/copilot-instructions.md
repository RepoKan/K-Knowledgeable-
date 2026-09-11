# K Knowledge Supporting AI Governance

Use `KKS-PROJECT-INHERITANCE-R1` as the Project bootstrap and inheritance contract for K Knowledge Supporting work. For KTC payment-critical review, also apply the more specific `KTC-PAYMENT-MASTER-R1` contract.

## Repository boundary

This repository is public and sanitized. Never add KTC Production source, private specifications, credentials, cryptographic or signing material, payment keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Project inheritance contract

For a new Project chat or new AI session:

1. Use only durable Project sources that are actually available in the session.
2. Load the general Project inheritance workflow before domain routing when applicable.
3. Route to the most specific domain Skill/workflow for the task.
4. Treat capability metadata as routing information, not factual evidence.
5. Do not claim that arbitrary historical ChatGPT conversations were searched unless a supported history-search surface is actually available.
6. Promote reusable chat-derived rules, capabilities, artifacts, and decisions into durable Project sources before expecting future chats to inherit them.
7. Apply SHA-256 exact-match deduplication for Master Source promotion; preserve non-identical versions and provenance.
8. Preserve source conflicts and use the governing source-authority order; never use last-write-wins for business truth.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md` and `docs/governance/K_KNOWLEDGE_SUPPORTING_CAPABILITY_REGISTRY_R1.md`.

## Production review contract

For Production-critical payment work:

1. Resolve the exact private Android source revision.
2. Resolve the exact private Knowledge Master revision.
3. Verify the Android repository pins the exact Knowledge Master SHA used for the review.
4. Resolve the applicable approved specification and matched runtime evidence when required.
5. Trace callers, callees, state, callbacks, persistence, SDK/kernel boundaries, ISO8583/host effects, reversal/advice and settlement impact as applicable.
6. Do not invent missing parameter names, thresholds, mappings, units, defaults, host contracts or security values.
7. Preserve source conflicts and apply the highest applicable authority.
8. If material evidence is missing, use `HOLD - IMPACT NOT PROVEN`.

## Three-source model

Synchronize reusable governed knowledge by revision and provenance across:

- K Knowledge Supporting Project durable sources
- Notion KKL Base
- Private GitHub Android + Knowledge Master pair

Skill and Agent instructions enforce the workflow but do not override exact Production source, approved specifications, or matched Production evidence.

See `docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md` for the payment-specific public governance pointer.
