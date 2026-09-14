# PantryPal Cooking AI Agent

PantryPal is an interactive Python console agent powered by GitHub Models. It can search a small local recipe catalog and extract ingredients from catalog recipes or pasted ingredient text.

## Setup

1. Create a GitHub personal access token with access to GitHub Models.
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   The Agent Framework package is currently in preview, so the `--pre` flag is required by the package installation guidance. If your package index does not resolve the preview dependency from `requirements.txt`, install it explicitly:

   ```bash
   pip install agent-framework-azure-ai --pre
   ```

3. Copy `.env.example` to `.env` and set `GITHUB_TOKEN`.
4. Run the console app:

   ```bash
   python app.py
   ```

## Example prompts

- `Find a quick vegetarian recipe`
- `What can I make with mushrooms?`
- `Extract the ingredients for Miso Mushroom Ramen`
- `Ingredients: 2 tomatoes, basil, olive oil, garlic`

The default model is `openai/gpt-4.1-mini`. Set `GITHUB_MODEL` in `.env` to try another compatible GitHub Models model.
