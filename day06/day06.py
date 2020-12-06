def data():
    def parse_group(group):
        return group.split("\n")

    with open("./day06/data", "r") as file:
        return [parse_group(group_desc) for group_desc in file.read().split("\n\n")]

groups = data()
print(sum([len(set(sum([list(declaration) for declaration in group], []))) for group in groups]))
print(sum([len(set.intersection(*[set(list(declaration)) for declaration in group])) for group in groups]))