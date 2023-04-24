"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730408141"


class Simpy:
    """Simpy class."""

    values: list[float]

    def __init__(self, values_inp: list[float]):
        """Initialize a Simpy object."""
        self.values = values_inp

    def __str__(self) -> str:
        """Return a str of Simpy."""
        return (f"Simpy({self.values})")
    
    def fill(self, num_to_fill: float, num_fills: int) -> None:
        """Fill Simpy's values with a specific number."""
        while num_fills > 0:
            self.values.append(num_to_fill)
            num_fills -= 1
        return self

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill Simpy's values with a certain range."""
        assert step != 0.0
        while (step > 0 and start < stop) or (step < 0 and start > stop):
            self.values.append(start)
            start += step
        return self

    def sum(self) -> float:
        """Add Simpy's values together."""
        total: float = sum(self.values)
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload addition operator."""
        new_simpy: Simpy = Simpy([])
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] + rhs.values[idx])
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] + rhs)
        return new_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the power operator."""
        new_simpy: Simpy = Simpy([])
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] ** rhs.values[idx])
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] ** rhs)
        return new_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check for equalities."""
        equalities: list[bool] = []
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    equalities.append(True)
                else:
                    equalities.append(False)
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs:
                    equalities.append(True)
                else:
                    equalities.append(False)
        return equalities
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test for greater than with Simpy objects."""
        equalities: list[bool] = []
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    equalities.append(True)
                else:
                    equalities.append(False)
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs:
                    equalities.append(True)
                else:
                    equalities.append(False)
        return equalities
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allow subscription notation with Simpys."""
        if type(rhs) == int:
            return self.values[rhs]
        else:
            idx_item = Simpy([])
            for idx in range(0, len(self.values)):
                if rhs[idx]:
                    idx_item.values.append(self.values[idx])
            return idx_item