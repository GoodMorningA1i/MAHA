from typing import TYPE_CHECKING, Any, Generic, \
 SupportsFloat, TypeVar, Type, Optional, List, Dict, Callable
from typing import Tuple, Any
from dataclasses import dataclass, field, MISSING

import numpy as np

import gymnasium
from gymnasium import spaces

@dataclass
class ActHelper():
    low: list[Any] = field(default_factory=list)
    high: list[Any] = field(default_factory=list)
    sections: Dict[str, int] = field(default_factory=dict)

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

    def add_key(self, name: str):
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
        self.low += [0]
        self.high += [1]
        self.sections[name] = len(self.low)-1

    def press_keys(self, keys: str | List[str], action: Optional[np.ndarray]=None) -> np.ndarray:
        """
        Set a part of the action vector corresponding to the named section.

        Parameters:
            action: The full action vector (np.ndarray) that will be modified.
            partial_action: The values to set for the section.
            name: The section name whose slice is to be replaced.

        Returns:
            The updated action vector.

        Raises:
            ValueError: If the partial action's size does not match the section size.
        """
        if isinstance(keys, str):
            keys = [keys]
        if action is None:
            action = self.zeros()

        for key in keys:
            key = key.lower()
            if key not in self.sections:
                raise KeyError(f"Key '{key}' not found in keys: {self.sections.keys()}")
            action[self.sections[key]] = 1
        return action

    def print_all_sections(self) -> None:
        """
        Prints the names and indices of all sections.
        """
        for name, (start, end) in self.sections.items():
            print(f"{name}: {end - start}")