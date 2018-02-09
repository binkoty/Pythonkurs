import random

class playingcards:

class hand:
    def __init__ (self):
        self.hand = []

    def generate(self):

        self.hand =

    def add_card(self, amount, deck):
        new_card = deck[random.randint(0, len(deck))]
        self.hand.append(new_card)

    def droppingcards(self, index):
        for i in index:
            self.hand.remove(self.hand[i])

    def show_hand(self):
        print (self.hand)