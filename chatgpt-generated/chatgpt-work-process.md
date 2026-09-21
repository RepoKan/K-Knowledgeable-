---
generated_by: ChatGPT
created_at: 2026-09-21T00:00:00Z
version: 2.0
repository: RepoKan/K-Knowledgeable-
connector: GitHub Contents API / ChatGPT Connector
source_configuration: chatgpt-connector-channel.json
status: operational-process
---

# ChatGPT Connector and GitHub Actions Work Process

This runbook is tailored to `RepoKan/K-Knowledgeable-`, its connector configuration, and its current GitHub Actions workflows.

> **Important:** `chatgpt-connector-channel.json` documents the intended connector behavior. It does not itself grant GitHub permissions or prove that autonomous processing is active. Actual access is determined by the active connector, its securely stored credential, GitHub permissions, branch rules, and the available API/tool connection.

## 1. Repository profile

- **Repository:** `RepoKan/K-Knowledgeable-`
- **Default branch:** `main`
- **Visibility:** Public
- **Primary content:** Markdown knowledge and sanitized project guidance
- **Primary generated-content directory:** `chatgpt-generated/`
- **Long-term knowledge directory:** `knowledge-supporting/`
- **Workflow directory:** `.github/workflows/`

This is a public repository. Never commit passwords, PATs, API keys, private keys, certificates, signing material, private endpoints, payment credentials, or unredacted confidential data.

## 2. Connector configuration mapping

The connector configuration identifies:

| Configuration | Repository process |
|---|---|
| `channel.enabled` | Treat the connector as usable only after the live connection confirms access. |
| `channel.endpoints.base_url` | Use `https://api.github.com/repos/RepoKan/K-Knowledgeable-`. |
| `channel.endpoints.auth_type` | Credentials are token-based, but token values must never enter this repository or chat. |
| `channel.api_routes.post_file` | Create or update files with `PUT` to the GitHub Contents API. |
| `channel.api_routes.get_file` | Read a file with `GET` before updating it. |
| `channel.api_routes.list_directory` | List repository or directory contents with `GET`. |
| `channel.api_routes.delete_file` | Treat deletion as destructive and require fresh, specific approval. |
| `storage_config.default_directory` | Store normal generated Markdown under `chatgpt-generated/`. |
| `storage_config.file_format` | Use UTF-8 Markdown (`.md`). |
| `storage_config.auto_commit` | Expect a successful write to create a Git commit; verify the response. |
| `storage_config.commit_message_template` | Use `Auto-generated from ChatGPT: {filename}` unless a more specific message is required. |
| `connector_processing.max_retries` | Retry at most three times, and only for safe, idempotent operations. |
| `connector_processing.retry_delay_seconds` | Start with a five-second delay; use bounded backoff for repeated service failures. |

The configuration lists broad read, write, delete, and admin capabilities. Those entries are not a reason to use broad access by default. Every operation must use the smallest practical scope.

## 3. Standard ChatGPT request lifecycle

```text
Receive request
    -> identify target and requested action
    -> inspect repository instructions and current file
    -> classify risk and required approval
    -> plan the smallest safe change
    -> read current SHA when updating
    -> write through the Contents API if authorized
    -> verify file and commit result
    -> validate related workflows/content
    -> report exact outcome and limitations
```

### 3.1 Request intake

Before writing, identify:

1. The requested outcome.
2. The exact repository, branch, and file path.
3. Whether the action is read, create, update, delete, workflow management, or administration.
4. Whether the change belongs under `chatgpt-generated/`, `knowledge-supporting/`, or another approved path.
5. Required validation and evidence.
6. Security, privacy, production, and destructive-operation risks.
7. Whether live connector permissions support the requested action.

Keep a request for one Markdown file limited to that file unless the user explicitly expands the scope.

### 3.2 Instruction review

For repository work, inspect applicable instructions in this order:

1. `AGENTS.md`
2. `.github/copilot-instructions.md`
3. Directory-specific README or policy files
4. The target file and related configuration
5. Related workflows and test/configuration files

Repository documentation can describe intended behavior, but it cannot override GitHub settings, branch protection, required reviews, or current connector authorization.

## 4. Markdown file creation and updates

### Create a new file

1. Confirm the target path, normally below `chatgpt-generated/`.
2. Use a descriptive `.md` filename.
3. Add the metadata header used by this runbook.
4. Exclude credentials and unverified claims.
5. Commit with the configured message pattern.
6. Confirm the returned commit and file URL.

### Update an existing file

1. `GET` the current file.
2. Record the current blob `sha`.
3. Preserve unrelated content and metadata.
4. Apply only the requested change.
5. `PUT` the updated content with the current `sha`.
6. If GitHub returns `409`, re-read the file and reassess the change before retrying.
7. Confirm the resulting commit and file content.

### Delete a file

Deletion is not an ordinary autonomous connector operation. It requires fresh, action-specific approval naming the file and repository. Never retry a deletion automatically after an ambiguous response.

## 5. GitHub Contents API reference

Base URL:

```text
https://api.github.com/repos/RepoKan/K-Knowledgeable-
```

| Operation | Method | Path |
|---|---|---|
| Read file | `GET` | `/contents/{path}` |
| List directory | `GET` | `/contents/{path}` |
| Create file | `PUT` | `/contents/{path}` |
| Update file | `PUT` with current `sha` | `/contents/{path}` |
| Delete file | `DELETE` with current `sha` | `/contents/{path}` |

A request body for a file write must contain a meaningful `message` and Base64-encoded `content`; updates and deletes must include the current file `sha`. Do not log authorization headers or token values.

