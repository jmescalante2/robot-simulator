import pytest

from robot_simulator.point import Point


@pytest.mark.parametrize(
    "point1,point2,expected_result",
    [
        (Point(1, 2), Point(3, 4), Point(4, 6)),
        (Point(-1, -2), Point(1, 2), Point(0, 0)),
        (Point(0, 0), Point(0, 0), Point(0, 0)),
    ],
)
def test_point_addition(point1, point2, expected_result):
    """Test if adding two Points results in the correct Point."""
    assert point1 + point2 == expected_result, f"Failed to add {point1} and {point2}"


# Test data for checking if a point is on the table
@pytest.mark.parametrize(
    "point,expected",
    [
        (Point(1, 2), True),
        (Point(4, 4), True),
        (Point(0, 0), True),
        (Point(5, 5), False),  # Assuming 0-based indexing, (5, 5) is out of bounds
        (Point(-1, -1), False),
    ],
)
def test_point_on_table(standard_table, point, expected):
    """Test if a Point is correctly identified as being on or off the table."""
    assert (
        point.on_table(standard_table) == expected
    ), f"Failed to verify if {point} is on table"


# Test for the TypeError when adding non-Point types
def test_point_addition_type_error():
    with pytest.raises(TypeError):
        _ = Point(1, 1) + "not_a_point"  # This should raise a TypeError
