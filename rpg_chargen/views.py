"""Views for RPG Character Generator app."""

import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rpg_chargen.generator import NameGenerator, CharacterGenerator, GENRES


def supers_page(request):
    """Main superhero character generator page."""
    context = {
        'genres': GENRES,
    }
    return render(request, 'rpg_chargen/supers.html', context)


@csrf_exempt
def htmx_generate_names(request):
    """HTMX endpoint to generate superhero/supervillain names.

    POST parameters:
    - num_names: Number of names to generate (1-5)
    - genre: Genre of names (Superhero, Dark/Gritty, Military, Sci-Fi, Urban Fantasy)

    Returns:
        HTML fragment with generated characters table
    """
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    try:
        num_names = int(request.POST.get("num_names", 3))
        genre = request.POST.get("genre", "Superhero")

        # Validate parameters
        num_names = max(1, min(5, num_names))
        if genre not in GENRES:
            genre = GENRES[0]

        # Get the data file path
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        example_file = os.path.join(data_dir, 'supernames.csv')

        # Generate names
        generator = NameGenerator()
        example_names = generator.load_example_names(example_file)
        prompt = generator.create_prompt(example_names, num_names, genre)
        characters = generator.generate_with_palm(prompt, num_names)

        context = {
            'characters': characters,
            'genre': genre,
        }

        return render(request, 'rpg_chargen/partials/characters_table.html', context)

    except Exception as e:
        return HttpResponse(
            f'<div class="ui error message">Error generating names: {str(e)}</div>',
            status=500
        )


@csrf_exempt
def htmx_generate_details(request):
    """HTMX endpoint to generate detailed character information.

    POST parameters:
    - character_name: Name of the character
    - tagline: Tagline for the character
    - description: Description of the character
    - genre: Genre of the character

    Returns:
        HTML fragment with detailed character information
    """
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    try:
        character_name = request.POST.get("character_name", "")
        tagline = request.POST.get("tagline", "")
        description = request.POST.get("description", "")
        genre = request.POST.get("genre", "Superhero")

        if not all([character_name, tagline, description]):
            return HttpResponse(
                '<div class="ui error message">Missing required character information</div>',
                status=400
            )

        # Generate character details
        char_generator = CharacterGenerator()
        details = char_generator.generate(character_name, tagline, description, genre)

        context = {
            'character': details,
        }

        return render(request, 'rpg_chargen/partials/character_details.html', context)

    except Exception as e:
        return HttpResponse(
            f'<div class="ui error message">Error generating character details: {str(e)}</div>',
            status=500
        )
