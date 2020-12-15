input = [int(n) for n in "8,0,17,4,1,12".split(",")]

from collections import defaultdict
indexes = defaultdict(lambda: [])
for i in range(len(input)):
    indexes[input[i]].append(i)

last = input[-1]

for i in range(len(input), 30000000):
    if len(indexes[last]) == 1:
        last = 0
    elif len(indexes[last]) == 2:
        last = indexes[last][-1] - indexes[last][-2]

    indexes[last].append(i)
    indexes[last] = indexes[last][-2:]

print(last)