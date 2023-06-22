from decimal import Decimal

import pytest

from src.coordinates.coordinates import Point


ZERO_DEC = Decimal(0)


@pytest.fixture()
def zero_point() -> Point:
    return Point(ZERO_DEC, ZERO_DEC, ZERO_DEC)


@pytest.fixture()
def one_point() -> Point:
    return Point(Decimal(1), Decimal(1), Decimal(1))
