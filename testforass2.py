import enum
import random
SUITS = ['h','c','d','s']


class Suits(enum.IntEnum):
        Clubs = 1
        Diamonds = 2
        Hearts = 3
        Spades = 4


class PlayingCard():
    def __init__(self):
        pass

    def give_value(self):
        raise NotImplementedError("Missing give_value implementation")



class NumberedCard (PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.card = (value, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

    def give_suit(self):
        return (self.suit)

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"


class JackCard (PlayingCard):
    def __init__(self, suit):
        self.value = 11
        self.suit = suit
        self.card = (11, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class QueenCard (PlayingCard):
    def __init__(self, suit):
        self.value = 12
        self.suit = suit
        self.card = (12, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class KingCard (PlayingCard):
    def __init__(self, suit):
        self.value = 13
        self.suit = suit
        self.card = (13, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class AceCard (PlayingCard):
    def __init__(self, suit):
        self.value = 14
        self.suit = suit
        self.card = (14, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

    def __lt__(self, other):
        if self.value == other.value:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"


class Deck:
    def __init__(self):
        self.deck = []

        for suit in Suits:
            for val in range(2,11):
                self.deck.append(NumberedCard(val,suit))
            self.deck.append(JackCard(suit))
            self.deck.append(QueenCard(suit))
            self.deck.append(KingCard(suit))
            self.deck.append(AceCard(suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def show(self):
        for card in self.deck:
            print (card.give_card())

    def give_size(self):
        return (len(self.deck))

    def draw_top(self):
        topcard = self.deck[0]
        self.deck.remove(topcard)
        return topcard


class Hand:
    def __init__ (self):
        self.hand = []

    def draw(self, amnt, deck):
        for size in range(0,amnt):
            self.hand.append(deck.draw_top())

    def sort(self):
        self.hand = sorted(self.hand)

    def droppingcards(self, index):
        for i in index:
            self.hand.remove(self.hand[i])

    def show(self):
        for card in self.hand:
            print (card.give_card())


def PokerHand:



deck1 = Deck()

deck1.shuffle()

deck1.show()

vhand = Hand()

vhand.show()

vhand.draw(15,deck1)

print ('kort i hand')
vhand.sort()
vhand.show()

#print ('kvar i decket')
