"""Entry point."""

from decimal import Decimal
from src.coordinates.coordinates import (
    Point,
    Coordinates,
    CoordinateSystem,
)

NUM_POINT = Decimal(1)


def main() -> None:
    """Main Function"""
    point = Point(NUM_POINT, NUM_POINT, NUM_POINT)
    coord_system = CoordinateSystem.CARTESIAN
    coordinates = Coordinates(point=point, coordinate_system=coord_system)
    print(point)
    print(coord_system.value)
    print(coordinates)


if __name__ == "__main__":
    main()
