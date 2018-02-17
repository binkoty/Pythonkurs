import enum
import random
from collections import Counter

#SUITS = ['h','c','d','s']


class Suits(enum.IntEnum):
        Clubs = 1
        Diamonds = 2
        Hearts = 3
        Spades = 4

class HandValue(enum.IntEnum):
    high_card = 0
    pair = 1
    two_pair = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8
    royal_flush = 9



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
        return self.value

    def give_card(self):
        return self.card

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


class Hand():
    def __init__ (self):
        self.hand = []
        self.currentcard = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.currentcard == len(self.hand):
            raise StopIteration
        else:
            self.currentcard += 1
            return self.hand[self.currentcard - 1]

    def __add__(self, other):
        for card in self.hand:
            other.hand.append[card]

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

    def best_poker_hand(self, cards):
        self.all_av_cards = cards + self.hand
        self.poker_hands = []
        self.check_pairs(self.all_av_cards)
        self.check_straight_flush(self.all_av_cards)
        for x in self.poker_hands:
            x.show()


    def check_pairs(self, cards):

        vals = [(c.value, c.suit) for c in cards]
        #print(vals)
        cnt = Counter()
        for c in cards:
            cnt[c.value] += 1
        #print(cnt)
        # Find the card ranks that have at least a pair
        twoval = [i[0] for i in cnt.items() if i[1] >= 2]
        twoval.sort()


        found_pairs = False
        for n in twoval:
            found_pairs = True
        # print (suits)
        if found_pairs:
            self.poker_hands.append (PokerHand(HandValue.pair, twoval))

    def check_straight_flush(self, cards):
        """
        Checks for the best straight flush in a list of cards (may be more than just 5)

        :param cards: A list of playing cards.
        :return: None if no straight flush is found, else the value of the top card.
        """
        vals = [(c.give_value(), c.suit) for c in cards] \
               + [(1, c.suit) for c in cards if c.give_value() == 14]  # Add the aces!
        for c in reversed(cards):  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.give_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                self.poker_hands.append (PokerHand(HandValue.straight_flush, c.value))

    def check_full_house(cards):
        """
        Checks for the best full house in a list of cards (may be more than just 5)

        :param cards: A list of playing cards
        :return: None if no full house is found, else a tuple of the values of the triple and pair.
        """
        value_count = Counter()
        for c in cards:
            value_count[c.give_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()

        # Threes are dominant in full house, lets check that value first:
        for three in reversed(threes):
            for two in reversed(twos):
                if two != three:
                    return three, two



class PokerHand:

    def __init__(self, type, cards):             #cardval = [highestcard1, hc2]
        self.type = HandValue(type)
        self.card_val = cards
        self.val = []
        self.val = [self.type, self.card_val]

    def __lt__(self, other):
        for n in range(0,len(self.val)):
            if self.val[n] < other.val[n]:
                return self.val[n] < other.val[n]

    def show(self):
        print (self.type, self.card_val)

class BestPokerHand:

    def check_pairs(cards):
        cnt = Counter()
        for n, card in enumerate(cards):
            cnt[card[n]] += 1
        print (cnt)

    def check_straight(self, cards):

        vals = [(c.give_value(), c.suit) for c in cards] \
               + [(1, c.suit) for c in cards if c.give_value() == 14]




deck1 = Deck()

deck1.shuffle()

#deck1.show()

vhand = Hand()

vhand.draw(2,deck1)
board = Hand()
board.draw(5, deck1)
print('hand')
vhand.sort()
vhand.show()
print ('board')
board.sort()
board.show()
vhand.best_poker_hand(board.hand)
#vhand.poker_hand.show()
ahand = Hand()
ahand.draw(2, deck1)
ahand.best_poker_hand(board.hand)
#ahand.poker_hand.show()

#if ahand.poker_hand < vhand.poker_hand:
#    print ('devetdu')


#print (vhand.hand[0])


#print ('kvar i decket')
