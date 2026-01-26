"""ICONS RPG Character Generator."""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Optional

from .name_generator import random_super_name
from .data.power_tables import (
    LEVEL_TABLE,
    ORIGINS_TABLE,
    POWER_GROUPS,
    POWER_ALTERATION,
    POWER_CONTROL,
    POWER_DEFENSIVE,
    POWER_MENTAL,
    POWER_MOVEMENT,
    POWER_OFFENSIVE,
    POWER_SENSORY,
    POWER_COUNT_TABLE,
    SPECIALTIES_TABLE,
    BG_GENDER,
    BG_ETHNICITY,
    BG_SUPER_AGE,
    BG_MANNER,
    BG_WHO_VALUE,
    BG_ATTITUDE,
    BG_BIRTH_PLACE,
    BG_BIRTH_STATUS,
    BG_FAMILY_TRAGEDIES,
    BG_PAST_EXPERIENCE_TYPE,
    BG_FRIEND_FOE_RELATIONSHIP,
    BG_PAST_GOOD_EXPERIENCE,
    BG_PAST_BAD_EXPERIENCE,
)


def d4() -> int:
    return random.randint(1, 4)


def d6() -> int:
    return random.randint(1, 6)


def two_d6() -> int:
    return d6() + d6()


def d10() -> int:
    return random.randint(0, 9)


@dataclass
class Power:
    name: str
    group: str = ""
    level: int = 1
    enhancement: Optional[str] = None
    limit: Optional[str] = None
    source: str = "innate"

    def __repr__(self) -> str:
        return f"Power({self.name}, level={self.level}, group={self.group})"


@dataclass
class Modifier:
    delta: int = 0
    reason: str = ""


@dataclass
class Ability:
    base: int = 3
    modifiers: list[Modifier] = field(default_factory=list)
    level: int = 3

    def add_modifier(self, mod: Modifier) -> None:
        self.modifiers.append(mod)
        total_mods = sum(m.delta for m in self.modifiers)
        self.level = min(10, self.base + total_mods)


ORIGIN_ABILITY_MODIFIERS: dict[str, dict[str, Modifier]] = {
    "artificial": {"strength": Modifier(2, "Artificial Origin")},
    "kaiju": {
        "strength": Modifier(3, "Kaiju Origin"),
        "prowess": Modifier(3, "Kaiju Origin"),
    },
}


def get_ability_modifier(origin: str, key: str) -> Optional[Modifier]:
    origin_mods = ORIGIN_ABILITY_MODIFIERS.get(origin)
    if origin_mods:
        return origin_mods.get(key)
    return None


def make_ability(level: int, origin: Optional[str] = None, key: Optional[str] = None) -> Ability:
    effective = min(10, level)
    ability = Ability(base=effective, level=effective)
    
    if origin and key:
        mod = get_ability_modifier(origin, key)
        if mod:
            ability.add_modifier(mod)
    
    return ability


@dataclass
class Abilities:
    prowess: Ability = field(default_factory=lambda: Ability())
    strength: Ability = field(default_factory=lambda: Ability())
    coordination: Ability = field(default_factory=lambda: Ability())
    intellect: Ability = field(default_factory=lambda: Ability())
    awareness: Ability = field(default_factory=lambda: Ability())
    willpower: Ability = field(default_factory=lambda: Ability())


@dataclass
class Specialty:
    name: str
    level: int = 1
    source: str = "background"


@dataclass
class PastExperience:
    type: str
    description: str


@dataclass
class Super:
    name: str = "Unnamed"
    origin: str = ""
    abilities: Abilities = field(default_factory=Abilities)
    stamina: int = 0
    powers: list[Power] = field(default_factory=list)
    determination: int = 1
    specialties: list[Specialty] = field(default_factory=list)
    knacks: list[str] = field(default_factory=list)
    gender: str = ""
    ethnicity: str = ""
    age: tuple[str, int] = ("Adult", 25)
    attitude: str = ""
    manner: str = ""
    who_value: str = ""
    birth_place: str = ""
    birth_status: str = ""
    tragedy: Optional[str] = None
    past: list[PastExperience] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.stamina == 0:
            self.stamina = self.abilities.willpower.level + self.abilities.strength.level

    def __repr__(self) -> str:
        return f"Super({self.name}, Origin: {self.origin})"


