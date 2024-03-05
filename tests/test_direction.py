import pytest

from robot_simulator.direction import Direction


@pytest.mark.parametrize(
    "current_direction, expected_direction",
    [
        (Direction.NORTH, Direction.WEST),
        (Direction.WEST, Direction.SOUTH),
        (Direction.SOUTH, Direction.EAST),
        (Direction.EAST, Direction.NORTH),
    ],
)
def test_turn_left(current_direction, expected_direction):
    """Test if turning left from a given direction results in the expected direction."""
    assert (
        current_direction.left() == expected_direction
    ), f"Failed for {current_direction} turning left"


@pytest.mark.parametrize(
    "current_direction, expected_direction",
    [
        (Direction.NORTH, Direction.EAST),
        (Direction.EAST, Direction.SOUTH),
        (Direction.SOUTH, Direction.WEST),
        (Direction.WEST, Direction.NORTH),
    ],
)
def test_turn_right(current_direction, expected_direction):
    """Test if turning right from a given direction results in the expected direction."""
    assert (
        current_direction.right() == expected_direction
    ), f"Failed for {current_direction} turning right"
