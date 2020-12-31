from collections import deque
from itertools import islice
def data():
    def parse_deck(deck):
        return deque([int(card) for card in deck.split("\n")[1:]])

    with open("./day22/data", "r") as file:
        return tuple([parse_deck(deck) for deck in file.read().split("\n\n")])

def score(deck):
    scoring_deck = list(reversed(deck))
    return sum([(i + 1) * card for i, card in enumerate(scoring_deck)]) 

def play_game(deck1, deck2):
    previous_decks = set()
    while(len(deck1) != 0 and len(deck2) != 0):
        if (tuple(deck1), tuple(deck2)) in previous_decks:
            return "player1", deck1
        previous_decks.add((tuple(deck1), tuple(deck2)))

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if len(deck1) >= card1 and len(deck2) >= card2:
            winner, _ = play_game(deque(islice(deck1.copy(), 0, card1)), deque(islice(deck2.copy(), 0, card2)))
        else:
            if card1 > card2:
                winner = "player1"
            else:
                winner = "player2"
        if winner == "player1":
            deck1.extend([card1, card2])
        elif winner == "player2":
            deck2.extend([card2, card1])

    if len(deck2) == 0:
        return "player1", deck1
    else:
        return "player2", deck2

init_deck1, init_deck2 = data()
print(score(play_game(init_deck1, init_deck2)[1]))