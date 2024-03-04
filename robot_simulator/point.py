from dataclasses import dataclass

from robot_simulator.table import Table


@dataclass(frozen=True)
class Point:
    """Represents a point in a 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    """

    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        """Allows adding two Points together to create a new Point.

        Args:
            other (Point): Another point to add to this one.

        Returns:
            Point: A new Point representing the sum of this point and the other.
        """
        # Example place for potential error handling if 'other' is not a Point instance
        if not isinstance(other, Point):
            raise TypeError("Operand must be of type Point")
        return Point(self.x + other.x, self.y + other.y)

    def on_table(self, table: Table) -> bool:
        """Checks if the point is within the bounds of the table.

        Args:
            table (Table): The table to check against.

        Returns:
            bool: True if the point is within the table's bounds, False otherwise.
        """
        return 0 <= self.x < table.length and 0 <= self.y < table.width
