from collections import deque
from itertools import islice

def safe_index(deq, value):
    try:
        return deq.index(value)
    except ValueError as _:
        return None

def find_destination(cups, current_cup):
    destination = current_cup - 1
    index = safe_index(cups, destination)
    while index == None:
        destination = (destination - 1) % 10
        index = safe_index(cups, destination)

    return index + 1

def rotate_till_one_starts(cups):
    current = cups[0]
    while current != 1:
        cups.rotate()
        current = cups[0]
    
    return cups

cups = deque([int(n) for n in list("925176834")])
for _ in range(100):
    current_cup = cups[0]
    cups.rotate(-1)
    cup1, cup2, cup3 = cups.popleft(), cups.popleft(), cups.popleft()
    destination = find_destination(cups, current_cup)
    cups.insert(destination, cup3)
    cups.insert(destination, cup2)
    cups.insert(destination, cup1)


print("".join([str(n) for n in rotate_till_one_starts(cups)])[1:])
