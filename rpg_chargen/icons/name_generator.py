"""Superhero name generator."""

import random

from .data.power_tables import (
    NAMES1,
    NAMES2,
    NAMES3,
    NAMES4,
    NAMES5,
    NAMES6,
    NAMES_TYPE_TABLE,
)


def random_super_name_type_a() -> str:
    """Generate a Type A name: names1 + names2."""
    return f"{random.choice(NAMES1)} {random.choice(NAMES2)}"


def random_super_name_type_b() -> str:
    """Generate a Type B name: names3 + names4 + names5."""
    parts = [random.choice(NAMES3), random.choice(NAMES4), random.choice(NAMES5)]
    return " ".join(p for p in parts if p).strip()


def random_super_name_type_c() -> str:
    """Generate a Type C name: pick from names6."""
    return random.choice(NAMES6)


def random_super_name() -> str:
    """Generate a random superhero name."""
    roll = random.randint(1, 10)
    name_type = NAMES_TYPE_TABLE.lookup(roll)

    if name_type == "NAMES_A":
        return random_super_name_type_a()
    elif name_type == "NAMES_B":
        return random_super_name_type_b()
    else:  # NAMES_C
        return random_super_name_type_c()
