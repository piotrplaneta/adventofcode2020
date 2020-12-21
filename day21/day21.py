from collections import defaultdict
flatten = lambda t: [item for sublist in t for item in sublist]

def data():
    def line_parser(line):
        splitted = line.strip(")\n").split(" (contains ")
        return (splitted[0].split(" "), splitted[1].split(", "))

    with open("./day21/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

recipes = data()
all_food = flatten([r[0] for r in recipes])

allergenes = defaultdict(lambda: set(all_food))
for r in recipes:
    for allergen in r[1]:
        allergenes[allergen] &= set(r[0])

no_allergenes = set(all_food) - set(flatten(allergenes.values()))
print(sum([all_food.count(food) for food in no_allergenes]))

allergen_matches = list(dict(allergenes).items())

count_of_matches = len(allergen_matches)
processed = {}
while(len(processed.keys()) != count_of_matches):
    current = sorted(allergen_matches, key=lambda m: len(m[1]))[0]
    current_food = list(current[1])[0]
    processed[current_food] = current[0]
    allergen_matches.remove(current)
    allergen_matches = [(k, v - set([current_food])) for k,v in allergen_matches]

print(",".join([k for k, v in sorted(list(processed.items()), key=lambda x: x[1])]))