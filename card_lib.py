import enum
import random
from collections import Counter

class Suits(enum.IntEnum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

class HandValue(enum.IntEnum):
    high_card = 0
    pair = 1
    two_pair = 2
    three_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_kind = 7
    straight_flush = 8
    royal_flush = 9


class PlayingCard():
    """
            PlayingCard class containing methods for comparison which are inherited to the different card-classes
    """
    def __init__(self):
        pass

    def give_value(self):
        raise NotImplementedError("Missing give_value implementation")

    def __lt__(self, other):
        return (self.value, self.suit) < (other.value, other.suit)

    def __eq__(selfs, other):
        return (self.value, self.suit) == (other.value, other.suit)


class NumberedCard (PlayingCard):
    """
            Class for a regular numbered playingcard

    """

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.card = (value, suit)

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

    def give_value(self):
        return (self.value)

    def give_suit(self):
        return (self.suit)


class JackCard (PlayingCard):
    """
           Class for a Jack card
    """

    def __init__(self, suit):
        self.value = 11
        self.suit = suit
        self.card = (11, suit)

    def give_value(self):
        return (self.value)

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class QueenCard (PlayingCard):
    """
           Class for a Queen card
    """

    def __init__(self, suit):
        self.value = 12
        self.suit = suit
        self.card = (12, suit)

    def give_value(self):
        return (self.value)

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class KingCard (PlayingCard):
    """
           Class for a King card
    """
    def __init__(self, suit):
        self.value = 13
        self.suit = suit
        self.card = (13, suit)

    def give_value(self):
        return self.value

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"

class AceCard (PlayingCard):
    """
           Class for an Ace
    """
    def __init__(self, suit):
        self.value = 14
        self.suit = suit
        self.card = (14, suit)

    def give_value(self):
        return (self.value)

    def __str__(self):
        return "(" + str(self.value) + str(self.suit) + ")"


class Deck:
    """
           Class that makes up the carddeck, constructor creating a deck with 52 different cards
    """

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
        """
           Shuffles the deck
        """
        random.shuffle(self.deck)

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))
        return str(cards)

    def draw_top(self):
        """
           Draws the top card of the deck
        """
        topcard = self.deck[0]
        self.deck.remove(topcard)
        return topcard


