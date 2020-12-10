def data():
    def line_parser(line):
        return int(line.strip("\n"))

    with open("./day10/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

def each_cons(xs, size):
    return [xs[i:i+size] for i in range(len(xs)-size+1)]

jolts = data()
jolts = jolts + [0, max(jolts) + 3]
sorted_jolts = sorted(jolts)

differences = {1: 0, 3: 0}
for pair in each_cons(sorted_jolts, 2):
    differences[pair[1] - pair[0]] += 1

print(differences[1] * differences[3])

next_arrangement_count_cache = {}
def possible_next_arrangement_count(current):
    if current == sorted_jolts[-1]:
        return 1
    else:
        if current not in next_arrangement_count_cache:
            next_adapters = [n for n in range(current+1, current+4) if n in sorted_jolts]
            next_arrangement_count_cache[current] = sum([possible_next_arrangement_count(next_adapter) for next_adapter in next_adapters])
        return next_arrangement_count_cache[current]

print(possible_next_arrangement_count(0))