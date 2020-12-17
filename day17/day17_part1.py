import copy
from collections import defaultdict
def data():
    def line_parser(line):
        return {k: v for k, v in enumerate(line)}

    with open("./day17/data", "r") as file:
        return {k: line_parser(line.strip("\n")) for k, line in enumerate(file.readlines())}

def adjacent(position, grid):
    x, y, z = position
    sum = 0
    for dz in range(max(z - 1, min(grid.keys())), min(z + 2, max(grid.keys()) + 1)):
        for dy in range(max(y - 1, min(grid[dz].keys())), min(y + 2, max(grid[dz].keys()) + 1)):
            for dx in range(max(x - 1, min(grid[dz][dy].keys())), min(x + 2, max(grid[dz][dy].keys()) + 1)):
                if (dz != z or dy != y or dx != x) and grid[dz][dy][dx] == "#":
                    sum += 1
    return sum

def iterate(grid, iterations):
    for _ in range(iterations):
        new_grid = copy.deepcopy(grid)
        z_range = range(min(grid.keys()) - 1, max(grid.keys()) + 2)
        y_range = range(min(grid[0].keys()) - 1, max(grid[0].keys()) + 2)
        x_range = range(min(grid[0][0].keys()) - 1, max(grid[0][0].keys()) + 2)

        for z in z_range:
            for y in y_range:
                for x in x_range:
                    adjacent_count = adjacent((x, y, z), grid)
                    if z in grid.keys() and y in grid[z].keys() and x in grid[z][y].keys():
                        if grid[z][y][x] == "#" and (adjacent_count not in [2, 3]):
                            new_grid[z][y][x] = "."
                        elif grid[z][y][x] == "." and adjacent_count == 3:
                            new_grid[z][y][x] = "#"
                        else:
                            new_grid[z][y][x] = grid[z][y][x]
                    else:
                        if adjacent_count == 3:
                            new_grid[z][y][x] = "#"
                        else:
                            if not z in new_grid.keys():
                                new_grid[z] = {}
                            if not y in new_grid[z].keys():
                                new_grid[z][y] = {}
                            if not x in new_grid[z][y].keys():
                                new_grid[z][y][x] = {}
                            new_grid[z][y][x] = "."
        grid = new_grid
    return grid

grid = {0: data()}
after_iterations = iterate(grid, 6)
sum = 0
for z in after_iterations.keys():
    for y in after_iterations[z].keys():
        for x in after_iterations[z][y].keys():
            if after_iterations[z][y][x] == "#":
                sum += 1
print(sum)