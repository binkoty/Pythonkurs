SUITS = ['h','c','d','s']

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

class JackCard (PlayingCard):
    def __init__(self, suit):
        self.value = 11
        self.suit = suit
        self.card = (11, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

class QueenCard (PlayingCard):
    def __init__(self, suit):
        self.value = 12
        self.suit = suit
        self.card = (12, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

class KingCard (PlayingCard):
    def __init__(self, suit):
        self.value = 13
        self.suit = suit
        self.card = (13, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)

class AceCard (PlayingCard):
    def __init__(self, suit):
        self.value = 14
        self.suit = suit
        self.card = (14, suit)

    def give_value(self):
        return (self.value)

    def give_card(self):
        return (self.card)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for val in range(2,11):
                self.deck.append(NumberedCard(val,suit))
            self.deck.append(JackCard(suit))
            self.deck.append(QueenCard(suit))
            self.deck.append(KingCard(suit))
            self.deck.append(AceCard(suit))

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

    def droppingcards(self, index):
        for i in index:
            self.hand.remove(self.hand[i])

    def show(self):
        for card in self.hand:
            print (card.give_card())


deck1 = Deck()

vhand = Hand()

vhand.show()

vhand.draw(5,deck1)

print ('kort i hand')

vhand.show()

print ('kvar i decket')

deck1.show()