LEVELS_DESCRIPTIONS = [
    "Weak", "Poor", "Average", "Fair", "Good",
    "Great", "Incredible", "Amazing", "Fantastic", "Supreme",
]


def icons_level_description(level: int) -> str:
    return LEVELS_DESCRIPTIONS[level - 1] if 1 <= level <= 10 else "Unknown"


def icons_random_level() -> int:
    roll = two_d6()
    result: int = LEVEL_TABLE.lookup(roll)
    return result


def icons_random_origin() -> str:
    roll = two_d6()
    result: str = ORIGINS_TABLE.lookup(roll)
    return result


def icons_random_abilities(origin: str) -> Abilities:
    return Abilities(
        prowess=make_ability(icons_random_level(), origin, "prowess"),
        strength=make_ability(icons_random_level(), origin, "strength"),
        coordination=make_ability(icons_random_level(), origin, "coordination"),
        intellect=make_ability(icons_random_level(), origin, "intellect"),
        awareness=make_ability(icons_random_level(), origin, "awareness"),
        willpower=make_ability(icons_random_level(), origin, "willpower"),
    )


def icons_random_power_group() -> str:
    roll = two_d6()
    result: str = POWER_GROUPS.lookup(roll)
    return result


def _get_power_table(group: str) -> Any:
    tables = {
        "alteration": POWER_ALTERATION,
        "control": POWER_CONTROL,
        "defensive": POWER_DEFENSIVE,
        "mental": POWER_MENTAL,
        "movement": POWER_MOVEMENT,
        "offensive": POWER_OFFENSIVE,
        "sensory": POWER_SENSORY,
    }
    return tables.get(group)


def icons_random_group_power(group: str) -> str:
    power_table = _get_power_table(group)
    if power_table is None:
        return "Unknown Power"
    roll = (d6(), d6())
    result: str = power_table.lookup(roll)
    return result


def icons_random_powersource(origin: Optional[str] = None) -> str:
    if origin == "gimmick":
        return "device"
    if origin == "monster":
        return "innate"
    return "device" if two_d6() < 5 else "innate"


def icons_random_power(origin: Optional[str] = None) -> Power:
    group = icons_random_power_group()
    return Power(
        name=icons_random_group_power(group),
        group=group,
        level=icons_random_level(),
        source=icons_random_powersource(origin),
    )


def icons_random_power_count() -> int:
    roll = two_d6()
    result: int = POWER_COUNT_TABLE.lookup(roll)
    return result


def icons_random_powerset(origin: Optional[str] = None) -> list[Power]:
    count = icons_random_power_count()
    return [icons_random_power(origin) for _ in range(count)]


def icons_random_specialty() -> str:
    roll = (d6(), d6())
    result: str = SPECIALTIES_TABLE.lookup(roll)
    return result


def icons_random_specialty_count(origin: str) -> int:
    count = icons_random_power_count() - 1
    if origin == "trained":
        count += 2
    return max(1, count)


def icons_random_specialties(origin: str) -> list[Specialty]:
    count = icons_random_specialty_count(origin)
    specs = [icons_random_specialty() for _ in range(count)]
    spec_counts = Counter(specs)
    return [
        Specialty(name=name, source="background", level=lvl)
        for name, lvl in spec_counts.items()
    ]


def ability_super_p(ability: Ability) -> bool:
    return ability.level > 7


def icons_ability_super_count(abilities: Abilities) -> int:
    all_abilities = [
        abilities.prowess,
        abilities.strength,
        abilities.coordination,
        abilities.intellect,
        abilities.awareness,
        abilities.willpower,
    ]
    return sum(1 for a in all_abilities if ability_super_p(a))


def calculate_determination(powers: list[Power], abilities: Abilities) -> int:
    count = len(powers) + icons_ability_super_count(abilities)
    return max(1, 6 - count)


def icons_random_gender() -> str:
    result: str = BG_GENDER.lookup(two_d6())
    return result


