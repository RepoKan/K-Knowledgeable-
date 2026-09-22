# GitHub MCP and Actions Policy R1

Repository: `RepoKan/K-Knowledgeable-`

Baseline reviewed: `main@afd0260cba7ad92c8767391d4dde1ff39f0d67d9`

## MCP review

GitHub repository MCP settings on GitHub.com are shared by Copilot cloud agent and Copilot code review. GitHub and Playwright MCP servers are enabled by default, so the repository settings page does not need an additional custom server unless external data or tools are required.

The repository previously contained a root `mcp_config.json` using a `servers` top-level object. That format is not the JSON shape documented for GitHub repository MCP settings, which use `mcpServers` and require explicit server `type` and `tools`.

A new `.github/mcp.json` is included for project-level Copilot CLI use. It uses the GitHub MCP read-only endpoint and limits toolsets to repository, issue, pull-request, Actions, code-security, and secret-protection data. This is intentionally read-only because GitHub Copilot can use configured MCP tools autonomously.

Do not add credentials, private keys, tokens, or private Production material to this public repository. If a future MCP server needs secrets, use Copilot Agents secrets/variables with the `COPILOT_MCP_` prefix.

## Actions policy review

The currently reviewed workflows use these trigger events:

- `push`
- `pull_request`
- `workflow_dispatch`
- `schedule`
- `release`

No reviewed workflow uses `pull_request_target`.

The import file `.github/policies/kks-safe-actions-events-r1.json` therefore allows only the events currently required by the repository and intentionally omits `pull_request_target`.

This aligns with GitHub's security guidance for public repositories: `pull_request_target` is privileged and should remain blocked unless a hardened workflow has a proven need for it.

## Apply in GitHub UI

### Repository MCP settings

For Copilot cloud agent and Copilot code review:

1. Open repository **Settings**.
2. Open **Copilot -> MCP servers**.
3. Keep the built-in GitHub and Playwright servers enabled.
4. Add custom JSON only when an external MCP server is required.
5. Do not paste `.github/mcp.json` into this page merely to duplicate the built-in GitHub server.

### Actions policy

1. Open repository **Settings**.
2. Open **Actions -> Policies**.
3. Choose **New policy -> Import a ruleset**.
4. Upload `.github/policies/kks-safe-actions-events-r1.json`.
5. Review the preview and confirm that `pull_request_target` is not allowed.
6. Create/activate the policy only after the repository administrator confirms the event allowlist is still complete.

## Change control

If a future workflow introduces a new trigger such as `workflow_call`, `workflow_run`, `repository_dispatch`, or `merge_group`, update the Actions policy before relying on that workflow.

Do not enable `pull_request_target` by default. If it becomes necessary, first review the workflow for untrusted checkout, secret access, token permissions, cache behavior, and command-injection risk.
