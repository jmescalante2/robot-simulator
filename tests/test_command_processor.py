from unittest.mock import MagicMock

import pytest

from robot_simulator.command_processor import CommandProcessor
from robot_simulator.direction import Direction
from robot_simulator.robot import Robot


@pytest.fixture
def mock_robot():
    """Fixture for creating a mock Robot instance."""
    robot = MagicMock(spec=Robot)
    return robot


@pytest.fixture
def command_processor(mock_robot):
    """Fixture for creating a CommandProcessor instance with a mock Robot."""
    return CommandProcessor(robot=mock_robot)


# Test execution of valid commands
@pytest.mark.parametrize(
    "command, expected_method_name",
    [
        ("PLACE 0,0,NORTH", "place"),
        ("MOVE", "move"),
        ("LEFT", "left"),
        ("RIGHT", "right"),
        ("REPORT", "report"),
    ],
)
def test_valid_commands(command_processor, mock_robot, command, expected_method_name):
    command_processor.execute(command)
    getattr(mock_robot, expected_method_name).assert_called()


# Test command processor does not execute unsupported commands
def test_unsupported_command(command_processor, mock_robot):
    command_processor.execute("JUMP")
    mock_robot.assert_not_called()  # Ensure no robot method was called for unsupported command


# Additional tests can include:
# - Checking the robot's position and direction after executing a sequence of commands.
# - Verifying error handling for out-of-bounds PLACE commands.
# - Testing the report functionality and its output formatting.
# - Ensuring that PLACE commands with invalid coordinates or directions are handled properly.
