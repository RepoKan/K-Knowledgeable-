---
name: enter
description: Bootstrap governed work in the K Knowledge Supporting repository. Use when starting repository inspection, analysis, GitHub/Notion/Slack routing, Android-payment work, CI troubleshooting, knowledge capture, or any change that must establish the exact repository/ref/SHA and apply Project governance before proceeding.
---

# K Knowledge Supporting Entry

Use this Skill as the repository entry gate. Keep the entry step short and route domain work to the most specific available workflow.

## Workflow

1. Classify the task: inspection, analysis, mutation, PR/merge, CI, artifact verification, knowledge capture, or Production-impact review.
2. Establish the exact repository, target ref, and full commit SHA before version-sensitive conclusions or Git writes.
3. Read `AGENTS.md` and `activation/PROJECT_INSTRUCTIONS.md`. For Project-wide scope also read `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md`.
4. Apply `docs/governance/K_KNOWLEDGE_SUPPORTING_VALUE_PROPOSITION_GATE_R1.md` before material analysis, RCA, or Production-solving conclusions.
5. Treat this public repository as a publication boundary. Never publish private Production source/specs, credentials or keys, private endpoints, unredacted logs, customer/cardholder/payment data, or confidential host configuration.
6. Route to the most specific available domain workflow:
   - KTC/payment Production impact -> payment inspection workflow.
   - Kotlin/Android/POS/device work -> Android POS workflow.
   - GitHub refs, PRs, CI, Actions, mergeability, or artifacts -> GitHub engineering troubleshooting workflow.
7. For mutation, use an isolated feature branch by default, inspect the full base...head diff, validate the exact head SHA, and use a pull request. Do not write directly to `main` unless explicitly authorized.
8. Before merge, deletion, permission/access changes, ruleset/branch-protection changes, or other critical operations, require the applicable fresh task-specific authorization and preserve repository enforcement.
9. Report evidence states precisely when useful: `CONFIRMED`, `INFERRED`, `NOT RUN`, `SOURCE BOUNDARY`, `GAP`, or `HOLD`.

## Evidence and safety rules

- Prefer executable repository code/tests and checked-in configuration over summaries.
- Preserve unrelated work and avoid incidental dependency or release changes.
- Treat every committed byte as public.
- Sanitization must happen before commit.
- A successful check applies only to the exact SHA on which it ran.
- Missing CI/status is `NOT RUN` or `NO STATUS`, never PASS.
