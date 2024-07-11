from __future__ import annotations


class Cell:
    """Class representing cell in a grid"""

    def __init__(self, row: int, column: int):
        self.row: int = row
        self.column: int = column
        self.links: dict[Cell, bool] = {}

        # Store immediate neighbours
        self.north: Cell | None = None
        self.east: Cell | None = None
        self.south: Cell | None = None
        self.west: Cell | None = None

    def __eq__(self, other):
        return (
            hasattr(other, "row")
            and self.row == other.row
            and hasattr(other, "column")
            and self.column == other.column
        )

    def __hash__(self):
        coord = f"({self.row}, {self.column})"

        return hash(coord)

    def __str__(self) -> str:
        return f"({self.row}, {self.column})"

    def link(self, cell, bidi: bool = True):
        self.links[cell] = True

        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi: bool = True):
        self.links.pop(cell, None)

        if bidi:
            cell.unlink(self, False)

    def linkedCells(self) -> list[Cell]:
        return [cell for cell in self.links.keys()]

    def isLinked(self, cell) -> bool:
        return cell in self.links

    def neighbours(self) -> list:
        adjacent = [self.north, self.east, self.south, self.west]

        return [cell for cell in adjacent if cell is not None]
