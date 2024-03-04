from enum import Enum, auto


class Direction(Enum):
    """Defines possible directions the robot can face."""

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def left(self) -> "Direction":
        """Returns the direction to the left of the current one."""
        # Direct mapping from each direction to its left
        left_mapping = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }
        return left_mapping[self]

    def right(self) -> "Direction":
        """Returns the direction to the right of the current one."""
        # Direct mapping from each direction to its right
        right_mapping = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        return right_mapping[self]
