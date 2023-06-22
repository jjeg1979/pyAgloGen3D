"""Coordinates module.


    Includes Point and Coordinates classes.
    Includes CoordinateSystem Enum
"""

from dataclasses import dataclass
from typing import Callable, List, Self, Sequence
from decimal import Decimal
from enum import StrEnum, auto
from src.coordinates.distances_cartesian import (
    MetricDistanceFn,
    calculate_euclidean_distance_in_cartesian_coords,
    calculate_manhattan_distance_in_cartesian_coords,
    calculate_minkowski_distance_in_cartesian_coords,
)


class CoordinateSystem(StrEnum):
    """Enumeration for the coordinate systems."""

    CARTESIAN = auto()
    POLAR = auto()
    SPHERICAL = auto()


@dataclass
class Point:
    """Class to represent a generic point, regardless of the
    coordinate system."""

    coord_1: Decimal
    coord_2: Decimal
    coord_3: Decimal

    @property
    def coordinates(self) -> List[Decimal]:
        return [self.coord_1, self.coord_2, self.coord_3]

    def __str__(self) -> str:
        return f"Point: ({self.coord_1}, {self.coord_2}, {self.coord_3})"

    def __sub__(self, other_point: Self) -> Self:
        return Point(
            self.coord_1 - other_point.coord_1,
            self.coord_2 - other_point.coord_2,
            self.coord_3 - other_point.coord_3,
        )

    def __neg__(self) -> Self:
        return Point(-self.coord_1, -self.coord_2, -self.coord_3)

    def __eq__(self, other_point: Self) -> bool:
        return (
            self.coord_1 == other_point.coord_1
            and self.coord_2 == other_point.coord_2
            and self.coord_3 == other_point.coord_3
        )


ChangeCoordinateSystemFn = Callable[
    [Sequence[Decimal], CoordinateSystem], List[Decimal]
]

""" TODO: Include a dictionary with approved methods to calculate metrics
          depending upon coordinate systems."""

METRICS_IN_CARTESIAN: dict[str, MetricDistanceFn] = {
    "euclidean": calculate_euclidean_distance_in_cartesian_coords,
    "manhattan": calculate_manhattan_distance_in_cartesian_coords,
    "minkowski": calculate_minkowski_distance_in_cartesian_coords,
}


@dataclass
class Coordinates:
    """Class for representing point coordinates"""

    point: Point
    coordinate_system: CoordinateSystem = CoordinateSystem.CARTESIAN

    def calculate_distance_to(
        self, other_coordinate: Self, distance_fun: MetricDistanceFn, p: Decimal
    ) -> Decimal:
        """Method to calculate the distance to another point."""
        return distance_fun(
            self.point.coordinates, other_coordinate.point.coordinates, p
        )

    def change_to_coordinate_sytem(self, other_coord_system: CoordinateSystem) -> None:
        """Method to change coordinates to a different coordinate system."""
