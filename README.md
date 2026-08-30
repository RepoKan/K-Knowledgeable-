# KTCEDC

TestRepowithCodex

## Using GitHub Copilot Spaces

This repository includes example configuration and guidance to help you use GitHub Copilot Spaces with this project.

Files added for Copilot Spaces integration:

- `mcp_config.json` — example MCP client configuration enabling the copilot_spaces toolset.
- `.copilot/example-space.md` — recommendations and an example Space manifest describing what to include in a Space for this repo.

How to use

1. Add `mcp_config.json` to your local Copilot MCP client configuration or point your IDE's MCP client at the example configuration.
2. Follow the guidance in `.copilot/example-space.md` to create a Space in GitHub and add the recommended context.
3. In your IDE, ensure Copilot Chat is set to "Agent" mode and that your MCP client is configured to use the `copilot_spaces` toolset (the `X-MCP-Toolsets` header).

For more information, see: https://docs.github.com/en/copilot/how-tos/provide-context/use-copilot-spaces/use-copilot-spaces
