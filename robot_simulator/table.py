class Table:
    """
    Represents a rectangular table surface on which a robot can move.

    The table is defined by its length and width, representing the number of units
    in each dimension. These dimensions define the permissible area for the robot's
    movement, where the bottom left corner of the table is considered the origin (0, 0).

    Attributes:
        length (int): The length of the table (number of units along the y-axis). Defaults to 5.
        width (int): The width of the table (number of units along the x-axis). Defaults to 5.

    Example usage:
        >>> table = Table(5, 5)
        >>> print(table.length, table.width)
        5 5
    """

    def __init__(self, length: int = 5, width: int = 5) -> None:
        self.length = length
        self.width = width
