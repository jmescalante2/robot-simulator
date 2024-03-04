import sys
from typing import Union

from robot_simulator.direction import Direction
from robot_simulator.point import Point
from robot_simulator.table import Table


class Robot:
    """
    A programmable robot that can navigate a two-dimensional table based on commands.

    This class allows a robot to be placed on a specified location on the table with
    a specific orientation, move forward, rotate left or right, and report its current
    position and direction. The robot's movements are constrained by the dimensions
    of the table, and it will not move if an operation would result in it falling off.

    Attributes:
        table (Table): The table on which the robot moves. Defaults to a 5x5 table.
        location (Point): The current location of the robot on the table. Initialized
                          to an invalid location (-1, -1) to signify the robot is not
                          yet placed on the table.
        direction (Direction): The current direction the robot is facing. It is None
                               until the robot is placed.
        verbose (bool): If True, the robot will print messages for invalid operations.
                        Defaults to True.

    Methods:
        place(x: int, y: int, facing: Direction) -> bool:
            Places the robot at a specified location with a specified direction on the table.

        on_table() -> bool:
            Checks if the robot's current location is within the bounds of the table.

        move() -> bool:
            Moves the robot one unit forward in its current direction if possible.

        left() -> None:
            Rotates the robot 90 degrees to the left (counter-clockwise) without changing its position.

        right() -> None:
            Rotates the robot 90 degrees to the right (clockwise) without changing its position.

        report(log_file: Union[str, "sys.stdout"] = sys.stdout) -> None:
            Prints the robot's current location and direction to the specified log file or stdout.
    """

    __MOVES = {
        Direction.NORTH: Point(0, 1),
        Direction.EAST: Point(1, 0),
        Direction.SOUTH: Point(0, -1),
        Direction.WEST: Point(-1, 0),
    }

    def __init__(self, table: Table = Table(5, 5), verbose: bool = True) -> None:
        self.table = table
        self.location = Point(
            -1, -1
        )  # Use an invalid initial location to denote 'not placed'
        self.direction = None
        self.verbose = verbose

    def place(self, x: int, y: int, facing: Direction) -> bool:
        """Places the robot at a specified location and direction on the table."""
        potential_location = Point(x, y)
        if potential_location.on_table(self.table) and facing in Direction:
            self.location = potential_location
            self.direction = facing
            return True
        return False

    def on_table(self) -> bool:
        return self.location.on_table(self.table)

    def move(self) -> bool:
        """Moves the robot one unit forward in the direction it is currently facing."""
        if self.on_table():
            new_location = self.location + self.__MOVES[self.direction]
            if new_location.on_table(self.table):
                self.location = new_location
                return True
        if self._verbose:
            print(
                "Move not allowed. Ensure the robot is correctly placed on the table."
            )
        return False

    def left(self) -> None:
        """Rotates the robot to face left of its current direction."""
        if self.on_table():
            self.direction = self.direction.left()
        elif self.verbose:
            print("Invalid command. Place the robot first.")

    def right(self) -> None:
        """Rotates the robot to face right of its current direction."""
        if self.on_table():
            self.direction = self.direction.right()
        elif self.verbose:
            print("Invalid command. Place the robot first.")

    def report(self, log_file: Union[str, "sys.stdout"] = sys.stdout) -> None:
        """Reports the current location and direction of the robot."""
        if self.on_table():
            print(
                f"{self.location.x}, {self.location.y}, {self.direction.name}",
                file=log_file,
            )
        elif self.verbose:
            print("Invalid command. Place the robot first.")
