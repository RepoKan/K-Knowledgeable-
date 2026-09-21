---
generated_by: ChatGPT
created_at: 2026-09-21T00:00:00Z
version: 1.0
repository: RepoKan/K-Knowledgeable-
connector: GitHub contents API / ChatGPT Connector
status: operational-process
---

# ChatGPT Connector Work Process

This document describes a safe, repeatable process for handling ChatGPT work connected to the public repository `RepoKan/K-Knowledgeable-`.

## 1. Purpose

Use this process to:

- Receive a ChatGPT request.
- Inspect repository context and applicable instructions.
- Plan and perform repository work through the connector.
- Create or update Markdown knowledge files.
- Review workflows, Python code, documentation, and security configuration.
- Validate changes and report the exact result.

This document is process guidance. It does not grant permissions, create credentials, or bypass GitHub repository settings, branch protection, required reviews, or external authorization.

## 2. Repository boundaries

The repository is public and sanitized. Never store or commit:

- Personal access tokens, API keys, passwords, or session credentials.
- Private keys, signing material, certificates, or keystore passwords.
- Private production source code or private specifications.
- Payment credentials or private endpoints.
- Unredacted personal, customer, or confidential data.

Generated knowledge should normally be stored under `chatgpt-generated/`. Long-term project knowledge may be stored under `knowledge-supporting/` when it follows that directory's storage policy.

## 3. Request intake

For every request, ChatGPT should identify:

1. The requested outcome.
2. The target repository, branch, and file path.
3. Whether the request is read-only, a file creation, an update, or a deletion.
4. Required evidence, tests, or validation.
5. Security, privacy, production, and destructive-operation risks.
6. Whether the requested action is authorized and technically available.

If the target or scope is ambiguous, resolve it from the conversation and repository context when safe. Otherwise, ask one concise clarification question before writing.

## 4. Context and instruction review

Before changing files, inspect the relevant sources in this order:

1. Repository-level instructions, including `AGENTS.md` and `.github/copilot-instructions.md`.
2. Directory-specific README or policy files.
3. The target file and related configuration.
4. Existing tests and workflows.
5. GitHub repository settings or workflow results when needed.

Preserve source conflicts and do not treat a generated document as proof of permissions. Repository files can describe an intended connector design, but actual access depends on the active GitHub connection, token or app permissions, branch rules, and available tools.

## 5. Standard work lifecycle

```text
ChatGPT request
    -> confirm scope and safety
    -> inspect instructions and current files
    -> formulate a short plan
    -> make the smallest required change
    -> validate syntax, security, and quality
    -> inspect the resulting diff or commit
    -> report files, validation, and limitations
```

### 5.1 Read

Use read-only repository operations first. Retrieve the current file before updating it so that existing content, metadata, and the current blob SHA are preserved.

### 5.2 Plan

State the intended change internally or to the user as appropriate. Keep the plan narrow. Do not expand a request from one Markdown file into unrelated workflow, dependency, or repository administration changes without explicit authorization.

### 5.3 Write

For a new file:

- Use a descriptive `.md` filename.
- Put it in the approved directory.
- Include the metadata header shown in this document.
- Use a meaningful commit message.
- Do not include secrets or unverified claims.

For an existing file:

- Retrieve the current blob SHA.
- Preserve unrelated content.
- Update only the requested sections.
- Use the SHA to prevent overwriting a concurrent change.

### 5.4 Validate

Depending on the change, validate:

- Markdown structure and links.
- YAML or JSON syntax.
- Python formatting, linting, tests, and dependency declarations.
- GitHub Actions permissions and action references.
- Secret exposure and unsafe path or command construction.
- CodeQL, dependency, and workflow implications.

If validation cannot be run, report that clearly rather than claiming it passed.

### 5.5 Report

The final report should include:

- The file path changed.
- A concise summary of the work.
- The commit or pull request reference when available.
- Validation performed and its result.
- Any unresolved risks, assumptions, or required follow-up.

## 6. Connector operations

The GitHub Contents API uses these operations:

| Operation | Method | Endpoint pattern |
|---|---|---|
| Read a file | `GET` | `/repos/RepoKan/K-Knowledgeable-/contents/{path}` |
| List a directory | `GET` | `/repos/RepoKan/K-Knowledgeable-/contents/{path}` |
| Create a file | `PUT` | `/repos/RepoKan/K-Knowledgeable-/contents/{path}` |
| Update a file | `PUT` | `/repos/RepoKan/K-Knowledgeable-/contents/{path}` with current `sha` |
| Delete a file | `DELETE` | `/repos/RepoKan/K-Knowledgeable-/contents/{path}` with current `sha` |

