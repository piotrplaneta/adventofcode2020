import math
def data():
    def parse_rules(rules):
        def parse_rule(rule):
            return (rule.split(": ")[0], list(map(lambda x: x.split("-"), rule.split(": ")[1].split(" or "))))

        return {parse_rule(rule)[0]: parse_rule(rule)[1] for rule in rules}

    def parse_tickets(tickets):
        return [list(map(lambda n: int(n), ticket.split(","))) for ticket in tickets]

    with open("./day16/data", "r") as file:
        content = file.read().split("\n\n")
        return {
            "rules": parse_rules(content[0].split("\n")),
            "my_ticket": parse_tickets(content[1].split("\n")[1:])[0],
            "nearby_tickets": parse_tickets(content[2].split("\n")[1:])
        }

rules = data()["rules"]
my_ticket = data()["my_ticket"]
nearby_tickets = data()["nearby_tickets"]

def is_value_in_rule(rule_ranges, value):
    return (
        (value >= int(rule_ranges[0][0]) and value <= int(rule_ranges[0][1])) or
        (value >= int(rule_ranges[1][0]) and value <= int(rule_ranges[1][1]))
    )

def is_field_invalid(field):
    valid = False
    for _, rule_ranges in rules.items():
        valid = valid or is_value_in_rule(rule_ranges, field)

    return not valid

def invalid_fields_value(ticket):
    return sum([field for field in ticket if is_field_invalid(field)])

def is_ticket_valid(ticket):
    return invalid_fields_value(ticket) == 0 and all([field != 0 for field in ticket])

def fields_values(tickets):
    values = []
    for i in range(len(tickets[0])):
        values.append([ticket[i] for ticket in tickets])

    return values

def rules_with_zero_errors_for_values(values):
    rules_with_zero_errors = []
    for rule_name, rule_ranges in rules.items():
        if all([is_value_in_rule(rule_ranges, value) for value in values]):
            rules_with_zero_errors.append(rule_name)
    
    return rules_with_zero_errors

def possible_fields_for_indexes(tickets):
    possible = []
    for i in range(len(fields_values(tickets))):
        possible.append((i, rules_with_zero_errors_for_values(fields_values(tickets)[i])))

    return possible

print(sum([invalid_fields_value(ticket) for ticket in nearby_tickets]))

valid_tickets = [ticket for ticket in nearby_tickets if is_ticket_valid(ticket)]
possible_field_assignments = sorted(possible_fields_for_indexes(valid_tickets), key=lambda x: len(x[1]))
assignments = {}
for possible_assignment in possible_field_assignments:
    assignments[possible_assignment[0]] = list(set(possible_assignment[1]) - set(assignments.values()))[0]
indexes_for_departure_data = {index: field for index, field in assignments.items() if "departure" in field}
print(math.prod(my_ticket[index] for index in indexes_for_departure_data.keys()))