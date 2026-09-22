---
applyTo: "docs/**/*.md,docs/**/*.txt,docs/**/*.json"
---

# Instructions for docs/

## Purpose

`docs/` contains public architecture, governance, workflow, security, and engineering guidance for `RepoKan/K-Knowledgeable-`.

Documentation must explain safe intended behavior without claiming permissions, integrations, approvals, or Production readiness that cannot be verified.

## Documentation categories

Use `docs/` for:

- architecture specifications;
- repository and free-tier design;
- governance contracts;
- source-authority and evidence rules;
- inspection workflows;
- connector and automation guidance;
- public operational runbooks;
- sanitized engineering research.

Use `knowledge-supporting/` for durable project knowledge and historical knowledge archives. Use `chatgpt-generated/` for generated content when that path is appropriate.

## Accuracy and authority

Every document should make clear whether its content is:

- an approved rule;
- a proposed architecture;
- a public framework guide;
- external research;
- derived knowledge;
- a historical reconstruction;
- a runtime or Production observation.

Do not present:
- a proposal as an implemented system;
- a configuration file as proof of permission;
- a capability registry as factual evidence;
- a connector description as proof of live access;
- a reconstructed archive as retroactive approval;
- general AI knowledge as Production authority.

Preserve exact revision, version, SHA, date, source, and status when material.

## Public safety rules

Never document or commit:

- real credentials, tokens, passwords, or secrets;
- private keys, signing keys, payment keys, or certificates;
- confidential endpoints or host configuration;
- customer data or payment data;
- unredacted logs;
- restricted source code or specifications;
- live webhook secrets;
- instructions that expose privileged access.

Use placeholders such as `YOUR_TOKEN`, `example.invalid`, or environment-variable names. Clearly label all examples as non-production.

## Connector and OpenAI guidance

When documenting ChatGPT, OpenAI, Copilot, MCP, or GitHub connectors:

- describe configuration as declarative intent;
- state that actual capability depends on the live connector, account, token, app installation, repository permission, branch rules, and platform policy;
- never claim “full permission,” “admin access,” or autonomous operation solely from a JSON file;
- distinguish read, write, delete, workflow, and administration capabilities;
- recommend least privilege;
- require explicit approval for destructive, workflow, security, or Production-impacting operations.

## Architecture documentation

Architecture documents should identify:

- scope and non-goals;
- components and responsibilities;
- trust and security boundaries;
- data classification;
- access and permission assumptions;
- failure boundaries;
- validation and acceptance criteria;
- evolution or migration conditions.

Mark target-state or proposed designs clearly. Do not imply deployment or implementation unless supported by repository evidence.

## Governance documentation

Governance documents must:

- preserve existing Rule IDs where semantics remain unchanged;
- identify scope and status;
- distinguish detection from persistence;
- preserve stricter approval gates;
- preserve source conflicts;
- avoid silently expanding permissions;
- avoid converting one-off task instructions into durable project rules.

If a user requests a reusable Project-wide rule, identify the proposed rule change and required synchronization targets. Do not claim synchronization unless the relevant targets were actually updated and verified.

## Code and configuration examples

Examples must be:

- minimal and reproducible;
- safe to copy;
- based on placeholders and environment variables;
- explicit about dependencies and setup;
- free of live credentials;
- clear about whether they are illustrative or production-ready.

Use timeouts for network examples. Avoid unsafe shell commands, unrestricted URL fetching, broad filesystem access, and destructive automation.

## Workflow documentation

When documenting GitHub Actions:

- explain the trigger and permission requirements;
- use least-privilege permissions;
- distinguish read-only validation from publishing or deployment;
- identify environments and approval gates;
- avoid recommending mutable third-party action tags when a reviewed SHA is required;
- do not suggest workflow administration for ordinary Markdown validation.

## Editing behavior

Before editing:
1. read the complete target document;
2. inspect related governance and architecture references;
3. determine whether the document is normative, proposed, historical, or informational;
4. preserve unrelated content;
5. check for security and permission overclaims.

After editing:
- validate Markdown, YAML, JSON, or code examples as applicable;
- verify internal links and repository paths;
- check that terminology and Rule IDs remain consistent;
- report limitations and unresolved questions.

## Evidence gap behavior

If a requested conclusion depends on missing material evidence, respond with the exact heading:

`GAP`

Provide a numbered list containing:
1. missing evidence;
2. why it matters;
3. how to obtain it;
4. required evidence format.

For Production-impacting conclusions where material impact cannot be proven, use:

`HOLD - IMPACT NOT PROVEN`

Do not fill evidence gaps with assumptions or generic knowledge.