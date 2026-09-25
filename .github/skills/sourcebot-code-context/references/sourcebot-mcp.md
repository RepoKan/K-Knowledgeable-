# Sourcebot MCP reference

Sourcebot MCP is served at `/api/mcp` over Streamable HTTP.

Prefer OAuth when supported. API-key authentication uses a bearer token; keep credentials outside repositories and skill packages.

The self-hosted Basic product provides code search and browsing. Current Sourcebot product documentation places Ask Sourcebot and the agent code-context/MCP layer in a paid tier. Do not promise MCP availability until the deployed instance exposes the MCP server.

Sourcebot indexes repositories and branches on a synchronization cycle. Use the native GitHub connector for current PR state, checks, reviews, branch protection, permissions, or immediately-created refs.

Recommended investigation pattern:

1. `list_repos`
2. `list_branches` when ref selection matters
3. `grep` or `glob`
4. `read_file`
5. `find_symbol_definitions` and `find_symbol_references`
6. `get_diff`
7. `ask_codebase` for broad synthesis, followed by targeted verification of critical claims
