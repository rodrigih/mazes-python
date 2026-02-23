from grid import Grid
from sideWinder import SideWinder, Texture

grid = Grid(4, 4)
sideWinder = SideWinder(closeOutBias=0.5, texture=Texture.EAST_TO_WEST)
sideWinder.on(grid)

print(grid)
