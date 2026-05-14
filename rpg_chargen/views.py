"""Views for RPG Character Generator app."""

import logging
import os
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt

from rpg_chargen.generator import NameGenerator, CharacterGenerator, GENRES

log = logging.getLogger(__name__)


def _summarize_exception(exc):
    """Return a concise exception summary for logs without traceback text."""
    message = str(exc).strip()
    if len(message) > 500:
        message = message[:497] + "..."
    return {
        "type": exc.__class__.__name__,
        "message": message or repr(exc),
    }


def _generation_error_response(action, error_id):
    """HTML fragment HTMX can swap into the target panel."""
    return HttpResponse(
        (
            '<div class="ui error message" role="alert">'
            f"<div class=\"header\">Could not {escape(action)}</div>"
            "<p>The model request failed before a usable result was returned. "
            "Please try again in a moment.</p>"
            f"<p><small>Error reference: {escape(error_id)}</small></p>"
            "</div>"
        ),
        status=200,
    )


def _log_generation_exception(action, request, exc, **context):
    error_id = uuid.uuid4().hex[:12]
    exc_summary = _summarize_exception(exc)
    request_context = {
        "path": request.path,
        "is_htmx": request.headers.get("HX-Request") == "true",
        "user_agent": request.headers.get("User-Agent", "")[:200],
        **context,
    }
    log.exception(
        "RPG chargen %s failed error_id=%s exception_type=%s exception_message=%r context=%r",
        action,
        error_id,
        exc_summary["type"],
        exc_summary["message"],
        request_context,
    )
    return error_id


def supers_page(request):
    """Main superhero character generator page."""
    context = {
        "genres": GENRES,
    }
    return render(request, "rpg_chargen/supers.html", context)


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
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        example_file = os.path.join(data_dir, "supernames.csv")

        # Generate names
        generator = NameGenerator()
        example_names = generator.load_example_names(example_file)
        prompt = generator.create_prompt(example_names, num_names, genre)
        characters = generator.generate_with_llm(prompt, num_names)

        context = {
            "characters": characters,
            "genre": genre,
        }

        return render(request, "rpg_chargen/partials/characters_table.html", context)

    except Exception as e:
        error_id = _log_generation_exception(
            "name generation",
            request,
            e,
            endpoint="htmx_generate_names",
            num_names=request.POST.get("num_names"),
            genre=request.POST.get("genre"),
        )
        return _generation_error_response("generate names", error_id)


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
                status=400,
            )

        # Generate character details
        char_generator = CharacterGenerator()
        details = char_generator.generate(character_name, tagline, description, genre)

        context = {
            "character": details,
            "genre": genre,
        }

        return render(request, "rpg_chargen/partials/character_details.html", context)

    except Exception as e:
        error_id = _log_generation_exception(
            "character detail generation",
            request,
            e,
            endpoint="htmx_generate_details",
            character_name=request.POST.get("character_name"),
            genre=request.POST.get("genre"),
            tagline_length=len(request.POST.get("tagline", "")),
            description_length=len(request.POST.get("description", "")),
        )
        return _generation_error_response("generate character details", error_id)


def icons_page(request):
    """Main ICONS RPG character and monster generator page."""
    from rpg_chargen.icons import CREATURE_REGISTRY

    context = {
        "creature_types": sorted(CREATURE_REGISTRY.keys()),
    }
    return render(request, "rpg_chargen/icons.html", context)


def icons_render_character(char):
    """Render character using Jinja2 template."""
    from pathlib import Path
    from jinja2 import Environment, FileSystemLoader

    templates_dir = Path(__file__).parent / "icons" / "templates"
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("character.j2")
    return template.render(super=char)


def icons_render_monster(monster):
    """Render monster using Jinja2 template."""
    from pathlib import Path
    from jinja2 import Environment, FileSystemLoader

    templates_dir = Path(__file__).parent / "icons" / "templates"
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("monster.j2")
    return template.render(monster=monster)


@csrf_exempt
def icons_htmx_generate(request):
    """HTMX endpoint to generate ICONS characters or monsters.

    POST parameters:
    - entity_type: "character" or "monster"
    - monster_type: "kaiju" or specific creature name (if entity_type is "monster")
    - count: Number to generate (1-10)

    Returns:
        HTML fragment with generated entities
    """
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    try:
        from rpg_chargen.icons import (
            icons_random_super,
            make_random_kaiju,
            CREATURE_REGISTRY,
        )

        entity_type = request.POST.get("entity_type", "character")
        count = int(request.POST.get("count", 1))
        count = max(1, min(10, count))  # Clamp between 1-10

        entities = []

        if entity_type == "character":
            # Generate characters
            for _ in range(count):
                char = icons_random_super()
                text_version = icons_render_character(char)
                entities.append(
                    {
                        "type": "character",
                        "data": char,
                        "text": text_version,
                    }
                )
        else:
            # Generate monsters
            monster_type = request.POST.get("monster_type", "kaiju")

            for _ in range(count):
                if monster_type == "kaiju":
                    monster = make_random_kaiju()
                else:
                    # Get specific creature generator
                    creature_func = CREATURE_REGISTRY.get(monster_type)
                    if creature_func:
                        monster = creature_func()
                    else:
                        monster = make_random_kaiju()  # Fallback

                text_version = icons_render_monster(monster)
                entities.append(
                    {
                        "type": "monster",
                        "data": monster,
                        "text": text_version,
                    }
                )

        context = {
            "entities": entities,
            "entity_type": entity_type,
        }

        return render(request, "rpg_chargen/partials/icons_results.html", context)

    except Exception as e:
        log.exception("Error generating ICONS entities")
        return HttpResponse(
            f'<div class="ui error message">Error generating: {str(e)}</div>',
            status=500,
        )
