````markdown
name: Example Space for KTCEDC
summary: A minimal Copilot Space manifest and guidance for this repository.

---

# What to include in this Space

This repository contains example configuration for GitHub Copilot Spaces. Add the following context to the Space to make Copilot Chat an effective assistant for this repo:

- Repository root files: README.md, mcp_config.json, .devcontainer/devcontainer.json
- Important paths: any src/ or docs/ folders, configuration files, CI workflows
- Architecture notes: high-level overview of the project, core components, data flow
- Setup & dev steps: how to run the project locally, required environment variables, build & test commands
- Known issues / TODOs: short list of open tasks, design trade-offs, and any files to avoid
- Example prompts & tasks: a set of natural-language questions and tasks you often ask Copilot about this repo

# Example Space manifest (suggested content)

```yaml
# space-manifest.yml
title: "KTCEDC example Space"
owner: "RepoKan"
visibility: private
context:
  - path: 
    - README.md
    - mcp_config.json
    - .devcontainer/devcontainer.json
  - files:
    - path: "README.md"
      purpose: "Project overview & how to use Copilot Spaces"
    - path: "mcp_config.json"
      purpose: "MCP client configuration enabling copilot_spaces toolset"
  - notes:
    - "Add architecture.md with diagrams and component responsibilities"

# recommended sample queries
queries:
  - "How do I run the project locally?"
  - "Where is the devcontainer configuration and how do I change the base image?"
  - "Summarize the files that configure Copilot Spaces for this repo."
```

# Security and private data
- Do NOT add secrets, private keys, or credentials to the Space. Instead document how to obtain them and how to configure them locally (e.g., using environment variables or a secrets manager).

# Using the Space in Copilot Chat
1. Point your MCP client at the provided `mcp_config.json` (already in repo root).
2. Enable the `copilot_spaces` toolset via the X-MCP-Toolsets header.
3. Use the example prompts above to validate the Space’s usefulness and add additional context as needed.

---

If you’d like, I can commit this file to .copilot/example-space.md in the repository now.
````