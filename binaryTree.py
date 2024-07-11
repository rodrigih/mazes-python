from random import choice


def on(grid):
    for cell in grid.eachCell():
        choices = [cell.north, cell.east]
        neighbours = [adj for adj in choices if adj is not None]

        if len(neighbours) != 0:
            neighbour = choice(neighbours)
            cell.link(neighbour)
