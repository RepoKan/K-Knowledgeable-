# K Knowledge Supporting GitHub Connector Fast Path R1

Rule ID: `KKS-GITHUB-CONNECTOR-FAST-PATH-R1`

Effective: `2026-09-22`

Status: `PROPOSED_FOR_MAIN`

## Purpose

Allow ChatGPT, Codex, Copilot, and other governed K Knowledge Supporting agents to use the connected GitHub connector without repeating unnecessary conversational approval or duplicate process for routine, non-critical repository work, while explicitly preventing connector permission from becoming a security bypass.

The fast path is a **process-simplification rule**, not a security-elevation rule.

Canonical principle:

`Connector capability != task authorization != security bypass`

## Fast-path scope

When the active GitHub connector exposes the required operation and the user request is already within the standing Project scope, the agent may proceed without asking the user to repeat the same permission for routine non-critical work such as:

- repository inspection, search, file reads, commit/ref/PR inspection, and CI/status inspection;
- creating or updating sanitized documentation and knowledge files;
- creating a reviewable feature branch for an authorized non-critical change;
- non-critical commits inside the already authorized task scope;
- opening or updating pull requests for those non-critical changes;
- issue/PR comments, labels, and other collaboration metadata when explicitly relevant to the requested task;
- non-destructive retry/rerun actions when the governing workflow already permits them.

For these operations, agents should bypass **duplicate conversational process**, not GitHub controls.

## Mandatory security boundary

The fast path MUST NOT be used to create, change, remove, weaken, or bypass security or access controls.

The following remain outside the fast path and require the applicable explicit task-specific authorization and any stricter fresh-approval rule:

- repository, organization, or enterprise permissions and roles;
- collaborator access, GitHub App permissions, PAT/OAuth scopes, deploy keys, or authentication configuration;
- branch protection, rulesets, bypass lists, required reviews, required status checks, merge restrictions, or deletion/force-push controls;
- Actions policies, environment protection rules, secrets, variables containing sensitive values, OIDC/trusted publishing, runner trust configuration, or token permissions;
- code-scanning, secret-scanning, Dependabot/security policy changes when they alter enforcement or access;
- webhooks, security integrations, audit/security settings, signing/cryptographic configuration;
- visibility changes, repository transfers, destructive history changes, or other administrative security operations;
- Production/payment/security-sensitive changes covered by stricter KKS/KTC governance.

Security collaboration is therefore **not delegated by connector permission alone**.

## Connector-permission rule

Live connector metadata is only a technical capability boundary.

Even if the connector reports `admin`, `maintain`, `push`, `write`, `delete`, workflow-write, or another elevated capability:

1. do not interpret that capability as standing authorization for security/admin work;
2. do not bypass branch protection, rulesets, required checks, review requirements, or GitHub platform restrictions;
3. do not infer permission that the active connector/tool does not actually expose;
4. do not let a static JSON file elevate connector permissions;
5. do not let user-facing wording such as "full access" override the active tool contract;
6. preserve public-repository data boundaries and source-authority rules;
7. preserve all stricter fresh-approval gates.

## ChatGPT / Codex reminder

At the start of any GitHub mutation:

`FAST PATH? -> non-critical + non-security + authorized scope + connector available`

- If **YES**, proceed without duplicate permission prompts and keep the work traceable.
- If **NO**, route to the governing approval/security workflow.

Never ask for duplicate approval merely because the operation is performed through a new chat/session when the standing non-critical permission is already valid.

Never use this rule to skip a fresh approval that another governing rule explicitly requires.

## Source-application inheritance

This rule must be referenced by the Project surfaces that direct ChatGPT/Codex/Copilot behavior:

- `AGENTS.md`
- `activation/PROJECT_INSTRUCTIONS.md`
- `.github/copilot-instructions.md`
- `.github/github_instructions_knowledge-supporting.instructions.md`
- `docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md`
- `chatgpt-connector-channel.json`
- `CHATGPT_CONNECTOR_GUIDE.md`

If another source conflicts, the stricter security/approval requirement wins.

## Non-goals

This rule does not:

- grant new GitHub permissions;
- create a GitHub security bypass;
- disable collaboration or review controls imposed by GitHub;
- weaken branch/ruleset/Actions/security policy;
- authorize destructive or Production-sensitive operations;
- make repository configuration authoritative over platform safety or tool contracts.
