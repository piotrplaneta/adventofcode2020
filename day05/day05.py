def data():
    def line_parser(line):
        row = int(line[0:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:10].replace("L", "0").replace("R", "1"), 2)
        return (row, column)

    with open("./day05/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

ids = sorted([boarding_pass[0] * 8 + boarding_pass[1] for boarding_pass in data()])

print(max(ids))

for id in range(ids[0], ids[-1]):
    if id not in ids:
        print(id)