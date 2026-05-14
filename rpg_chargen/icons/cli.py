"""ICONS RPG CLI - Command line interface for generating characters and monsters."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from jinja2 import Environment, FileSystemLoader
from rich.console import Console

from .icons_characters import icons_random_super
from .icons_kaiju import make_random_kaiju
from .icons_creatures import (
    make_bear,
    make_cat,
    make_cheetah,
    make_crocodile,
    make_dog,
    make_dog_guard,
    make_dolphin,
    make_eagle,
    make_electric_eel,
    make_elephant,
    make_gorilla,
    make_hippo,
    make_horse,
    make_human,
    make_lion,
    make_monkey,
    make_orca,
    make_python,
    make_rhino,
    make_shark,
    make_squid_giant,
    make_swarm,
    make_viper,
    make_whale,
    make_wolf,
    make_wolverine,
    make_apatosaurus,
    make_deinonychus,
    make_pterodactyl,
    make_triceratops,
    make_tyrannosaur,
)

app = typer.Typer(
    name="icons-explorer",
    help="ICONS RPG Character and Monster Generator CLI",
    no_args_is_help=True,
)

console = Console()

TEMPLATES_DIR = Path(__file__).parent / "templates"

CREATURE_REGISTRY: dict[str, callable] = {
    "bear": make_bear,
    "cat": make_cat,
    "cheetah": make_cheetah,
    "crocodile": make_crocodile,
    "dog": make_dog,
    "guard-dog": make_dog_guard,
    "dolphin": make_dolphin,
    "eagle": make_eagle,
    "electric-eel": make_electric_eel,
    "elephant": make_elephant,
    "gorilla": make_gorilla,
    "hippo": make_hippo,
    "horse": make_horse,
    "human": make_human,
    "lion": make_lion,
    "monkey": make_monkey,
    "orca": make_orca,
    "python": make_python,
    "rhino": make_rhino,
    "shark": make_shark,
    "giant-squid": make_squid_giant,
    "swarm": make_swarm,
    "viper": make_viper,
    "whale": make_whale,
    "wolf": make_wolf,
    "wolverine": make_wolverine,
    "apatosaurus": make_apatosaurus,
    "deinonychus": make_deinonychus,
    "pterodactyl": make_pterodactyl,
    "triceratops": make_triceratops,
    "tyrannosaur": make_tyrannosaur,
}


def get_jinja_env() -> Environment:
    """Create and configure Jinja2 environment."""
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_character(super_obj: object) -> str:
    """Render a character using the Jinja2 template."""
    env = get_jinja_env()
    template = env.get_template("character.j2")
    return template.render(super=super_obj)


def render_monster(monster_obj: object) -> str:
    """Render a monster using the Jinja2 template."""
    env = get_jinja_env()
    template = env.get_template("monster.j2")
    return template.render(monster=monster_obj)


@app.command("character")
def generate_character(
    count: int = typer.Option(
        1, "--count", "-n", help="Number of characters to generate"
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Output file path"
    ),
) -> None:
    """Generate random ICONS superhero character(s)."""
    results: list[str] = []

    for i in range(count):
        character = icons_random_super()
        rendered = render_character(character)
        results.append(rendered)

        if count > 1 and i < count - 1:
            results.append("\n" + "=" * 40 + "\n")

    output_text = "".join(results)

    if output:
        output.write_text(output_text)
        console.print(f"[green]Generated {count} character(s) to {output}[/green]")
    else:
        console.print(output_text)


@app.command("monster")
def generate_monster(
    monster_type: str = typer.Argument(
        "kaiju",
        help="Type of monster: 'kaiju' or a creature name (e.g., 'bear', 'wolf', 'tyrannosaur')",
    ),
    count: int = typer.Option(
        1, "--count", "-n", help="Number of monsters to generate"
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Output file path"
    ),
    list_creatures: bool = typer.Option(
        False, "--list", "-l", help="List available creature types"
    ),
) -> None:
    """Generate ICONS monsters (kaiju or predefined creatures)."""
    if list_creatures:
        console.print("[bold]Available creature types:[/bold]")
        for name in sorted(CREATURE_REGISTRY.keys()):
            console.print(f"  - {name}")
        console.print("\n  - kaiju (random)")
        return

    results: list[str] = []

    for i in range(count):
        if monster_type == "kaiju":
            monster = make_random_kaiju()
        elif monster_type in CREATURE_REGISTRY:
            monster = CREATURE_REGISTRY[monster_type]()
        else:
            console.print(f"[red]Unknown monster type: {monster_type}[/red]")
            console.print("Use --list to see available creature types")
            raise typer.Exit(1)

        rendered = render_monster(monster)
        results.append(rendered)

        if count > 1 and i < count - 1:
            results.append("\n" + "=" * 40 + "\n")

    output_text = "".join(results)

    if output:
        output.write_text(output_text)
        console.print(f"[green]Generated {count} monster(s) to {output}[/green]")
    else:
        console.print(output_text)


@app.command("creatures")
def list_creatures() -> None:
    """List all available predefined creatures."""
    console.print("[bold]Available creatures:[/bold]\n")

    categories = {
        "Mammals": [
            "bear",
            "cat",
            "cheetah",
            "dog",
            "guard-dog",
            "elephant",
            "gorilla",
            "hippo",
            "horse",
            "human",
            "lion",
            "monkey",
            "rhino",
            "wolf",
            "wolverine",
        ],
        "Aquatic": [
            "crocodile",
            "dolphin",
            "electric-eel",
            "orca",
            "python",
            "shark",
            "giant-squid",
            "whale",
        ],
        "Birds": ["eagle"],
        "Reptiles/Other": ["swarm", "viper"],
        "Dinosaurs": [
            "apatosaurus",
            "deinonychus",
            "pterodactyl",
            "triceratops",
            "tyrannosaur",
        ],
    }

    for category, creatures in categories.items():
        console.print(f"[bold cyan]{category}:[/bold cyan]")
        for creature in creatures:
            console.print(f"  - {creature}")
        console.print()


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
