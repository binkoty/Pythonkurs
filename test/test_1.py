import testforass2

def test_card():
    assert testforass2.JackCard(testforass2.Suits.Hearts).give_value() == 11