def icons_random_ethnicity(recursing: bool = False) -> str | list[str]:
    roll = two_d6()
    ethnicity: str = BG_ETHNICITY.lookup(roll)
    
    if recursing or roll < 12:
        return ethnicity
    
    results: list[str] = []
    while True:
        next_eth = icons_random_ethnicity(True)
        if isinstance(next_eth, str):
            if next_eth in results:
                break
            results.append(next_eth)
    return results if len(results) > 1 else (results[0] if results else ethnicity)


def icons_random_age() -> tuple[str, int]:
    roll = two_d6()
    delta = two_d6()
    age_data = BG_SUPER_AGE.lookup(roll)
    return (age_data[0], age_data[1] + delta)


def icons_random_manner() -> str:
    result: str = BG_MANNER.lookup(two_d6())
    return result


def icons_random_who_value() -> str:
    result: str = BG_WHO_VALUE.lookup(two_d6())
    return result


def icons_random_attitude() -> str:
    result: str = BG_ATTITUDE.lookup(two_d6())
    return result


def icons_random_birth_place() -> str:
    result: str = BG_BIRTH_PLACE.lookup(d6())
    return result


def icons_random_birth_status() -> str:
    result: str = BG_BIRTH_STATUS.lookup(two_d6())
    return result


def icons_random_tragedy_result() -> str:
    roll = d6()
    if roll > 5:
        return " is imprisoned."
    return " escaped and is in hiding."


def icons_random_tragedy() -> Optional[str]:
    if d6() > 3:
        return None
    
    scope_roll = d6()
    roll1 = d6()
    roll2 = d6()
    
    tragedy: str = BG_FAMILY_TRAGEDIES.lookup((roll1, roll2))
    
    prefix = (
        "The character's entire family was "
        if scope_roll > 4
        else "One or more family members were "
    )
    
    if roll1 > 3 and roll2 == 1:
        return prefix + tragedy + icons_random_tragedy_result()
    return prefix + tragedy


def icons_random_friend_foe() -> PastExperience:
    is_friend = d6() > 4
    type_str = "friend" if is_friend else "foe"
    type_label = "Friend" if is_friend else "Foe"
    relationship = BG_FRIEND_FOE_RELATIONSHIP.lookup(d6())
    return PastExperience(type=type_str, description=f"{type_label} {relationship}")


def icons_random_good_experience() -> PastExperience:
    return PastExperience(
        type="good_experience",
        description=BG_PAST_GOOD_EXPERIENCE.lookup(d6()),
    )


def icons_random_bad_experience() -> PastExperience:
    return PastExperience(
        type="bad_experience",
        description=BG_PAST_BAD_EXPERIENCE.lookup(d6()),
    )


def icons_random_past_experience() -> PastExperience:
    exp_type = BG_PAST_EXPERIENCE_TYPE.lookup(d6())
    
    if exp_type == "friend_foe":
        return icons_random_friend_foe()
    elif exp_type == "good_experience":
        return icons_random_good_experience()
    else:
        return icons_random_bad_experience()


def icons_random_past_experience_count(age: int) -> int:
    roll = two_d6()
    cap = age - 15
    return min(roll, max(0, cap))


def icons_random_past_experience_set(age: int) -> list[PastExperience]:
    count = icons_random_past_experience_count(age)
    return [icons_random_past_experience() for _ in range(count)]


def icons_random_super() -> Super:
    origin = icons_random_origin()
    powers = icons_random_powerset(origin)
    abilities = icons_random_abilities(origin)
    age = icons_random_age()
    
    stamina = abilities.willpower.level + abilities.strength.level
    determination = calculate_determination(powers, abilities)
    
    return Super(
        name=random_super_name(),
        origin=origin,
        abilities=abilities,
        stamina=stamina,
        powers=powers,
        determination=determination,
        specialties=icons_random_specialties(origin),
        gender=icons_random_gender(),
        ethnicity=icons_random_ethnicity(),  # type: ignore
        age=age,
        attitude=icons_random_attitude(),
        manner=icons_random_manner(),
        who_value=icons_random_who_value(),
        birth_place=icons_random_birth_place(),
        birth_status=icons_random_birth_status(),
        tragedy=icons_random_tragedy(),
        past=icons_random_past_experience_set(age[1]),
    )
