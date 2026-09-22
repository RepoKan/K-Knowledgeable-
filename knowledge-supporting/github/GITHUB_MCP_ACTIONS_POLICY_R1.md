# GitHub MCP and Actions Policy R1

Repository: `RepoKan/K-Knowledgeable-`

Baseline reviewed: `main@afd0260cba7ad92c8767391d4dde1ff39f0d67d9`

## Master connector governance

Apply `KKS-GITHUB-CONNECTOR-FAST-PATH-R1` together with this document. The connector fast path removes duplicate conversational process for authorized routine non-security work; it never authorizes security/admin bypass. Rulesets, branch protection, required checks/reviews, access controls, secrets, Actions policies, authentication scopes, and security settings remain outside the fast path.

## MCP review

GitHub repository MCP settings on GitHub.com are shared by Copilot cloud agent and Copilot code review. GitHub and Playwright MCP servers are enabled by default, so this repository does not need a duplicate custom GitHub MCP server unless external data or wider GitHub access is intentionally required.

The repository already contains a root `mcp_config.json` with a `servers` top-level object. That is not the current GitHub repository MCP-settings schema and it is not the recommended Copilot CLI project-level location. Current GitHub repository settings use `mcpServers`; Copilot CLI project-level configuration is loaded from `.mcp.json` or `.github/mcp.json`.

Because the built-in GitHub server is already available, this change does **not** add a second GitHub server. Instead, `.github/policies/kks-copilot-mcp-settings.json` is a copy-ready repository-settings payload that leaves custom MCP servers empty:

```json
{
  "mcpServers": {}
}
```

This preserves the built-in GitHub and Playwright MCP servers while avoiding unnecessary credentials and duplicate tool surfaces.

Do not add credentials, private keys, tokens, or private Production material to this public repository. If a future custom MCP server requires secrets, use Copilot Agents secrets/variables and follow the required `COPILOT_MCP_` naming rules.

## Actions policy review

The currently reviewed workflows use these trigger events:

- `push`
- `pull_request`
- `workflow_dispatch`
- `schedule`
- `release`

No reviewed workflow uses `pull_request_target`.

The import file `.github/policies/kks-safe-actions-events-r1.json` therefore allows only the events currently required by the repository and intentionally omits `pull_request_target`.

This aligns with GitHub's security guidance for public repositories: `pull_request_target` is a privileged event and GitHub is moving public repositories toward blocking it by default.

## Apply in GitHub UI

### Repository MCP settings

For Copilot cloud agent and Copilot code review:

1. Open repository **Settings**.
2. Open **Copilot -> MCP servers**.
3. Keep the built-in GitHub and Playwright servers enabled.
4. If the page is empty and no external MCP server is needed, use the payload from `.github/policies/kks-copilot-mcp-settings.json`.
5. Add custom MCP JSON only when an external server or wider GitHub data scope is actually required.

### Actions policy

1. Open repository **Settings**.
2. Open **Actions -> Policies**.
3. Choose **New policy -> Import a ruleset**.
4. Upload `.github/policies/kks-safe-actions-events-r1.json`.
5. Review the preview and confirm that `pull_request_target` is not allowed.
6. Create/activate the policy only after confirming the event allowlist still matches all repository workflows.

## Change control

If a future workflow introduces a new trigger such as `workflow_call`, `workflow_run`, `repository_dispatch`, or `merge_group`, update the Actions policy before relying on that workflow.

Do not enable `pull_request_target` by default. If it becomes necessary, first review the workflow for untrusted checkout, secret access, token permissions, cache behavior, and command-injection risk.