## 6. Authentication and permissions

- Prefer a GitHub App or other least-privileged integration for service automation.
- Use a fine-grained PAT only when a PAT is required.
- Never copy a PAT into Markdown, JSON, YAML, source code, logs, issues, or chat.
- Never assume the connector's `admin: true` configuration field means the live token has administration rights.
- Do not request `workflow`, hook, delete, or administration access for ordinary Markdown creation.
- Use GitHub Actions' built-in `GITHUB_TOKEN` inside workflows whenever it is sufficient.
- Use OIDC rather than a long-lived publishing token for PyPI, as configured by the publishing workflow.

## 7. Current GitHub Actions setup

The repository currently contains these relevant workflows:

### `.github/workflows/codeql.yml`

Current behavior:

- Runs on pushes and pull requests targeting `main`.
- Runs on the weekly schedule `25 20 * * 4`.
- Analyzes `actions` and `python` using `build-mode: none`.
- Uploads CodeQL results with `security-events: write`.
- Reads repository contents.
- Currently also requests `packages: read` and `actions: read`; remove those unless private CodeQL packs or a demonstrated workflow-analysis requirement needs them.
- Uses `actions/checkout@v7` and CodeQL actions at `@v4`; production hardening should replace mutable tags with verified full commit SHAs.
- Should include `workflow_dispatch`, path filters, and concurrency control.

Recommended baseline permissions:

```yaml
permissions:
  contents: read
  security-events: write
```

Recommended language coverage for this repository:

```yaml
matrix:
  include:
    - language: actions
      build-mode: none
    - language: python
      build-mode: none
```

`security-extended` may be enabled after establishing an alert-triage process:

```yaml
with:
  queries: security-extended
```

### `.github/workflows/python-publish.yml`

Current behavior:

- Runs when a GitHub Release is published.
- Builds distributions in `release-build`.
- Transfers them with an artifact.
- Publishes to PyPI using `pypa/gh-action-pypi-publish`.
- Uses `id-token: write`, which is required for PyPI trusted publishing.
- Targets the protected `pypi` environment.

Required hardening:

- Protect the `pypi` environment with required reviewers.
- Restrict trusted publishing to the intended repository, workflow, environment, and release/tag policy in PyPI.
- Pin `checkout`, `setup-python`, `upload-artifact`, `download-artifact`, and the PyPI action to reviewed commit SHAs.
- Ensure a valid `pyproject.toml` or other packaging configuration exists before publishing.
- Build and publish only from an intended release revision.
- Do not replace OIDC with a PAT or PyPI token unless trusted publishing is unavailable and an explicit exception is approved.

## 8. Workflow change process

Changes under `.github/workflows/` have elevated risk because they can execute code and change repository automation.

Before changing a workflow:

1. Read the complete current workflow.
2. Identify all triggers, permissions, secrets, environments, and external actions.
3. Determine whether untrusted pull-request code can execute.
4. Preserve least-privilege permissions.
5. Pin third-party actions where production hardening is required.
6. Validate YAML syntax and expressions.
7. Review the resulting diff.
8. Run or inspect the relevant workflow when authorized.

Creating, updating, or deleting a workflow requires explicit scope. Do not infer workflow-management authorization solely from the connector JSON template.

## 9. Python and CodeQL quality gates

For Python changes:

- Declare dependencies in `pyproject.toml` or a maintained requirements file.
- Run tests for changed behavior.
- Run Ruff or an equivalent linter/formatter.
- Run Bandit or an equivalent security scanner where appropriate.
- Use timeouts for outbound HTTP requests.
- Validate external response types and fields.
- Restrict user-controlled URLs, paths, filenames, and command arguments.
- Use timezone-aware timestamps.
- Avoid broad exception handlers that conceal defects.

CodeQL is one layer of the security process. Review CodeQL alerts together with dependency alerts, secret scanning, workflow security, tests, and manual review.

## 10. Connector error handling

| HTTP result | Process |
|---|---|
| `401` | Stop. Check the secure credential configuration; do not expose or replace credentials in the repository. |
| `403` | Stop and verify effective GitHub permissions, SSO authorization, environment protection, or rate limits. |
| `404` | Verify owner, repository, branch, path, and whether the resource is available to the authenticated connector. |
| `409` | Re-read the file, obtain the latest SHA, and retry only if the requested change still applies. |
| `422` | Correct the request path, body, encoding, branch, or required fields. |
| `5xx` | Use bounded retries for safe reads or idempotent writes; do not repeat destructive actions automatically. |

The configured maximum of three retries is a ceiling, not a requirement. A retry must not create duplicate content, duplicate releases, or repeated destructive effects.

## 11. Metadata template for generated files

```markdown
---
generated_by: ChatGPT
created_at: YYYY-MM-DDTHH:MM:SSZ
version: 1.0
repository: RepoKan/K-Knowledgeable-
connector: GitHub Contents API / ChatGPT Connector
---

# Document title

Content...
```

## 12. Completion checklist

- [ ] Repository and exact path confirmed.
- [ ] `AGENTS.md` and `.github/copilot-instructions.md` reviewed.
- [ ] Connector configuration treated as declarative, not proof of live permissions.
- [ ] Scope kept to the requested file or workflow.
- [ ] No credentials or private data included.
- [ ] Current file SHA used for updates.
- [ ] Destructive or workflow changes received fresh specific approval.
- [ ] Markdown, JSON, YAML, Python, or workflow validation completed as applicable.
- [ ] Resulting file and commit verified.
- [ ] Risks, limitations, and follow-up actions reported.
