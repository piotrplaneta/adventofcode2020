import itertools
flatten = lambda t: [item for sublist in t for item in sublist]

def data():
    def line_parser(line):
        return list(line.strip("\n"))

    with open("./day11/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

init_grid = data()

def neighbour_count_part1(position, grid):
    x, y = position
    def valid_x(x):
        return x >= 0 and x < len(grid[0])
    def valid_y(y):
        return y >= 0 and y < len(grid)

    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and valid_x(x+dx) and valid_y(y+dy) and grid[y+dy][x+dx] == "#":
                count += 1
    return count

def neighbour_count_part2(position, grid):
    def valid_x(x):
        return x >= 0 and x < len(grid[0])
    def valid_y(y):
        return y >= 0 and y < len(grid)

    def find_first_visible_seat(d):
        x, y = position
        dx, dy = d
        while(valid_x(x+dx) and valid_y(y+dy)):
            x = x + dx
            y = y + dy
            if grid[y][x] in ["#", "L"]:
                return grid[y][x]
                
        return None

    count = 0
    for d in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        if find_first_visible_seat(d) == "#":
            count += 1
    return count

def iterate(grid, counting_f, max_adjacent):
    new_grid = [[] for n in grid]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "L" and counting_f((x, y), grid) == 0:
                new_grid[y].append("#")
            elif grid[y][x] == "#" and counting_f((x, y), grid) >= max_adjacent:
                new_grid[y].append("L")
            else:
                new_grid[y].append(grid[y][x])
    return new_grid

def current_and_previous_iteration(counting_f, max_adjacent):
    current_grid = init_grid

    while True:
        previous_grid = current_grid
        current_grid = iterate(current_grid, counting_f, max_adjacent)
        yield (current_grid, previous_grid)

stable_grid_part1 = list(itertools.takewhile(lambda t: t[0] != t[1], current_and_previous_iteration(neighbour_count_part1, 4)))[-1][0]
print(sum(c == "#" for c in flatten(stable_grid_part1)))

stable_grid_part2 = list(itertools.takewhile(lambda t: t[0] != t[1], current_and_previous_iteration(neighbour_count_part2, 5)))[-1][0]
print(sum(c == "#" for c in flatten(stable_grid_part2)))