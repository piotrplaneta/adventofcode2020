from collections import defaultdict
def parse_file():
    def line_parser(line):
        return int(line.strip("\n"))

    with open("./day09/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

data = parse_file()

preamble_size = 25
possible_sums = defaultdict(lambda: set())
for n in range(preamble_size, len(data)):
    for i in range(n - preamble_size, n):
        for j in range(i + 1, n):
            possible_sums[n].add(data[i] + data[j])

def find_invalid_number():
    for n in range(preamble_size, len(data)):
        if not data[n] in possible_sums[n]:
            return data[n]

invalid_number = find_invalid_number()
print(invalid_number)

for i in range(len(data)):
    for j in range(i, len(data)):
        if i != j and sum(data[i:j+1]) == invalid_number:
            print(min(data[i:j+1]) + max(data[i:j+1]))