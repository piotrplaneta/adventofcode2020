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

def mask_address(address, mask):
    address_in_bin = "{0:036b}".format(address)
    result = ""
    for i in range(len(address_in_bin)):
        if mask[i] == "1":
            result += "1"
        elif mask[i] == "0":
            result += address_in_bin[i]
        else:
            result += "X"
    return result

def generate_adresses(address, possible_substitutions):
    addresses = []
    for sub in possible_substitutions:
        sub_iter = iter(list(sub))
        with_subs = ""
        for i in range(len(address)):
            if address[i] == "X":
                with_subs += next(sub_iter)
            else:
                with_subs += address[i]
        addresses.append(with_subs)

    return addresses

def write_to_memory(memory, address, value):
    count_of_xs = address.count("X")
    possible_substitutions = ["{0:0{count}b}".format(s, count=count_of_xs) for s in range(2**count_of_xs)]
    for addresss_with_sub in generate_adresses(address, possible_substitutions):
        memory[int(addresss_with_sub, 2)] = value

memory = {}
current_mask = ""
for instruction in data():
    if instruction[0] == "mask":
        current_mask = instruction[1]
    else:
        address = mask_address(instruction[1], current_mask)
        write_to_memory(memory, address, instruction[2])

print(sum(memory.values()))