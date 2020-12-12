def data():
    def line_parser(line):
        return (line[0], int(line.strip("\n")[1:]))

    with open("./day12/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

moves = data()
def part1():
    position = (0, 0)
    direction = (1, 0)
    directions = [(1,0), (0, -1), (-1, 0), (0, 1)]

    for move_desc in moves:
        move, amount = move_desc
        if move == "N":
            position = (position[0], position[1] + amount)
        elif move == "S":
            position = (position[0], position[1] - amount)
        elif move == "E":
            position = (position[0] + amount, position[1])
        elif move == "W":
            position = (position[0] - amount, position[1])
        elif move == "F":
            position = (position[0] + direction[0] * amount, position[1] + direction[1] * amount)
        elif move == "L":
            current_dir_index = directions.index(direction)
            direction = directions[(current_dir_index - int(amount / 90)) % 4]
        elif move == "R":
            current_dir_index = directions.index(direction)
            direction = directions[(current_dir_index + int(amount / 90)) % 4]

    return abs(position[0]) + abs(position[1])

def part2():
    position = (0, 0)
    waypoint = (10, 1)

    for move_desc in moves:
        move, amount = move_desc
        if move == "N":
            waypoint = (waypoint[0], waypoint[1] + amount)
        elif move == "S":
            waypoint = (waypoint[0], waypoint[1] - amount)
        elif move == "E":
            waypoint = (waypoint[0] + amount, waypoint[1])
        elif move == "W":
            waypoint = (waypoint[0] - amount, waypoint[1])
        elif move == "F":
            position = (position[0] + amount * waypoint[0], position[1] + amount * waypoint[1])
        elif move in ["L", "R"]:
            rotated_waypoints = [waypoint, (waypoint[1], -waypoint[0]), (-waypoint[0], -waypoint[1]), (-waypoint[1], waypoint[0])]
            if move == "L":
                waypoint = rotated_waypoints[-int(amount / 90)]
            else:
                waypoint = rotated_waypoints[int(amount / 90)]

    return abs(position[0]) + abs(position[1])
    
print(part1())
print(part2())
