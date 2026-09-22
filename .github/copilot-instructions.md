# K Knowledge Supporting AI Governance

Use `KKS-PROJECT-INHERITANCE-R1` as the Project bootstrap and inheritance contract for K Knowledge Supporting work. Apply `KKS-PROJECT-CHAT-UNIFIED-SCOPE-R1` for Project-wide chat/capability/standing-permission inheritance. For KTC payment-critical review, also apply the more specific `KTC-PAYMENT-MASTER-R1` contract.

## Repository boundary

This repository is public and sanitized. Never add KTC Production source, private specifications, credentials, cryptographic or signing material, payment keys, private endpoints, unredacted Production logs, customer data, or confidential host configuration.

## Project inheritance contract

For every current or future work chat/session inside **K Knowledge Supporting**:

1. Treat the chat as a governance sibling in the same Project.
2. Inherit the same Project governance, capability routing, source-authority rules, and baseline permission envelope.
3. Reuse Project-wide standing non-critical permissions without duplicate grant when the required capability is actually available in the current session.
4. Preserve any narrower authorization limit: one chat, one action, one repository/branch, one file, or one execution remains narrow unless the user explicitly broadens it.
5. Require fresh/action-specific approval wherever the governing rule requires it, including critical Git write/merge/delete, Production/payment/security changes, destructive operations, and permission/access changes.
6. Do not claim technical access merely because the chat is part of the same Project. Historical messages, uploads, mounted files, connector sessions, or external accounts may still be unavailable.
7. Resolve effective executable permission as the intersection of Project-wide user authorization, the governing approval rule, current tool/connector availability, external permissions, branch/ruleset/check constraints, and platform safety/privacy/source-authority requirements.
8. Use only durable Project sources that are actually available in the session for factual inheritance; promote reusable chat-derived knowledge into governed sources for reliable cross-chat reuse.
9. Load the general Project inheritance workflow before domain routing when applicable.
10. Route to the most specific domain Skill/workflow for the task.
11. Treat capability metadata as routing information, not factual evidence.
12. Do not claim that arbitrary historical ChatGPT conversations were searched unless a supported history-search surface is actually available.
13. Apply SHA-256 exact-match deduplication for Master Source promotion; preserve non-identical versions and provenance.
14. Preserve source conflicts and use the governing source-authority order; never use last-write-wins for business truth.

See `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md` and `docs/governance/K_KNOWLEDGE_SUPPORTING_CAPABILITY_REGISTRY_R1.md`.

## Git authorization

- Project default: `KKS-AUTO-GIT-COMMIT-CRITICAL-APPROVAL-R1`.
- Kotlin/Android RCA exception: `KKS-RCA-GIT-EXPLICIT-SCOPE-R1` — `auto Git commit = No`; commit, push, and merge require explicit authorization for action + target repository/branch + scope.
- Critical operations retain fresh, single-purpose approval immediately before the critical write/merge/delete action even when baseline Project permissions are inherited.
- Never use Project-wide inheritance to bypass branch protection, required checks, external repository permission, source authority, privacy, or Production evidence gates.

## GitHub Connector fast path

Apply `KKS-GITHUB-CONNECTOR-FAST-PATH-R1`.

For routine non-critical, non-security repository work that is already within authorized Project scope, ChatGPT/Codex/Copilot may skip duplicate conversational permission prompts and use the available GitHub connector directly.

Do not interpret connector permission as security authorization. Never use connector capability to bypass rulesets, branch protection, required checks/reviews, access controls, secrets, Actions policies, security settings, platform restrictions, or stricter fresh-approval requirements.

Security/admin mutations remain outside the fast path.

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
