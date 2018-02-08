import random

class playingcards:

class hand:
    def __init__ (self):
        self._hand = []

    def add_card(self, amount, deck):
        new_card = deck[random.randint(0, len(deck))]
        self._hand.append(new_card)

    def droppingcards(self, index):
        for i in index:
            self._hand.remove(self._hand[i])

    def show_hand:
        print (_hand)