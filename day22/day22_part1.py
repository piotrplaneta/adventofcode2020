from collections import deque
def data():
    def parse_deck(deck):
        return deque([int(card) for card in deck.split("\n")[1:]])

    with open("./day22/data", "r") as file:
        return tuple([parse_deck(deck) for deck in file.read().split("\n\n")])

def score(deck):
    scoring_deck = list(reversed(deck))
    return sum([(i + 1) * card for i, card in enumerate(scoring_deck)])

deck1, deck2 = data()

while(len(deck1) != 0 and len(deck2) != 0):
    card1 = deck1.popleft()
    card2 = deck2.popleft()

    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

print(score(deck1), score(deck2))