"""ICONS RPG Predefined Creatures."""

from .icons_kaiju import Monster
from .icons_characters import Abilities, Ability, Power, Specialty


def _ability(val: int) -> Ability:
    return Ability(base=val, level=val)


def _abilities(
    pro: int, coo: int, strength: int, intellect: int, awa: int, wil: int
) -> Abilities:
    return Abilities(
        prowess=_ability(pro),
        coordination=_ability(coo),
        strength=_ability(strength),
        intellect=_ability(intellect),
        awareness=_ability(awa),
        willpower=_ability(wil),
    )


def _power(name: str, level: int) -> Power:
    return Power(name=name, level=level, source="natural")


def _specialty(name: str, level: int) -> Specialty:
    return Specialty(name=name, level=level, source="natural")


def make_bear() -> Monster:
    return Monster(
        name="Bear",
        type=["Bear"],
        abilities=_abilities(4, 3, 6, 1, 3, 3),
        stamina=9,
        powers=[_power("Claws & Bite (Slashing)", 2)],
    )


def make_cat() -> Monster:
    return Monster(
        name="Cat",
        type=["Cat"],
        abilities=_abilities(2, 4, 0, 1, 3, 2),
        stamina=2,
        powers=[_power("Claws", 0)],
    )


def make_cheetah() -> Monster:
    return Monster(
        name="Cheetah",
        type=["Cat"],
        abilities=_abilities(4, 4, 3, 1, 4, 3),
        stamina=6,
        specialties=[_specialty("Running", 2)],
        powers=[_power("Claws & Bite", 3)],
    )


def make_crocodile() -> Monster:
    return Monster(
        name="Crocodile",
        type=["Crocodile"],
        abilities=_abilities(3, 2, 5, 1, 3, 2),
        stamina=7,
        powers=[_power("Bite (slashing)", 4)],
    )


def make_dog() -> Monster:
    return Monster(
        name="Dog",
        type=["Dog"],
        abilities=_abilities(2, 3, 2, 1, 3, 2),
        stamina=4,
        powers=[_power("Bite", 2)],
    )


def make_dog_guard() -> Monster:
    return Monster(
        name="Guard Dog",
        type=["Dog"],
        abilities=_abilities(3, 3, 3, 1, 3, 2),
        stamina=4,
        powers=[_power("Bite", 3)],
    )


def make_dolphin() -> Monster:
    return Monster(
        name="Dolphin",
        type=["Dolphin"],
        abilities=_abilities(3, 4, 3, 2, 4, 3),
        stamina=6,
        powers=[_power("Aquatic", 3), _power("Super-Sense (Sonar)", 1)],
    )


def make_eagle() -> Monster:
    return Monster(
        name="Eagle",
        type=["Eagle"],
        abilities=_abilities(3, 4, 1, 1, 5, 3),
        stamina=4,
        powers=[_power("Claws (Slashing)", 2), _power("Flight", 3)],
    )


def make_electric_eel() -> Monster:
    return Monster(
        name="Electric-Eel",
        type=["Electric-Eel"],
        abilities=_abilities(2, 3, 1, 0, 3, 2),
        stamina=3,
        powers=[_power("Aura (Electricity)", 3)],
    )


def make_elephant() -> Monster:
    return Monster(
        name="Elephant",
        type=["Elephant"],
        abilities=_abilities(3, 2, 7, 1, 3, 3),
        stamina=10,
        powers=[_power("Tusks (Slashing)", 4)],
    )


def make_gorilla() -> Monster:
    return Monster(
        name="Gorilla",
        type=["Gorilla"],
        abilities=_abilities(3, 4, 6, 1, 3, 3),
        stamina=9,
        specialties=[_specialty("Athletics", 1)],
    )


def make_hippo() -> Monster:
    return Monster(
        name="Hippo",
        type=["Hippo"],
        abilities=_abilities(3, 2, 6, 1, 3, 2),
        stamina=8,
        powers=[_power("Bite (Slashing)", 3)],
    )


def make_horse() -> Monster:
    return Monster(
        name="Horse",
        type=["Horse"],
        abilities=_abilities(2, 3, 6, 1, 3, 2),
        stamina=8,
        specialties=[_specialty("Running", 2)],
    )


def make_human() -> Monster:
    return Monster(
        name="Human",
        type=["Human", "Humanoid"],
        abilities=_abilities(3, 3, 3, 3, 3, 3),
        stamina=6,
    )


def make_lion() -> Monster:
    return Monster(
        name="Lion",
        type=["Lion"],
        abilities=_abilities(5, 4, 5, 1, 4, 3),
        stamina=8,
        powers=[_power("Claws & Bite (slashing)", 4)],
    )


