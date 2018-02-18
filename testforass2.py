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

    def show_poker_hand(self):
        for x in self.poker_hands:
            if x:
                x.show()

    def check_pair(cards):

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
        x = Hand.check_pair(cards)
        if x:
            if len(x.card_val) > 1:
                return PokerHand(HandValue.two_pair, x.card_val)

    def check_three_kind(cards):

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

        :param cards: A list of playing cards.
        :return: None if no straight flush is found, else the value of the top card.
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
                return PokerHand(HandValue.straight_flush, [c.value])


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
                    return PokerHand(HandValue.full_house, [three, two])

    def check_royal_sflush(cards):

        x = Hand.check_straight_flush(cards)
        if x:
            if x.card_val == [14]:
                return PokerHand(HandValue.royal_flush, x.card_val)



class PokerHand:

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

    def show(self):
        print (self.type, self.card_val)

