import pytest

from robot_simulator.direction import Direction
from robot_simulator.point import Point
from robot_simulator.robot import Robot


# Tests for placing the robot
@pytest.mark.parametrize(
    "x,y,facing,expected_result",
    [
        (0, 0, Direction.NORTH, True),
        (4, 4, Direction.SOUTH, True),
        (5, 5, Direction.EAST, False),  # Out of bounds
        (-1, -1, Direction.WEST, False),  # Negative coordinates
    ],
)
def test_robot_placement(standard_table, x, y, facing, expected_result):
    robot = Robot(table=standard_table, verbose=False)
    assert robot.place(x, y, facing) == expected_result


# Tests for moving the robot
@pytest.mark.parametrize(
    "start_position, facing, expected_position, expected_status",
    [
        ((0, 0), Direction.NORTH, (0, 1), True),
        ((0, 0), Direction.EAST, (1, 0), True),
        (
            (0, 0),
            Direction.SOUTH,
            (0, 0),
            False,
        ),
        ((0, 0), Direction.WEST, (0, 0), False),
    ],
)
def test_move(
    standard_table, start_position, facing, expected_position, expected_status
):
    robot = Robot(table=standard_table)
    x, y = start_position
    robot.place(x, y, facing)
    success = robot.move()
    assert success == expected_status, "Move success/failure did not match expectation"
    if success:
        assert robot.location == Point(
            *expected_position
        ), "Robot did not move to the expected position"


# Tests for turning the robot left
@pytest.mark.parametrize(
    "start_direction, expected_direction",
    [
        (Direction.NORTH, Direction.WEST),
        (Direction.WEST, Direction.SOUTH),
        (Direction.SOUTH, Direction.EAST),
        (Direction.EAST, Direction.NORTH),
    ],
)
def test_left(standard_table, start_direction, expected_direction):
    robot = Robot(table=standard_table)
    robot.place(0, 0, start_direction)
    success = robot.left()
    assert success, "Robot failed to turn left"
    assert (
        robot.direction == expected_direction
    ), "Robot did not turn left to the expected direction"


# Tests for turning the robot right
@pytest.mark.parametrize(
    "start_direction, expected_direction",
    [
        (Direction.NORTH, Direction.EAST),
        (Direction.EAST, Direction.SOUTH),
        (Direction.SOUTH, Direction.WEST),
        (Direction.WEST, Direction.NORTH),
    ],
)
def test_right(standard_table, start_direction, expected_direction):
    robot = Robot(table=standard_table)
    robot.place(0, 0, start_direction)
    success = robot.right()
    assert success, "Robot failed to turn right"
    assert (
        robot.direction == expected_direction
    ), "Robot did not turn right to the expected direction"
