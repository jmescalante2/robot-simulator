import re
from typing import Optional

from robot_simulator.direction import Direction
from robot_simulator.robot import Robot


class CommandProcessor:
    """Processes textual commands and applies them to a Robot instance."""

    def __init__(self, robot: Robot) -> None:
        self.robot = robot
        self.place_command_pattern = re.compile(
            r"\s*PLACE\s*(\d+)\s*,\s*(\d+)\s*,\s*(NORTH|SOUTH|EAST|WEST)\s*"
        )
        # Command mapping to methods to reduce cyclomatic complexity
        # Note: 'PLACE' is handled separately due to its unique argument requirements
        self.commands = {
            "MOVE": self.robot.move,
            "LEFT": self.robot.left,
            "RIGHT": self.robot.right,
            "REPORT": self.robot.report,
        }

    def execute(self, command: str) -> Optional[bool]:
        """Executes a single command."""
        command = command.strip()
        place_match = self.place_command_pattern.match(command)
        if place_match:
            x, y, direction = place_match.groups()
            return self.robot.place(int(x), int(y), Direction[direction])
        elif command in self.commands:
            return self.commands[command]()
        else:
            print(
                'Only "PLACE int, int, NORTH|SOUTH|EAST|WEST", "MOVE", "LEFT", "RIGHT", and "REPORT" commands are supported.'
            )
