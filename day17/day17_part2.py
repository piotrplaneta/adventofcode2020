import copy
from collections import defaultdict
def data():
    def line_parser(line):
        return {k: v for k, v in enumerate(line)}

    with open("./day17/data", "r") as file:
        return {k: line_parser(line.strip("\n")) for k, line in enumerate(file.readlines())}

def adjacent(position, grid):
    x, y, z, w = position
    sum = 0
    for dw in range(max(w - 1, min(grid.keys())), min(w + 2, max(grid.keys()) + 1)):
        for dz in range(max(z - 1, min(grid[dw].keys())), min(z + 2, max(grid[dw].keys()) + 1)):
            for dy in range(max(y - 1, min(grid[dw][dz].keys())), min(y + 2, max(grid[dw][dz].keys()) + 1)):
                for dx in range(max(x - 1, min(grid[dw][dz][dy].keys())), min(x + 2, max(grid[dw][dz][dy].keys()) + 1)):
                    if (dw != w or dz != z or dy != y or dx != x) and grid[dw][dz][dy][dx] == "#":
                        sum += 1
    return sum

def iterate(grid, iterations):
    for _ in range(iterations):
        new_grid = copy.deepcopy(grid)
        w_range = range(min(grid.keys()) - 1, max(grid.keys()) + 2)
        z_range = range(min(grid[0].keys()) - 1, max(grid[0].keys()) + 2)
        y_range = range(min(grid[0][0].keys()) - 1, max(grid[0][0].keys()) + 2)
        x_range = range(min(grid[0][0][0].keys()) - 1, max(grid[0][0][0].keys()) + 2)

        for w in w_range:
            for z in z_range:
                for y in y_range:
                    for x in x_range:
                        adjacent_count = adjacent((x, y, z, w), grid)
                        if w in grid.keys() and z in grid[w].keys() and y in grid[w][z].keys() and x in grid[w][z][y].keys():
                            if grid[w][z][y][x] == "#" and (adjacent_count not in [2, 3]):
                                new_grid[w][z][y][x] = "."
                            elif grid[w][z][y][x] == "." and adjacent_count == 3:
                                new_grid[w][z][y][x] = "#"
                            else:
                                new_grid[w][z][y][x] = grid[w][z][y][x]
                        else:
                            if adjacent_count == 3:
                                new_grid[w][z][y][x] = "#"
                            else:
                                if not w in new_grid.keys():
                                    new_grid[w] = {}
                                if not z in new_grid[w].keys():
                                    new_grid[w][z] = {}
                                if not y in new_grid[w][z].keys():
                                    new_grid[w][z][y] = {}
                                if not x in new_grid[w][z][y].keys():
                                    new_grid[w][z][y][x] = {}
                                new_grid[w][z][y][x] = "."
        grid = new_grid
    return grid

grid = {0: {0: data()}}
after_iterations = iterate(grid, 6)
sum = 0
for w in after_iterations.keys():
    for z in after_iterations[w].keys():
        for y in after_iterations[w][z].keys():
            for x in after_iterations[w][z][y].keys():
                if after_iterations[w][z][y][x] == "#":
                    sum += 1
print(sum)