class Hand():
    """
           Creates a Hand class
    """
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

    def __str__(self):
        cards = []
        for card in self.hand:
            cards.append(str(card))
        return str(cards)

    def draw(self, amnt, deck):
        """
               Method for drawing the top card from a specific deck
               Params: amnt = amount of cards, deck = the deck from which cards should be drawn
        """
        for size in range(0,amnt):
            self.hand.append(deck.draw_top())

    def sort(self):
        """
           Method for sorting the hand in reference to value and suit
        """
        self.hand = sorted(self.hand)

    def droppingcards(self, index):
        """
                   Removes cards from the hand in the indexed locations
                   param: index = list of indices
        """
        for i in index:
            self.hand.remove(self.hand[i])

    def best_poker_hand(self, cards):

        """
           Calculates the best pokerhand for self.hand together with a given amount of cards (usually the board)
           param: cards = the board, or other list of cards
        """

        self.all_av_cards = cards + self.hand
        self.poker_hands = []

        self.hand.sort()
        self.poker_hands += [PokerHand(HandValue.high_card, [self.hand[1].value, self.hand[1].suit])]       #add high card pokerhand

        self.poker_hands += [Hand.check_pair(self.all_av_cards)]
        self.poker_hands += [Hand.check_two_pair(self.all_av_cards)]
        self.poker_hands += [Hand.check_straight(self.all_av_cards)]
        self.poker_hands += [Hand.check_flush(self.all_av_cards)]
        self.poker_hands += [Hand.check_straight_flush(self.all_av_cards)]          #check for pokerhands
        self.poker_hands += [Hand.check_full_house(self.all_av_cards)]
        self.poker_hands += [Hand.check_three_kind(self.all_av_cards)]
        self.poker_hands += [Hand.check_four_kind(self.all_av_cards)]
        self.poker_hands += [Hand.check_royal_sflush(self.all_av_cards)]

        self.best_hand = max(self.poker_hands)
        return self.best_hand

    def check_pair(cards):
        """
           Checks for pairs in given list of cards
           param cards: A list of playing cards.
        """

        cnt = Counter()
        for c in cards:
            cnt[c.value] += 1

        twoval = [i[0] for i in cnt.items() if i[1] >= 2]
        twoval.sort()

        found_pair = False
        if twoval:
            found_pair = True

        if found_pair:
            return PokerHand(HandValue.pair, twoval)


    def check_two_pair(cards):

        """
           Checks for two pairs in given list of cards
           param cards: A list of playing cards.
        """

        x = Hand.check_pair(cards)
        if x:
            if len(x.card_val) > 1:
                return PokerHand(HandValue.two_pair, x.card_val)

    def check_three_kind(cards):

        """
           Checks for three of a kind in given list of cards
           param cards: A list of playing cards.
        """


        cnt = Counter()
        for c in cards:
            cnt[c.value] += 1

        threeval = [i[0] for i in cnt.items() if i[1] >= 3]
        threeval.sort()

        found_three_kind = False
        if threeval:
            found_three_kind = True

        if found_three_kind:
            return PokerHand(HandValue.three_kind, threeval)

    def check_four_kind(cards):
        """
           Checks for four of a kind in given list of cards
           param cards: A list of playing cards.
        """


        cnt = Counter()
        for c in cards:
            cnt[c.value] += 1

        fourval = [i[0] for i in cnt.items() if i[1] >= 4]
        fourval.sort()

        found_four_kind = False
        if fourval:
            found_four_kind = True

        if found_four_kind:
            return PokerHand(HandValue.four_kind, fourval)

    def check_straight(cards):
        """
        Checks for the best straight in a list of cards (may be more than just 5)

        param cards: A list of playing cards.
        """

        vals = [(c.value) for c in cards] \
               + [(1) for c in cards if c.value == 14]  #adding aces
        for c in reversed(cards):  # Starting point (high card)

            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.value - k) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return PokerHand(HandValue.straight, [c.value])


    def check_flush(cards):
        """
           Checks for flush in given list of cards
           param cards: A list of playing cards.
        """



        cnt = Counter()
        for c in cards:
            cnt[c.suit] += 1

        flush = [i[0] for i in cnt.items() if i[1] >= 5]

        found_flush = False
        if flush:
            found_flush = True

        if found_flush:
            return PokerHand(HandValue.flush, flush)


    def check_straight_flush(cards):
        """
        Checks for the best straight flush in a list of cards (may be more than just 5)

        param cards: A list of playing cards.
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
                return PokerHand(HandValue.straight_flush, [c.value])


    def check_full_house(cards):
        """
        Checks for the best full house in a list of cards (may be more than just 5)

        param cards: A list of playing cards
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
                    return PokerHand(HandValue.full_house, [three, two])

    def check_royal_sflush(cards):
        """
           Checks for royal flush in given list of cards
           param cards: A list of playing cards.
        """


        x = Hand.check_straight_flush(cards)
        if x:
            if x.card_val == [14]:
                return PokerHand(HandValue.royal_flush, x.card_val)



class PokerHand:
    """
       Class representing a pokerhand
       param cards: A list of playing cards.
    """

    def __init__(self, type, cards):             #cardval = [highestcard1, hc2]
        self.type = HandValue(type)
        self.card_val = cards
        self.val = []
        self.val = [self.type, self.card_val]

    def __lt__(self, other):
        if self:
            if other:
                for n in range(0,len(self.val)):
                    if self.val[n] < other.val[n]:
                        return self.val[n] < other.val[n]


