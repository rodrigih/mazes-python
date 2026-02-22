from grid import Grid
from random import choice


def on(grid: Grid):
    """Sidewinder Algorithm for generating mazes

    Given a grid, this function runs the Sidewinder algorithm to generate a maze
    """
    for row in grid.eachRow():
        run = []

        for cell in row:
            run.append(cell)

            isAtEasternBoundary = cell.east == None
            isAtNorthernBoundary = cell.north == None

            shouldCloseOut = isAtEasternBoundary or (
                not isAtNorthernBoundary and choice([True, False])
            )

            if shouldCloseOut:
                chosenCell = choice(run)
                if chosenCell.north:
                    chosenCell.link(chosenCell.north)
                    run.clear()

            else:
                cell.link(cell.east)
