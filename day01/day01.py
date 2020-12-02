def data():
    with open("./day01/data", "r") as file:
        return [int(line.strip("\n")) for line in file.readlines()]

numbers = data()

part1 = [first_number for first_number in numbers if (2020 - first_number) in numbers]
print(part1[0] * part1[1])

import math
pairs = [[second_number for second_number in numbers if (2020 - first_number - second_number) in numbers] for first_number in numbers]
relevant = [pair for pair in pairs if pair != []]
print(math.prod(set(sum(relevant, []))))