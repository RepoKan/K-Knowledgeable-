"""Interactive cooking assistant powered by GitHub Models."""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Annotated, Any

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
from openai import AsyncOpenAI


CATALOG_PATH = Path(__file__).with_name("recipes.json")


def load_recipes() -> list[dict[str, Any]]:
    with CATALOG_PATH.open(encoding="utf-8") as catalog_file:
        return json.load(catalog_file)


def search_recipes(
    query: Annotated[str, "Ingredients, cuisine, dietary need, or dish to search for."],
) -> str:
    """Search the local recipe catalog and return matching recipe summaries."""
    normalized_query = query.lower().strip()
    if not normalized_query:
        return "Please provide an ingredient, dish, cuisine, or dietary preference."

    matches = []
    for recipe in load_recipes():
        searchable_text = " ".join(
            [
                recipe["name"],
                recipe["description"],
                recipe["cuisine"],
                " ".join(recipe["tags"]),
                " ".join(recipe["ingredients"]),
            ]
        ).lower()
        if normalized_query in searchable_text:
            matches.append(
                f"{recipe['name']} ({recipe['cuisine']}, {recipe['minutes']} min): "
                f"{recipe['description']}"
            )

    if not matches:
        return f"No catalog recipes matched '{query}'. Try a broader ingredient or cuisine."
    return "\n".join(matches)


def extract_ingredients(
    recipe_text: Annotated[str, "A recipe name, recipe text, or ingredient list."],
) -> str:
    """Extract a clean ingredient list from a catalog recipe or pasted recipe text."""
    normalized_text = recipe_text.lower().strip()
    catalog_matches = [
        recipe
        for recipe in load_recipes()
        if recipe["name"].lower() in normalized_text
    ]
    if catalog_matches:
        recipe = catalog_matches[0]
        return f"Ingredients for {recipe['name']}:\n- " + "\n- ".join(recipe["ingredients"])

    if "ingredients:" in normalized_text:
        ingredient_text = recipe_text.split(":", 1)[1]
    else:
        ingredient_text = recipe_text
    items = [item.strip(" .,-") for item in ingredient_text.replace(";", ",").split(",")]
    items = [item for item in items if item]
    if not items:
        return "I could not identify ingredients. Paste a comma-separated ingredient list or a recipe."
    return "Extracted ingredients:\n- " + "\n- ".join(items)


def build_agent() -> ChatAgent:
    load_dotenv()
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise RuntimeError(
            "GITHUB_TOKEN is missing. Create a GitHub token with Models access "
            "and put it in cooking-agent/.env."
        )

    model_id = os.getenv("GITHUB_MODEL", "openai/gpt-4.1-mini")
    client = AsyncOpenAI(
        base_url="https://models.github.ai/inference",
        api_key=github_token,
    )
    chat_client = OpenAIChatClient(async_client=client, model_id=model_id)
    return ChatAgent(
        chat_client=chat_client,
        name="PantryPal",
        instructions=(
            "You are PantryPal, a practical cooking assistant. Help users discover recipes "
            "and prepare ingredients. Use search_recipes whenever the user asks to find or "
            "recommend recipes. Use extract_ingredients whenever the user asks for a shopping "
            "list or ingredients. Be concise, mention assumptions, and never invent catalog "
            "results. You can answer general cooking questions without a tool."
        ),
        tools=[search_recipes, extract_ingredients],
    )


async def run_console() -> None:
    print("PantryPal: your GitHub Models cooking assistant")
    print("Ask for recipes or ingredient lists. Type 'quit' to exit.\n")
    agent = build_agent()
    thread = agent.get_new_thread()

    try:
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not user_input:
                continue
            if user_input.lower() in {"quit", "exit"}:
                break

            try:
                result = await agent.run(user_input, thread=thread)
                print(f"PantryPal: {result.text}\n")
            except Exception as error:
                print(f"PantryPal: I could not complete that request: {error}\n")
    finally:
        await agent.close()


if __name__ == "__main__":
    asyncio.run(run_console())