def make_monkey() -> Monster:
    return Monster(
        name="Monkey",
        type=["Monkey"],
        abilities=_abilities(3, 6, 0, 1, 4, 3),
        stamina=3,
        specialties=[_specialty("Athletics", 1)],
        powers=[
            _power("Extra Limbs (prehensile tail)", 1),
            _power("Fast Attack (prehensile tail)", 1),
        ],
    )


def make_orca() -> Monster:
    return Monster(
        name="Orca",
        type=["Orca"],
        abilities=_abilities(4, 3, 7, 1, 3, 3),
        stamina=10,
        specialties=[_specialty("Wrestling", 2)],
        powers=[_power("Bite", 5), _power("Aquatic", 2)],
    )


def make_python() -> Monster:
    return Monster(
        name="Python",
        type=["Python"],
        abilities=_abilities(4, 4, 4, 1, 4, 2),
        stamina=6,
        specialties=[_specialty("Wrestling", 2)],
        powers=[_power("Bite (slashing)", 3)],
    )


def make_rhino() -> Monster:
    return Monster(
        name="Rhino",
        type=["Rhino"],
        abilities=_abilities(3, 2, 7, 1, 3, 3),
        stamina=10,
        powers=[_power("Gore (slashing)", 4)],
    )


def make_shark() -> Monster:
    return Monster(
        name="Shark",
        type=["Shark"],
        abilities=_abilities(5, 3, 5, 1, 4, 4),
        stamina=9,
        powers=[_power("Bite", 5), _power("Aquatic", 2)],
    )


def make_squid_giant() -> Monster:
    return Monster(
        name="Giant Squid",
        type=["Squid-Giant"],
        abilities=_abilities(4, 4, 8, 1, 3, 3),
        stamina=11,
        powers=[
            _power("Extra limbs (tentacles)", 1),
            _power("Elongation (tentacles)", 1),
            _power("Aquatic", 2),
        ],
    )


def make_swarm() -> Monster:
    return Monster(
        name="Insect Swarm",
        type=["Swarm"],
        abilities=_abilities(3, 4, 0, 0, 3, 0),
        stamina=3,
        powers=[_power("Stings", 1), _power("Gaseous Form", 4)],
    )


def make_viper() -> Monster:
    return Monster(
        name="Viper",
        type=["Viper"],
        abilities=_abilities(4, 5, 0, 1, 3, 2),
        stamina=2,
        powers=[_power("Bite", 0), _power("Affliction (poison)", 2)],
    )


def make_whale() -> Monster:
    return Monster(
        name="Whale",
        type=["Whale"],
        abilities=_abilities(3, 2, 8, 2, 3, 3),
        stamina=11,
        powers=[_power("Aquatic", 2), _power("Super-Sense (Sonar)", 1)],
    )


def make_wolf() -> Monster:
    return Monster(
        name="Wolf",
        type=["Wolf"],
        abilities=_abilities(4, 4, 3, 1, 4, 3),
        stamina=6,
        powers=[_power("Claws & Bite", 3)],
    )


def make_wolverine() -> Monster:
    return Monster(
        name="Wolverine",
        type=["Wolverine"],
        abilities=_abilities(5, 3, 3, 1, 4, 4),
        stamina=7,
        powers=[_power("Claws & Bite", 3)],
    )


def make_apatosaurus() -> Monster:
    return Monster(
        name="Apatosaurus",
        type=["Apatosaurus"],
        abilities=_abilities(1, 1, 9, 0, 3, 1),
        stamina=10,
    )


def make_deinonychus() -> Monster:
    return Monster(
        name="Deinonychus",
        type=["Deinonychus"],
        abilities=_abilities(4, 4, 5, 0, 4, 2),
        stamina=7,
        specialties=[_specialty("running", 2)],
        powers=[_power("Claws & Bite", 4)],
    )


def make_pterodactyl() -> Monster:
    return Monster(
        name="Pterodactyl",
        type=["Pterodactyl"],
        abilities=_abilities(3, 3, 5, 0, 4, 2),
        stamina=7,
        powers=[_power("Beak & Claws", 4), _power("Flight", 2)],
    )


def make_triceratops() -> Monster:
    return Monster(
        name="Triceratops",
        type=["Triceratops"],
        abilities=_abilities(4, 2, 7, 0, 4, 2),
        stamina=9,
        powers=[_power("Horns (slashing)", 4), _power("Armor Plates DR", 2)],
    )


def make_tyrannosaur() -> Monster:
    return Monster(
        name="Tyrannosaur",
        type=["Tyrannosaur"],
        abilities=_abilities(5, 3, 8, 0, 4, 3),
        stamina=11,
        specialties=[_specialty("running", 2)],
        powers=[_power("Bite (slashing)", 6)],
    )
