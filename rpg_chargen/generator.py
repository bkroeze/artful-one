"""
Core functionality for generating superhero names using AI models.

Author: Bruce Kroeze (0xbigbee@protonmail.com)
Copyright: 2024 Bruce Kroeze
License: MIT
"""

import csv
import json
import os
from typing import List

import google.generativeai as palm
from django.conf import settings


BASE_NAMING_RULES = [
    "Names should be creative and memorable",
    "Avoid exact copies of existing names",
    "Consider both heroes and villains",
    "At least one response should be alliterative",
    'response should be in the form of a list of characters, following the format: "name","tagline","short description" one per line, with no markdown or other formatting'
]

GENRES = ["Superhero", "Dark/Gritty", "Military", "Sci-Fi", "Urban Fantasy"]

BASE_CHARACTER_RULES = [
    "Generate a detailed description of this character"
]


def character_rules_by_genre(genre: str) -> List[str]:
    rules = BASE_CHARACTER_RULES + [
        "Genre of character to generate: " + genre,
    ]

    base_fields = ['powers', 'backstory', 'appearance', 'personality', 'goals', 'motivations', 'weaknesses', 'strengths', 'origin', 'amusing trivial fact']

    if genre == "Superhero":
        fields = base_fields + ['team']
        return rules + [
            "Include occasional pun references in backstory or origin",
            "Include heroics or villainy in backstory or origin",
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(fields)}"
        ]

    elif genre == "Sci-Fi":
        return rules + [
            "Include occasional alien or futuristic details in appropriate fields",
            "Include occasional military titles or ranks where appropriate",
            "Include occasional tech or science terms",
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(base_fields)}"
        ]

    elif genre == "Dark/Gritty":
        fields = ['abilities'] + base_fields[1:]
        return rules + [
            "Include occasional anti-hero, dark or grim themes",
            "Replace the 'powers' field with 'abilities'",
            "Imply the dark cost of or debt due for the character's abilities",
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(fields)}"
        ]

    elif genre == "Military":
        fields = ['abilities'] + base_fields[1:] + ['team']
        return rules + [
            "Include occasional military titles, ranks, operation names or vehicle names where appropriate",
            "Have the origin field include a military background and rank",
            "Add a 'team' field with the name of the team the character is part of",
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(fields)}"
        ]

    elif genre == "Urban Fantasy":
        fields = base_fields + ['team']
        return rules + [
            "Include occasional magical creatures, weapons, occult or supernatural details",
            "Have the origin field include a magical background unless the name doesn't fit",
            "Include occasional puns",
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(fields)}"
        ]

    else:
        return rules + [
            f"The response should be in the form of a raw JSON object without any markdown formatting, with keys: {', '.join(base_fields)}"
        ]


def naming_rules_by_genre(genre: str) -> List[str]:
    rules = BASE_NAMING_RULES + [
        "Genre of names to generate: " + genre
    ]
    if genre == "Superhero":
        return rules + [
            "Names can be 1-3 words long",
            "Include occasional pun names"]
    elif genre == "Sci-Fi":
        return rules + [
            "Include occasional alien or futuristic names",
            "Names can be 1-4 words long"
            "Names can include military titles or ranks"
            "Names can include numbers or symbols"
            "Names can include tech or science terms"
            ]
    elif genre == "Dark/Gritty":
        return rules + [
            "Names can be 1-3 words long",
            "Include occasional anti-hero names",
            "Include occasional dark or grim names",
            "Names can include violent or aggressive terms",
            "Names can include supernatural or occult terms",
            "Names can include criminal or underworld terms"
            ]
    elif genre == "Military":
        return rules + [
            "Names can be 1-4 words long",
            "Include occasional military unit names",
            "Include occasional military operation names",
            "Include occasional military rank names",
            "Include occasional military vehicle names",
            "Include occasional military weapon names",
            "Include occasional military term names"
            ]
    elif genre == "Urban Fantasy":
        return rules + [
            "Names can be 1-3 words long",
            "Include occasional magical creature names",
            "Include occasional magical weapon names",
            "Include occasional magical item names",
            "Include occasional magical term names",
            "Include occasional magical location names",
            "Include occasional magical event names"
            ]
    else:
        return rules + [
             "Names can be 1-3 words long",
        ]


def parse_naming_response(response: str) -> List[dict]:
    """Parse a response string into structured name data.

    Expected format:
    "name","tagline","description"

    Returns list of dicts with keys: name, tagline, description
    """
    results = []
    for line in response.strip().split('\n'):
        if not line.strip():
            continue

        try:
            reader = csv.reader([line])
            row = next(reader)

            if len(row) >= 3:
                results.append({
                    'name': row[0].strip(),
                    'tagline': row[1].strip(),
                    'description': row[2].strip()
                })
        except Exception:
            continue
    return results


class NameGenerator:
    def __init__(self):
        api_key = os.environ.get('PALM_API_KEY')
        if api_key:
            palm.configure(api_key=api_key)
            self.palm_model = palm.GenerativeModel('models/gemini-2.5-flash')
        else:
            self.palm_model = None
        self.used_names = []
        self.history = []

    def load_example_names(self, file_path: str) -> List[str]:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]

    def create_prompt(self, example_names: List[str], count: int = 1, genre: str = "Superhero") -> str:
        import random
        examples = "\n".join(f"- {line}" for line in random.choices(example_names, k=10))
        rule_list = naming_rules_by_genre(genre)
        rules = "\n".join(f"- {line}" for line in rule_list)
        prompt = f"""Task: Generate {count} unique superhero or supervillain names.

Use these examples as inspiration, but create new, original names:
{examples}

Rules:
{rules}
"""

        if self.used_names:
            if len(self.used_names) > 100:
                self.used_names = self.used_names[:100]
            prompt = f"{prompt}\n\nPreviously generated do not reuse:\n" + "\n".join(self.used_names)

        return prompt

    def generate_with_palm(self, prompt: str, count: int = 1) -> List[dict]:
        if not self.palm_model:
            raise ValueError("PALM_API_KEY not configured")

        response = self.palm_model.generate_content(prompt)
        return self.parse_and_add_to_history(response.text, count)

    def parse_and_add_to_history(self, response: str, count: int = 1) -> List[dict]:
        characters = parse_naming_response(response)
        names = [character['name'] for character in characters]
        self.used_names.extend(names[:count])
        rows = characters[:count]
        rows.extend(self.history)
        self.history = rows
        return rows


class CharacterGenerator:
    def __init__(self):
        api_key = os.environ.get('PALM_API_KEY')
        if api_key:
            palm.configure(api_key=api_key)
            self.palm_model = palm.GenerativeModel('models/gemini-2.5-flash')
        else:
            self.palm_model = None

    def generate(self, name: str, tagline: str, description: str, genre: str) -> dict:
        if not self.palm_model:
            raise ValueError("PALM_API_KEY not configured")

        rules = character_rules_by_genre(genre)
        prompt = f"""Task: Generate a detailed description of a superhero or supervillain using the following information:

Name: {name}
Tagline: {tagline}
Description: {description}

Rules:
{rules}
"""
        response = self.palm_model.generate_content(prompt)

        try:
            details = json.loads(response.text)
        except json.JSONDecodeError:
            details = {}

        details['name'] = name
        details['tagline'] = tagline
        details['description'] = description
        return details
