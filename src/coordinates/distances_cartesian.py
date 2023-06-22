"""Module for functions that calculate distances in cartesian coordinates."""
from decimal import Decimal
from typing import Callable, List, Tuple

MetricDistanceFn = Callable[[List[Decimal], List[Decimal], Decimal], Decimal]


def prepare_points_for_calcs(
    point_1: List[Decimal], point_2: List[Decimal]
) -> List[Decimal]:
    point: List[Tuple[Decimal, Decimal]] = list(zip(point_1, point_2))
    return [pair[-1] - pair[0] for pair in point]


def calculate_euclidean_distance_in_cartesian_coords(
    point_1: List[Decimal], point_2: List[Decimal], p: Decimal = Decimal(2)
) -> Decimal:
    """Usual Euclidean distance in cartesian coordinates"""
    coordinates: List[Decimal] = prepare_points_for_calcs(point_1, point_2)
    return Decimal(sum(c**p for c in coordinates))


def calculate_manhattan_distance_in_cartesian_coords(
    point_1: List[Decimal], point_2: List[Decimal], p: Decimal = Decimal(1)
) -> Decimal:
    """Calculates the taxicab distance between two points in cartesian"""
    coordinates: List[Decimal] = prepare_points_for_calcs(point_1, point_2)
    return Decimal(sum(abs(c**p) for c in coordinates))


def calculate_minkowski_distance_in_cartesian_coords(
    point_1: List[Decimal], point_2: List[Decimal], p: Decimal
) -> Decimal:
    """Calculates the minkowski distance betwen two points in cartesian"""
    coordinates: List[Decimal] = prepare_points_for_calcs(point_1, point_2)
    return Decimal(sum(abs(c) ** p for c in coordinates)) ** (1 / p)
