import re
def data():
    def line_parser(line):
        m = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
        if m:
            return ("mem", int(m.group(1)), int(m.group(2)))
        else:
            return ("mask", line[7:])
    
    with open("./day14/data", "r") as file:
        return [line_parser(line.strip()) for line in file.readlines()]

def mask_number(number, mask):
    number_in_bin = "{0:036b}".format(number)
    result = ""
    for i in range(len(number_in_bin)):
        if mask[i] != "X":
            result += mask[i]
        else:
            result += number_in_bin[i]
    return int(result, 2)

memory = {}
current_mask = ""
for instruction in data():
    if instruction[0] == "mask":
        current_mask = instruction[1]
    else:
        memory[instruction[1]] = mask_number(instruction[2], current_mask)

print(sum(memory.values()))