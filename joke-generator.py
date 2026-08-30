#!/usr/bin/env python3
"""
Random Joke Generator using Official Joke API
Fetches random jokes from multiple categories and displays them in a formatted way.
"""

import requests
import json
import sys
from typing import Dict, List, Optional
from datetime import datetime

# API Configuration
JOKE_API_URL = "https://official-joke-api.appspot.com"
ENDPOINTS = {
    "random": "/random_joke",
    "jokes": "/jokes",
    "categories": "/jokes/categories",
    "by_type": "/jokes/{type}/random",
    "ten_random": "/jokes/ten"
}


class JokeGenerator:
    """Main class for generating random jokes from external API"""
    
    def __init__(self, base_url: str = JOKE_API_URL):
        """
        Initialize the Joke Generator
        
        Args:
            base_url: Base URL for the joke API
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'ChatGPT-Joke-Generator/1.0'
        })
    
    def get_random_joke(self) -> Optional[Dict]:
        """
        Fetch a single random joke
        
        Returns:
            Dictionary containing joke data or None if request fails
        """
        try:
            url = f"{self.base_url}{ENDPOINTS['random']}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching random joke: {e}", file=sys.stderr)
            return None
    
    def get_joke_categories(self) -> Optional[List[str]]:
        """
        Fetch available joke categories
        
        Returns:
            List of available categories or None if request fails
        """
        try:
            url = f"{self.base_url}{ENDPOINTS['categories']}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching categories: {e}", file=sys.stderr)
            return None
    
    def get_joke_by_type(self, joke_type: str) -> Optional[Dict]:
        """
        Fetch a random joke by specific type/category
        
        Args:
            joke_type: Type of joke (general, knock-knock, programming, etc.)
        
        Returns:
            Dictionary containing joke data or None if request fails
        """
        try:
            url = f"{self.base_url}{ENDPOINTS['by_type'].format(type=joke_type)}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching {joke_type} joke: {e}", file=sys.stderr)
            return None
    
    def get_ten_random_jokes(self) -> Optional[List[Dict]]:
        """
        Fetch ten random jokes at once
        
        Returns:
            List of joke dictionaries or None if request fails
        """
        try:
            url = f"{self.base_url}{ENDPOINTS['ten_random']}"
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching ten jokes: {e}", file=sys.stderr)
            return None
    
    def format_joke(self, joke: Dict) -> str:
        """
        Format a joke for display
        
        Args:
            joke: Joke dictionary from API
        
        Returns:
            Formatted joke string
        """
        joke_type = joke.get('type', 'general').upper()
        setup = joke.get('setup', '')
        punchline = joke.get('punchline', '')
        
        return f"""
╔════════════════════════════════════════╗
║  📝 {joke_type:<33} ║
╠════════════════════════════════════════╣
║ {setup:<40} ║
║                                        ║
║ {punchline:<40} ║
╚════════════════════════════════════════╝
"""
    
    def display_joke(self, joke: Dict) -> None:
        """
        Display a formatted joke to console
        
        Args:
            joke: Joke dictionary from API
        """
        if joke:
            print(self.format_joke(joke))
    
    def display_multiple_jokes(self, jokes: List[Dict], count: Optional[int] = None) -> None:
        """
        Display multiple jokes
        
        Args:
            jokes: List of joke dictionaries
            count: Number of jokes to display (default: all)
        """
        if not jokes:
            return
        
        display_count = count or len(jokes)
        for i, joke in enumerate(jokes[:display_count], 1):
            print(f"\n🎭 Joke #{i}")
            self.display_joke(joke)
    
    def export_jokes_json(self, jokes: List[Dict], filename: str) -> bool:
        """
        Export jokes to JSON file
        
        Args:
            jokes: List of joke dictionaries
            filename: Output filename
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {
                "generated_at": datetime.now().isoformat(),
                "total_jokes": len(jokes),
                "jokes": jokes
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Jokes exported to {filename}")
            return True
        except IOError as e:
            print(f"❌ Error exporting jokes: {e}", file=sys.stderr)
            return False


def main():
    """Main function demonstrating joke generator usage"""
    
    print("=" * 50)
    print("🎉 Random Joke Generator (Official Joke API)")
    print("=" * 50)
    
    generator = JokeGenerator()
    
    # Example 1: Get a single random joke
    print("\n📌 Example 1: Single Random Joke")
    print("-" * 50)
    joke = generator.get_random_joke()
    if joke:
        generator.display_joke(joke)
    
    # Example 2: Get available categories
    print("\n📌 Example 2: Available Joke Categories")
    print("-" * 50)
    categories = generator.get_joke_categories()
    if categories:
        print(f"Available categories ({len(categories)}):")
        for category in categories:
            print(f"  • {category}")
    
    # Example 3: Get joke by specific type
    if categories and len(categories) > 0:
        print(f"\n📌 Example 3: Joke by Type ('{categories[0]}')")
        print("-" * 50)
        typed_joke = generator.get_joke_by_type(categories[0])
        if typed_joke:
            generator.display_joke(typed_joke)
    
    # Example 4: Get ten random jokes
    print("\n📌 Example 4: Ten Random Jokes")
    print("-" * 50)
    ten_jokes = generator.get_ten_random_jokes()
    if ten_jokes:
        print(f"Fetched {len(ten_jokes)} jokes!")
        generator.display_multiple_jokes(ten_jokes, count=3)
        print(f"\n... and {len(ten_jokes) - 3} more jokes!")
        
        # Export to JSON
        generator.export_jokes_json(ten_jokes, "jokes_export.json")
    
    print("\n" + "=" * 50)
    print("✨ Thanks for using the Joke Generator!")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
