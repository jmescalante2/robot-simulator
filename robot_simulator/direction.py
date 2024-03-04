from enum import Enum, auto


class Direction(Enum):
    """
    Enum representing the four cardinal directions that a robot can face.

    This class provides functionality to determine a new direction based on
    turning left or right from the current direction.

    Members:
        NORTH: Represents the direction pointing towards the north.
        EAST: Represents the direction pointing towards the east.
        SOUTH: Represents the direction pointing towards the south.
        WEST: Represents the direction pointing towards the west.
    """

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def left(self) -> "Direction":
        """
        Determines the new direction after turning 90 degrees to the left.

        This method calculates the new direction by mapping the current direction
        to its immediate left counterpart, simulating a 90-degree counter-clockwise rotation.

        Returns:
            Direction: The direction to the left of the current direction.
        """
        left_mapping = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }
        return left_mapping[self]

    def right(self) -> "Direction":
        """
        Determines the new direction after turning 90 degrees to the right.

        This method calculates the new direction by mapping the current direction
        to its immediate right counterpart, simulating a 90-degree clockwise rotation.

        Returns:
            Direction: The direction to the right of the current direction.
        """
        right_mapping = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        return right_mapping[self]
