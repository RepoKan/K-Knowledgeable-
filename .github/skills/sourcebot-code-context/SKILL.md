---
name: sourcebot-code-context
description: Use a connected self-hosted Sourcebot deployment as a governed multi-repository code context layer. Trigger for cross-repository code search, architecture tracing, symbol definition/reference lookup, branch-aware file inspection, commit/diff analysis, or natural-language codebase questions when Sourcebot MCP tools are available. Preserve exact repository/ref/SHA evidence, respect repository permissions, never expose tokens or secrets, and fall back to the native GitHub connector when Sourcebot is unavailable or live code-host state is required.
---

# Sourcebot Code Context

Use Sourcebot as the code-context plane for broad, cross-repository understanding. Treat Sourcebot search/index data as repository evidence only after recording the repository and ref used.

## Workflow

1. Identify the code question, repositories in scope, and whether the answer must reflect a specific branch, tag, or commit SHA.
2. Confirm Sourcebot MCP is connected. If unavailable, do not invent results; use the native GitHub connector for accessible repositories or report the capability gap.
3. Discover indexed repositories with `list_repos` when repository identity is uncertain.
4. For broad discovery, use `grep` or `glob`; for structure, use `list_tree`; for exact content, use `read_file`.
5. For symbol tracing, use `find_symbol_definitions` and `find_symbol_references` before drawing call-flow or impact conclusions.
6. For version-sensitive work, use `list_branches`, `list_commits`, and `get_diff`, and record the exact ref or SHA supporting the answer.
7. Use `ask_codebase` for multi-step research when it materially reduces tool churn. Verify critical claims against concrete files and refs when needed.
8. For current GitHub PR, issue, permission, workflow, or branch-protection state, prefer the native GitHub connector because Sourcebot is an indexed snapshot and may lag the code host.
9. Return concise evidence: repository, ref or SHA, relevant file paths, symbols, and unresolved gaps.

Read `references/sourcebot-mcp.md` for MCP authorization, entitlement, and snapshot semantics.

## Evidence and security

- Preserve explicit refs supplied by the user; do not silently substitute the default branch.
- Distinguish Sourcebot indexed state from live code-host state.
- Cite file paths and line ranges when available.
- Never treat an absent Sourcebot result as proof that code never existed.
- Never place API keys, OAuth tokens, repository credentials, private endpoints, signing keys, payment data, or confidential Production payloads in prompts, committed config, or skill files.
- Respect Sourcebot user and repository permission scoping and K Knowledge Supporting source authority.
