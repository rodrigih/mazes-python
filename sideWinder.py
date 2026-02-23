from grid import Grid
from enum import Enum
from random import choice, random


class Texture(Enum):
    SOUTH_TO_NORTH = ("passages go south to north",)
    EAST_TO_WEST = "passages go east to west"


class SideWinder:
    """Class representing SideWinder algorithm

    Attributes:
        closeOutBias (float): Lower bias mean longer runs
                              If texture south-to-north, this means wider runs
                              If texture east-to-north, this means taller runs
        texture (Texture): determines orientation paths tend to go

    Methods:
        on(grid): Generates a maze based on bias and texture provided
    """

    def __init__(self, closeOutBias=0.5, texture=Texture.SOUTH_TO_NORTH):
        if texture in Texture:
            self.texture = texture
        else:
            self.texture = Texture.SOUTH_TO_NORTH

        self.closeOutBias = closeOutBias

    def on(self, grid: Grid):
        """
        This is with
        """

        if self.texture == Texture.SOUTH_TO_NORTH:
            self.withSouthToNorthTexture(grid)
        else:
            self.withEastToWestTexture(grid)

    def withSouthToNorthTexture(self, grid):
        for row in grid.eachRow():
            run = []

            for cell in row:
                run.append(cell)

                isAtEasternBoundary = cell.east is None
                isAtNorthernBoundary = cell.north is None

                shouldCloseOut = isAtEasternBoundary or (
                    not isAtNorthernBoundary and random() < self.closeOutBias
                )

                if shouldCloseOut:
                    chosenCell = choice(run)
                    if chosenCell.north:
                        chosenCell.link(chosenCell.north)
                        run.clear()

                else:
                    cell.link(cell.east)

    def withEastToWestTexture(self, grid):
        for i in range(grid.columns):
            run = []

            for row in grid.eachRow():
                cell = row[i]
                run.append(cell)

                isAtWesternBoundary = cell.west is None
                isAtSouthernBoundary = cell.south is None

                shouldCloseOut = isAtSouthernBoundary or (
                    not isAtWesternBoundary and random() < self.closeOutBias
                )

                if shouldCloseOut:
                    chosenCell = choice(run)
                    if chosenCell.east:
                        chosenCell.link(chosenCell.east)
                        run.clear()
                else:
                    cell.link(cell.south)