A successful write creates a Git commit. The connector must not assume that a write succeeded until GitHub returns a successful response and the resulting file or commit can be confirmed.

## 7. Authentication and authorization

- Prefer the least-privileged authentication available.
- Use `GITHUB_TOKEN` for workflow-local repository operations.
- Prefer GitHub App authentication for service integrations.
- Use a fine-grained PAT only when a PAT is necessary.
- Never paste a token into Markdown, source code, logs, issue comments, or chat.
- Store credentials only in the connector's secure secret store or environment.
- Do not document a token's value or claim permissions that have not been verified.

A public repository does not mean that write, delete, workflow, or administration permissions are public. Verify the active connector's effective permissions before attempting an operation.

## 8. GitHub Actions and security work

For workflow changes:

- Set explicit least-privilege `permissions`.
- Prefer `contents: read` unless a write permission is required.
- Use `security-events: write` only for workflows that upload security results, such as CodeQL.
- Add `id-token: write` only for trusted OIDC publishing or deployment.
- Avoid PATs in workflows when `GITHUB_TOKEN` or OIDC is sufficient.
- Pin third-party actions to reviewed commit SHAs for production use.
- Use narrow branch and path filters.
- Add concurrency controls where duplicate runs could conflict.
- Review pull-request workflows carefully because untrusted code may execute in them.

## 9. CodeQL process for this repository

The repository is primarily Python. The recommended CodeQL coverage is:

- `python` with `build-mode: none`.
- `actions` with `build-mode: none` to inspect GitHub Actions workflows.

The baseline CodeQL permissions are:

```yaml
permissions:
  contents: read
  security-events: write
```

Use `workflow_dispatch` for an on-demand scan, a weekly scheduled scan, and path filters that exclude documentation-only changes while retaining Python, workflow, and configuration changes. Review CodeQL alerts together with dependency, lint, test, and secret-scanning results.

## 10. Python quality and security process

For Python changes:

- Declare runtime and dependencies in `pyproject.toml` or a maintained requirements file.
- Run tests for changed behavior.
- Run a linter and formatter such as Ruff.
- Run a security scanner such as Bandit where appropriate.
- Validate external API responses and use request timeouts.
- Restrict user-controlled URLs, paths, filenames, and command arguments.
- Use timezone-aware timestamps.
- Avoid broad exception handling that hides programming errors.

## 11. Error handling

| Result | Meaning | Action |
|---|---|---|
| `401` | Authentication failed | Check the secure credential configuration; never put credentials in the repository. |
| `403` | Permission denied or rate limited | Verify effective permissions, SSO authorization, or rate-limit state. |
| `404` | Repository or path unavailable | Verify owner, repository, branch, and file path. |
| `409` | Concurrent update or SHA conflict | Re-read the file and retry only if the intended change is still valid. |
| `422` | Invalid request | Check the path, encoding, commit message, and request body. |
| `5xx` | GitHub service failure | Retry safely with bounded backoff; do not duplicate destructive operations. |

Retries must be bounded and idempotent. Never automatically retry a delete or workflow-management operation without confirming that the operation remains authorized and safe.

## 12. Change approval rules

Fresh, action-specific approval is required before critical operations, including:

- Deleting files or workflows.
- Writing outside the normal knowledge directories.
- Changing production, payment, signing, or security-critical behavior.
- Changing repository settings, branch protection, hooks, or permissions.
- Force pushes, merges, or other destructive Git operations.

A request to create or update one Markdown file should remain limited to that file unless the user explicitly expands the scope.

## 13. Markdown document template

Use this template for future generated documents:

```markdown
---
generated_by: ChatGPT
created_at: YYYY-MM-DDTHH:MM:SSZ
version: 1.0
repository: RepoKan/K-Knowledgeable-
connector: GitHub contents API / ChatGPT Connector
---

# Document title

Content...
```

## 14. Completion checklist

- [ ] Target repository and path confirmed.
- [ ] Repository instructions reviewed.
- [ ] Scope kept narrow.
- [ ] No credentials or private data included.
- [ ] Existing file SHA used for updates.
- [ ] Syntax and relevant quality checks completed.
- [ ] Security implications reviewed.
- [ ] Commit or resulting file confirmed.
- [ ] Limitations and follow-up items reported.
