def data():
    def line_parser(line):
        return line.strip("\n")

    with open("./day03/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

tree_map = data()

def count_trees_with_steps(steps):
    step_down, step_right = steps
    trees = 0
    current = 0
    for i in range(0, len(tree_map), step_down):
        if tree_map[i][current] == '#':
            trees = trees + 1
        current = (current + step_right) % len(tree_map[0])
    return trees

print(count_trees_with_steps((1,3)))

import math
print(math.prod([count_trees_with_steps(steps) for steps in [(1,1), (1,3), (1,5), (1,7), (2,1)]]))