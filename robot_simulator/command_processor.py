import re
from typing import Optional

from robot_simulator.direction import Direction
from robot_simulator.robot import Robot


class CommandProcessor:
    """
    A command processor for interpreting and executing textual commands on a Robot instance.

    This class takes textual commands, parses them, and invokes corresponding methods
    on the Robot instance to perform actions like moving, turning, and reporting position.
    It supports a basic command language that includes moving the robot in four cardinal
    directions, rotating it left or right, placing it at specific coordinates, and reporting
    its current location and orientation.

    Attributes:
        robot (Robot): The Robot instance that the commands will be applied to.
        place_command_pattern (re.Pattern): A compiled regular expression pattern used to
                                            match and parse the PLACE command.

    Methods:
        execute(command: str) -> Optional[bool]:
            Parses a given textual command and executes the corresponding action on the robot.
    """

    def __init__(self, robot: Robot) -> None:
        """
        Initializes the CommandProcessor with a Robot instance.

        Parameters:
            robot (Robot): The robot instance that will execute the commands.
        """
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
        """
        Executes a given textual command by invoking the corresponding method on the robot.

        This method first attempts to match the command against the PLACE command format.
        If a match is found, it places the robot at the specified coordinates and orientation.
        For other commands, it looks up the corresponding method in the commands dictionary
        and executes it. If the command is unrecognized, it prints a message indicating
        that the command is unsupported.

        Parameters:
            command (str): The textual command to be executed.
        """
        command = command.strip()
        place_match = self.place_command_pattern.match(command)
        if place_match:
            x, y, direction = place_match.groups()
            if self.robot.place(int(x), int(y), Direction[direction]):
                print(f"[SUCCESS] PLACE({x}, {y}, {direction})")
            else:
                print(f"[FAILED] PLACE({x}, {y}, {direction})")
        elif command in self.commands:
            if self.commands[command]():
                print(f"[SUCCESS] {command}")
            else:
                print(f"[FAILED] {command}")
        else:
            print(
                'Unsupported command. Only "PLACE <X int>, <Y int>, <DIRECTION NORTH|EAST|WEST|SOUTH>", "MOVE", "LEFT", "RIGHT", and "REPORT" are supported.'
            )

    def execute_from_file(self, filepath: str) -> None:
        """
        Reads commands from a file and executes them.

        Parameters:
            filepath (str): The path to the file containing the commands.
        """
        with open(filepath, "r") as file:
            for line in file:
                self.execute(line.strip())
