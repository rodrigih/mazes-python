from grid import Grid
from random import choice


def on(grid: Grid):
    """Binary Tree Algorithm for generating mazes

    Given a grid, this function runs the Binary Tree algorithm to generate a maze
    """
    for cell in grid.eachCell():
        choices = [cell.north, cell.east]
        neighbours = [adj for adj in choices if adj is not None]

        if len(neighbours) != 0:
            neighbour = choice(neighbours)
            cell.link(neighbour)
