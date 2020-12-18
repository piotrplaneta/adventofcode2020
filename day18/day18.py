def find_matching_paren(string, reversed):
    depth = 1
    for i, c in enumerate(string):
        if c == ")" and reversed:
            depth += 1
        elif c == "(" and not reversed:
            depth += 1
        elif c == "(" and reversed:
            depth -= 1
        elif c == ")" and not reversed:
            depth -= 1

        if depth == 0:
            return i

stack = []
def evaluate(exp):
    if len(exp) == 0:
        return stack.pop()
    elif exp[0].isdigit():
        stack.append(int(exp[0]))
        return evaluate(exp[1:])
    elif exp[0] == "+":
        return stack.pop() + evaluate(exp[1:])
    elif exp[0] == "*":
        return stack.pop() * evaluate(exp[1:])
    elif exp[0] == ")":
        matching_paren_index = find_matching_paren(exp[1:], True)
        stack.append(evaluate(exp[1:matching_paren_index + 1]))
        return evaluate(exp[matching_paren_index + 2:])

def add_parens(exp):
    new_exp = exp
    i = 0
    while i < len(new_exp):
        if new_exp[i] == "*":
            new_exp = new_exp[0:i+1] + "(" + new_exp[i+1:] + ")"
            i += 2
        elif new_exp[i] == "(":
            matching_paren_offset = find_matching_paren(new_exp[i+1:], False)
            inner_with_parens = add_parens(new_exp[(i + 1):(i + matching_paren_offset + 1)])
            new_exp = new_exp[0:i+1] + inner_with_parens + new_exp[(i + matching_paren_offset + 1):]
            i += len(inner_with_parens)
        else:
            i += 1
    return new_exp
   
expressions = [line.replace(" ", "") for line in open("day18/data").read().splitlines()]
print(sum([evaluate(exp[::-1]) for exp in expressions]))
print(sum([evaluate(add_parens(exp)[::-1]) for exp in expressions]))