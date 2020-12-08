import itertools

def data():
    def parse_op(op):
        return op.split(" ")[0], int(op.split(" ")[1])

    with open("./day08/data", "r") as file:
        return [parse_op(op) for op in file.read().split("\n")]

class GameConsole:
    accumulator = 0
    execution_index = 0

    def nop(self, operand):
        self.execution_index = self.execution_index + 1
        return self.accumulator, self.execution_index

    def acc(self, operand):
        self.execution_index = self.execution_index + 1
        self.accumulator = self.accumulator + operand
        return self.accumulator, self.execution_index

    def jmp(self, operand):
        self.execution_index = self.execution_index + operand
        return self.accumulator, self.execution_index

    def execute_instructions(self, instructions):
        functions = {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }

        while self.execution_index < len(instructions):
            current_operation, operand = instructions[self.execution_index]
            yield functions[current_operation](operand)

instructions = data()

def indexes_seen_so_far_and_state(indexes_so_far, current_state):
    _, current_index = current_state
    return indexes_so_far[0] + [current_index], current_state

def execute_while_error_or_end(instructions):
    execution = GameConsole().execute_instructions(instructions)
    with_indexes = itertools.accumulate(execution, indexes_seen_so_far_and_state, initial=([], (0, 0)))
    return list(itertools.takewhile(lambda element: len(element[0]) == len(set(element[0])), with_indexes))[-1][1]

print(execute_while_error_or_end(instructions)[0])

for i in range(len(instructions)):
    changes = {
        "nop": "jmp",
        "jmp": "nop"
    }

    def has_ended_properly(state):
        return state[1] == len(instructions)

    operation, operand = instructions[i]

    if instructions[i][0] in changes:
        new_instructions = instructions[0:i] + [(changes[operation], operand)] + instructions[i+1:]
        if has_ended_properly(execute_while_error_or_end(new_instructions)):
            print(execute_while_error_or_end(new_instructions)[0])
    else:
        pass