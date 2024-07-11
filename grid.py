from cell import Cell
from random import choice
from typing import Iterator


class Grid:
    def __init__(self, rows: int, columns: int):
        self.rows: int = rows
        self.columns: int = columns

        self.grid = self.prepareGrid()
        self.configureCells()

    def __str__(self):
        output = "+" + ("---+" * self.columns) + "\n"

        for row in self.eachRow():
            top = "|"
            bottom = "+"

            for cell in row:
                body = " " * 3
                eastBoundary = " " if cell.isLinked(cell.east) else "|"
                top = f"{top}{body}{eastBoundary}"

                southBoundary = " " * 3 if cell.isLinked(cell.south) else "---"
                bottom = f"{bottom}{southBoundary}+"

            output = f"{output}{top}\n"
            output = f"{output}{bottom}\n"

        return output

    def get(self, row: int, col: int) -> Cell | None:
        """
        Gets Cell in specified row and column.
        If out of bounds, returns None
        """
        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.columns:
            return None

        return self.grid[row][col]

    def prepareGrid(self) -> list[list[Cell]]:
        """Creates 2-d array of cells"""
        grid = []

        for row in range(self.rows):
            currentRow = []

            for col in range(self.columns):
                currentRow.append(Cell(row, col))

            grid.append(currentRow)

        return grid

    def configureCells(self):
        """Tells each cell who it's neighbours are"""
        for row in range(self.rows):
            for col in range(self.columns):
                cell = self.grid[row][col]
                cell.north = self.get(row - 1, col)
                cell.east = self.get(row, col + 1)
                cell.south = self.get(row + 1, col)
                cell.west = self.get(row, col - 1)

    def randomCell(self) -> Cell:
        """Randomly picks a cell from the grid"""
        randRow = choice(range(self.rows))
        randCol = choice(range(self.columns))

        return self.grid[randRow][randCol]

    def size(self) -> int:
        """Returns number of cells"""
        return self.rows * self.columns

    def eachRow(self) -> Iterator[list[Cell]]:
        """Returns Iterator for each row in Grid"""
        for row in self.grid:
            yield row

    def eachCell(self) -> Iterator[Cell]:
        """Returns Iterator for each cell in Grid"""
        for rows in self.grid:
            for cell in rows:
                yield cell
