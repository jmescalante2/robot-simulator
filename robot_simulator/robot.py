import sys

from robot_simulator.direction import Direction
from robot_simulator.point import Point
from robot_simulator.table import Table


class Robot:
    """
    A programmable robot that can navigate a two-dimensional table based on commands.

    This class enables the robot to be placed on a table with a specific orientation,
    move forward, rotate left or right, and report its current position and direction.
    The robot's movements are constrained by the table's dimensions.
    """

    __MOVES = {
        Direction.NORTH: Point(0, 1),
        Direction.EAST: Point(1, 0),
        Direction.SOUTH: Point(0, -1),
        Direction.WEST: Point(-1, 0),
    }

    def __init__(
        self,
        table: Table = Table(5, 5),
        report_file: str = None,
    ) -> None:
        """
        Initializes the Robot with a given table and verbosity setting.

        Parameters:
            table (Table): The table on which the robot moves. Defaults to a 5x5 table.
            report_file (str): The file in which the robot will log its reports.
        """
        self.table = table
        self.location = Point(
            -1, -1
        )  # Use an invalid initial location to denote 'not placed'
        self.direction = None
        self.report_file = report_file

    def place(self, x: int, y: int, facing: Direction) -> bool:
        """
        Places the robot at a specified location with a specified direction on the table.

        Parameters:
            x (int): The x-coordinate of the location.
            y (int): The y-coordinate of the location.
            facing (Direction): The direction the robot will face.

        Returns:
            bool: True if the placement is successful, False otherwise.
        """
        potential_location = Point(x, y)
        if potential_location.on_table(self.table) and facing in Direction:
            self.location = potential_location
            self.direction = facing
            return True
        return False

    def on_table(self) -> bool:
        """
        Checks if the robot's current location is within the bounds of the table.

        Returns:
            bool: True if the robot is on the table, False otherwise.
        """
        return self.location.on_table(self.table)

    def move(self) -> bool:
        """
        Moves the robot one unit forward in its current direction if possible.

        Returns:
            bool: True if the move is successful, False otherwise.
        """
        if self.on_table():
            new_location = self.location + self.__MOVES[self.direction]
            if new_location.on_table(self.table):
                self.location = new_location
                return True
        return False

    def left(self) -> None:
        """
        Rotates the robot 90 degrees to the left (counter-clockwise) without changing its position.

        Returns:
            bool: True if the robot turned to its left successfully, False otherwise.
        """
        if self.on_table():
            self.direction = self.direction.left()
            return True
        return False

    def right(self) -> None:
        """
        Rotates the robot 90 degrees to the right (clockwise) without changing its position.

        Returns:
            bool: True if the robot turned to its right successfully, False otherwise.
        """
        if self.on_table():
            self.direction = self.direction.right()
            return True
        return False

    def report(self) -> None:
        """
        Prints the robot's current location and direction to the specified log file or stdout.

        Parameters:
            report_file (Union[str, "sys.stdout"]): The output destination for the report. Defaults to stdout.

        Returns:
            bool: True if the robot turned to its left successfully, False otherwise.
        """
        if self.on_table():
            if self.report_file:
                print(
                    f"[REPORTING] {self.location.x}, {self.location.y}, {self.direction.name}",
                    file=open(self.report_file, "a"),
                )
            else:
                print(
                    f"[REPORTING] {self.location.x}, {self.location.y}, {self.direction.name}",
                    file=sys.stdout,
                )
            return True
        return False
