"""Roll table system for dice-based lookups."""

from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Sequence, TypeVar, Union

RollValue = Union[int, tuple[int, int]]
T = TypeVar("T")


def pair_equal_or_less(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """Check if pair a is <= pair b in both components."""
    return a[0] <= b[0] and a[1] <= b[1]


@dataclass
class RollTable:
    """A lookup table for dice rolls.
    
    For single die (dice=1): keys are max values (e.g., key=3 matches rolls 1-3)
    For dual die (dice=2): keys are (x,y) pairs, matches using pair_equal_or_less
    """
    table: dict[RollValue, Any] = field(default_factory=dict)
    dice: int = 2
    roller: Optional[Callable[[], RollValue]] = None

    def _sorted_keys(self) -> list[RollValue]:
        """Sort keys appropriately based on dice count."""
        keys = list(self.table.keys())
        if self.dice == 1:
            return sorted(keys)  # type: ignore
        else:
            return sorted(keys, key=lambda k: (k[0], k[1]))  # type: ignore

    def lookup(self, roll: RollValue) -> Any:
        """Get the table entry for a roll.
        
        For single die: finds first key >= roll
        For dual die: finds first key where pair_equal_or_less(roll, key)
        """
        sorted_keys = self._sorted_keys()
        
        if self.dice == 1:
            for key in sorted_keys:
                if roll <= key:  # type: ignore
                    return self.table[key]
        else:
            for key in sorted_keys:
                if pair_equal_or_less(roll, key):  # type: ignore
                    return self.table[key]
        
        return None

    def multiple_lookup(self, rolls: Sequence[RollValue]) -> list[Any]:
        """Lookup multiple rolls and return list of results."""
        return [self.lookup(r) for r in rolls]


def rolltable_factory(
    alist: list[tuple[RollValue, Any]],
    dice: int = 2,
    roller: Optional[Callable[[], RollValue]] = None,
) -> RollTable:
    """Create a RollTable from an association list."""
    table = {key: value for key, value in alist}
    return RollTable(table=table, dice=dice, roller=roller)


def rolltable_lookup(table: RollTable, roll: RollValue) -> Any:
    """Lookup a value in a rolltable."""
    return table.lookup(roll)
