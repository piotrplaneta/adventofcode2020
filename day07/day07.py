import re
from collections import defaultdict

def data():
    def line_parser(line):
        parent, children = line.split(" bags contain ")[0], line.split(" bags contain ")[1].split(", ")
        children = [re.sub(r"\.| bags| bag", "", child) for child in children]
        children = [(child.split(" ", 1)[0], child.split(" ", 1)[1]) for child in children]
        if children == [('no', 'other')]:
            return parent, []
        else:
            return parent, [(int(child[0]), child[1]) for child in children]

    with open("./day07/data", "r") as file:
        return [line_parser(line.strip("\n")) for line in file.readlines()]

rules = dict(data())
parents = defaultdict(lambda: [])
for (parent, children) in rules.items():
    for _, child in children:
        parents[child] = parents[child] + [parent]

def count_parents(node, processed):
    if node in processed:
        return 0, processed
    else:
        parent_counts = 1
        processed.add(node)
        for parent in parents[node]:
            parent_count, new_processed = count_parents(parent, processed)
            parent_counts = parent_counts + parent_count
            processed = processed | new_processed
        return parent_counts, processed

print(count_parents("shiny gold", set())[0] - 1)

def count_children_with_amount(node):
    if rules[node]:
        return sum([amount * count_children_with_amount(child) for (amount, child) in rules[node]]) + 1
    else:
        return 1

print(count_children_with_amount("shiny gold") - 1)