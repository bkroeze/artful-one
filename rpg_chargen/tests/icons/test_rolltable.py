"""Tests for the rolltable module."""

import pytest

from icons_rpg.rolltable import (
    RollTable,
    rolltable_factory,
    rolltable_lookup,
    pair_equal_or_less,
)


def test_pair_equal_or_less():
    assert pair_equal_or_less((1, 1), (2, 2)) is True
    assert pair_equal_or_less((2, 2), (1, 1)) is False
    assert pair_equal_or_less((2, 1), (2, 2)) is True
    assert pair_equal_or_less((2, 2), (2, 1)) is False
    assert pair_equal_or_less((1, 1), (1, 2)) is True
    assert pair_equal_or_less((1, 2), (1, 1)) is False


def test_simple_rolltable():
    table = rolltable_factory([])
    assert isinstance(table, RollTable)


def test_rolltable_defaults():
    table = rolltable_factory([])
    assert table.dice == 2


def test_rolltable_lookups_single_die():
    table = rolltable_factory(
        [(1, "one"), (2, "two"), (4, "four"), (6, "six")],
        dice=1,
    )
    results = [rolltable_lookup(table, i) for i in range(1, 7)]
    assert results == ["one", "two", "four", "four", "six", "six"]


def test_rolltable_lookups_dual_die():
    table = rolltable_factory(
        [
            ((1, 2), "1-2"),
            ((1, 3), "1-3"),
            ((1, 6), "1-6"),
            ((2, 6), "2-6"),
            ((6, 1), "6-1"),
            ((6, 6), "6-6"),
        ],
        dice=2,
    )
    
    expected = [
        ["1-2", "1-2", "1-3", "1-6", "1-6", "1-6"],
        ["2-6", "2-6", "2-6", "2-6", "2-6", "2-6"],
        ["6-1", "6-6", "6-6", "6-6", "6-6", "6-6"],
        ["6-1", "6-6", "6-6", "6-6", "6-6", "6-6"],
        ["6-1", "6-6", "6-6", "6-6", "6-6", "6-6"],
        ["6-1", "6-6", "6-6", "6-6", "6-6", "6-6"],
    ]
    
    results = [
        [rolltable_lookup(table, (roll1, roll2)) for roll2 in range(1, 7)]
        for roll1 in range(1, 7)
    ]
    assert results == expected


def test_rolltable_level_table():
    table = rolltable_factory(
        [(2, 1), (3, 2), (4, 3), (6, 4), (8, 5), (10, 6), (11, 7), (12, 8)],
        dice=1,
    )
    assert rolltable_lookup(table, 2) == 1
    assert rolltable_lookup(table, 3) == 2
    assert rolltable_lookup(table, 5) == 4
    assert rolltable_lookup(table, 7) == 5
    assert rolltable_lookup(table, 12) == 8
