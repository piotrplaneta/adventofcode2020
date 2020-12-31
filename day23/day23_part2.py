from collections import deque
from itertools import islice

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.prev) + "<-" + str(self.value) + "->" + str(self.next)

    def __str__(self):
        return str(self.value)

class RingWithIndexing:
    def __init__(self, init_seq, max_value):
        self.nodes = {}
        self.max_value = max_value
        starting_node = Node(init_seq[0])
        self.nodes[init_seq[0]] = starting_node

        prev_node = starting_node
        to_add = init_seq[1:] + list(range(10, max_value + 1))
        for n in to_add:
            current = Node(n)
            current.prev = prev_node
            prev_node.next = current
            self.nodes[n] = current
            prev_node = current

        prev_node.next = starting_node
        starting_node.prev = prev_node
        self.current = starting_node

    def find_destination_for_current(self):
        current_cup = self.current
        c_value = current_cup.value
        next_3 = [current_cup.next, current_cup.next.next, current_cup.next.next.next]
        without = [c.value for c in next_3]
        possible = [(c_value - d) % (self.max_value + 1) for d in [1,2,3,4,5]]
        for p in possible:
            if p != 0 and p not in without:
                return self.nodes[p]

    def play_round(self):
        destination = self.find_destination_for_current()
        after_destination = destination.next
        new_next = self.current.next.next.next.next
        first_to_move = self.current.next
        last_to_move = self.current.next.next.next

        destination.next = first_to_move
        first_to_move.prev = destination

        after_destination.prev = last_to_move
        last_to_move.next = after_destination

        self.current.next = new_next
        new_next.prev = self.current

        self.current = new_next

    def first_two_after_one(self):
        one = self.nodes[1]
        return [one.next.value, one.next.next.value]

cups = [int(n) for n in list("925176834")]
ring = RingWithIndexing(cups, 1000000)
for _ in range(10000000):
    ring.play_round()

print(ring.first_two_after_one()[0] * ring.first_two_after_one()[1])