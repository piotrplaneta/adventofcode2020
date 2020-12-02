import re
def data():
    def line_parser(line):
        m = re.search(r"(\d+)-(\d+) (\w): (\w+)", line.strip("\n"))
        return (int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))

    with open("./day02/data", "r") as file:
        return [line_parser(line) for line in file.readlines()]

def is_password_valid_for_part1(password_entry):
    min, max, char, password = password_entry
    return password.count(char) >= min and password.count(char) <= max

def is_password_valid_for_part2(password_entry):
    pos1, pos2, char, password = password_entry
    return [password[pos1 - 1], password[pos2 - 1]].count(char) == 1

password_entries = data()
print(len([password_entry for password_entry in password_entries if is_password_valid_for_part1(password_entry)]))
print(len([password_entry for password_entry in password_entries if is_password_valid_for_part2(password_entry)]))