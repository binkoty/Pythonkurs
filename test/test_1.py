import testforass2

def test_card_value():
    assert testforass2.JackCard(testforass2.Suits.Hearts).give_value() == 11
    assert testforass2.QueenCard(testforass2.Suits.Hearts).give_value() == 12
    assert testforass2.KingCard(testforass2.Suits.Hearts).give_value() == 13
    assert testforass2.AceCard(testforass2.Suits.Hearts).give_value() == 14
    assert testforass2.NumberedCard(5, testforass2.Suits.Hearts).give_value() == 5
def test_suit():
    assert testforass2.Suits.Clubs == 1
    assert testforass2.Suits.Diamonds == 2
    assert testforass2.Suits.Hearts == 3
    assert testforass2.Suits.Spades == 4
def test_HandValue():
    assert testforass2.HandValue.high_card == 0
    assert testforass2.HandValue.pair == 1
    assert testforass2.HandValue.two_pair == 2
    assert testforass2.HandValue.three_kind == 3
    assert testforass2.HandValue.straight == 4
    assert testforass2.HandValue.flush == 5
    assert testforass2.HandValue.full_house == 6
    assert testforass2.HandValue.four_kind == 7
    assert testforass2.HandValue.straight_flush == 8
    assert testforass2.HandValue.royal_flush == 9


