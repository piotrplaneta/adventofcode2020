import re
def data():
    def rules_parser(line):
        if line[-1] in ["a", "b"]:
            return (line.split(": ")[0], line[-1])
        else:
            return (line.split(": ")[0], [tuple(possibility.split(" ")) for possibility in line.split(": ")[1].split(" | ")])

    def example_parser(line):
        return line

    with open("./day19/data", "r") as file:
        lines = file.read()
        return (
            {rules_parser(line)[0]: rules_parser(line)[1] for line in lines.split("\n\n")[0].split("\n")},
            [example_parser(line) for line in lines.split("\n\n")[1].split("\n")],
        )

rules, examples = data()
def generate_regex_part1(rule):
    if rules[rule] in ["a", "b"]:
        return rules[rule]
    else:
        strings = []
        for alternative in rules[rule]:
            possibilities_to_concat = [generate_regex_part1(to_concat) for to_concat in alternative]
            strings.append(("".join(possibilities_to_concat)))

        return "(" + "|".join(strings) + ")"

def generate_regex_part2(rule):
    if rules[rule] in ["a", "b"]:
        return rules[rule]
    else:
        strings = []
        for alternative in rules[rule]:
            possibilities_to_concat = [generate_regex_part2(to_concat) for to_concat in alternative]
            if rule == "11":
                for n in range(1, 11):
                    strings.append(possibilities_to_concat[0] + "{" + str(n) + "}" + possibilities_to_concat[1] + "{" + str(n) + "}")
            elif rule == "8":
                strings.append(possibilities_to_concat[0] + "+")
            else:
                strings.append(("".join(possibilities_to_concat)))

        return "(" + "|".join(strings) + ")"

regex_part1 = "^" + generate_regex_part1("0") + "$"
regex_part2 = "^" + generate_regex_part2("0") + "$"

print(len([example for example in examples if re.match(regex_part1, example)]))
print(len([example for example in examples if re.match(regex_part2, example)]))