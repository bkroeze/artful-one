"""ICONS RPG Kaiju Monster Generator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .icons_characters import (
    Abilities,
    Power,
    Specialty,
    d6,
    icons_random_abilities,
    icons_random_power,
)
from .data.power_tables import KAIJU_TYPE, KAIJU_FEATURES, KAIJU_MOTIVATIONS


@dataclass
class Monster:
    name: str = "Unnamed"
    abilities: Abilities = field(default_factory=Abilities)
    type: list[str] = field(default_factory=list)
    features: list[str] = field(default_factory=list)
    stamina: int = 0
    specialties: Optional[list[Specialty]] = None
    powers: Optional[list[Power]] = None

    def __repr__(self) -> str:
        return f"Monster({self.name}, type={self.type})"


def roll_and_repeat(wild: int = 6) -> list[int]:
    """Roll d6, if result equals wild, roll again and add to list. Max 10 iterations."""
    results: list[int] = []
    last = wild
    for _ in range(10):
        roll = d6()
        results.append(roll)
        if roll != last:
            break
        last = roll
    return results


def icons_random_kaiju_type() -> list[str]:
    """Generate kaiju type(s) using roll-and-repeat."""
    rolls = roll_and_repeat(6)
    result: list[str] = KAIJU_TYPE.multiple_lookup(rolls)
    return result


def icons_random_kaiju_features() -> list[str]:
    """Generate kaiju features using roll-and-repeat."""
    rolls = roll_and_repeat(6)
    result: list[str] = KAIJU_FEATURES.multiple_lookup(rolls)
    return result


def icons_random_kaiju_motivation() -> str:
    """Generate a random kaiju motivation."""
    result: str = KAIJU_MOTIVATIONS.lookup(d6())
    return result


def icons_random_kaiju_powers(count: int) -> list[Power]:
    """Generate random powers for a kaiju."""
    return [icons_random_power("monster") for _ in range(count)]


def make_random_kaiju() -> Monster:
    """Generate a random kaiju monster."""
    types = icons_random_kaiju_type()
    abilities = icons_random_abilities("kaiju")
    stamina = abilities.willpower.level + abilities.strength.level
    features = icons_random_kaiju_features()

    power_count = len(features) + len(types)
    powers = icons_random_kaiju_powers(power_count)

    return Monster(
        name="Kaiju: ???",
        abilities=abilities,
        type=types,
        features=features,
        powers=powers,
        stamina=stamina,
    )
