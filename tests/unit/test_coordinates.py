"""Test points, metric functions and coordinates"""
from decimal import Decimal
from typing import List

from src.coordinates.coordinates import Point


class TestPoint:
    """Class to Test Points"""

    def test_point_coordinates_property(self, one_point: Point):
        """Test coordinates property from Point class"""
        # GIVEN a point object
        # WHEN calling to its coordinates property
        # THEN the result should be a list of decimal numbers

        coords: List[Decimal] = one_point.coordinates
        assert isinstance(coords, List)
        assert coords == [Decimal(1)] * 3

    def test_point_str_dunder(self, one_point: Point):
        """Test __str__ method from Point class"""
        # GIVEN a point object
        # WHEN getting its string representation
        # THEN the result should be of the form: "Point: (c1, c2, c3)"

        assert str(one_point) == "Point: (1, 1, 1)"

    def test_sub_dunder_method(self, zero_point: Point, one_point: Point):
        """Test coordinates property from Point class"""
        # GIVEN two point objects
        # WHEN substracting them both
        # THEN the result should be a point whose coordinates
        #      are the difference of the points' coordinates
        new_point: Point = one_point - zero_point
        assert isinstance(new_point, Point)
        assert new_point.coordinates == one_point.coordinates

    
    def test_neg_dunder_method(self, one_point: Point):
        """Test coordinates property from Point class"""
        # GIVEN one point object
        # WHEN negating it
        # THEN the result should be a point whose coordinates
        #      are the opposite of the original points' coordinates
        new_point: Point = -one_point
        assert isinstance(new_point, Point)
        assert new_point.coord_1 == -one_point.coord_1
        assert new_point.coord_2 == -one_point.coord_2
        assert new_point.coord_2 == -one_point.coord_3

    def test_subtraction_is_anti_commutative(self, zero_point: Point, one_point: Point):
        """Test coordinates property from Point class"""
        # GIVEN two point objects p1 and p2
        # WHEN substracting them both in different order
        # THEN the result should be anti-conmmutative,
        # i.e. p1 - p2 = - (p2 - p1)
        assert (one_point - zero_point) == -(zero_point - one_point)
