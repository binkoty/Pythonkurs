import random
suits = ['h','c','d','s']

class PlayingCard():
    def __init__(self):

    def give_value(self):
        raise NotImplementedError("Missing give_value implementation")

class NumberedCard (Playingcard):
    def __init__(self, value, suit):
        self.card = (value, suit)

    def give_value(self):
        print (self.card[0])

class JackCard (Playingcard):
    def __init__(self, suit):
        self.card = (11, suit)

    def give_value(self):
        print (self.card[0])

class QueenCard (Playingcard):
    def __init__(self, suit):
        self.card = (12, suit)

    def give_value(self):
        print (self.card[0])

class KingCard (Playingcard):
    def __init__(self, suit):
        self.card = (13, suit)

    def give_value(self):
        print (self.card[0])

class AceCard (Playingcard):
    def __init__(self, suit):
        self.card = (14, suit)

    def give_value(self):
        print (self.card[0])

class Deck:
    def __init__(self):
        self.deck = []
        while len(deck) < 52:
            for suit in suits:


class Hand:
    def __init__ (self):
        self.hand = []

    def generate(self, handsize, deck):
        for element in handsize:
            self.hand.append(deck[random.randint(0, len(deck))])

    def add_card(self, amount, deck):
        new_card = deck[random.randint(0, len(deck))]
        self.hand.append(new_card)
        deck.remove(new_card)

    def droppingcards(self, index):
        for i in index:
            self.hand.remove(self.hand[i])

    def show_hand(self):
        print (self.hand)




viktor = hand()

viktor.generate()

viktor.showhand