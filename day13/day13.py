import math
input = "13,x,x,x,x,x,x,37,x,x,x,x,x,449,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,773,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"
input = input.split(",")

divisors = [((int(input[index]) - index) % int(input[index]), int(input[index])) for index in range(len(input)) if input[index] != "x"]
divisors = sorted(divisors, key=lambda p: -p[1])

def iterate_for_index(index, n, solution):
    while True:
        if solution % divisors[index][1] == divisors[index][0]:
            return solution
        else:
            solution += n

solution = divisors[0][0]
for index in range(1, len(divisors)):
    n = math.prod([d[1] for d in divisors[0:index]])
    solution = iterate_for_index(index, n, solution)

print(solution)