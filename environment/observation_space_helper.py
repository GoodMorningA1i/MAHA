from typing import TYPE_CHECKING, Any, Generic, \
 SupportsFloat, TypeVar, Type, Optional, List, Dict, Callable
from typing import Tuple, Any
from dataclasses import dataclass, field, MISSING

import numpy as np

import gymnasium
from gymnasium import spaces

@dataclass
class ObsHelper():
    low: list[Any] = field(default_factory=list)
    high: list[Any] = field(default_factory=list)
    sections: Dict[str, Tuple[int, int]] = field(default_factory=dict)

    def get_as_np(self) -> Tuple[np.ndarray, np.ndarray]:
        """Return the low and high bounds as NumPy arrays."""
        return np.array(self.low), np.array(self.high)

    def get_as_box(self) -> spaces.Box:
        lowarray, higharray = self.get_as_np()
        return spaces.Box(
            low=lowarray,
            high=higharray,
            shape=lowarray.shape,
            dtype=np.float32
        )

    def zeros(self) -> np.ndarray:
        """
        Returns a zeros vector with the same total dimension as defined by the low vector.
        """
        return np.zeros(len(self.low))

    def add_section(self, low_values: List[Any], high_values: List[Any], name: str) :
        """
        Adds a new section with a label to the overall low and high lists.

        Parameters:
            name: A string that identifies the section (e.g., "global_position").
            low_values: A list of low values for this section.
            high_values: A list of high values for this section.

        The method appends the values to the overall lists and records the indices
        where this section is stored. This is later used for observation parsing.
        """
        name = name.lower()
        start_idx = len(self.low)  # Starting index for this section.
        self.low += low_values
        self.high += high_values
        end_idx = len(self.low)    # Ending index (exclusive) for this section.
        self.sections[name] = (start_idx, end_idx)

    def get_section(self, obs: np.ndarray, name: str) -> np.ndarray:
        start, end = self.sections[name]
        return obs[start:end]

    def print_all_sections(self) -> None:
        """
        Prints the names and indices of all sections.
        """
        for name, (start, end) in self.sections.items():
            print(f"{name}: {end - start}")