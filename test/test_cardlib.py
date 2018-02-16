from nose.tools import assert_raises

def test_math():

    assert 1 + 1 == 2
    assert 2 * 2 + 3 == 7
    # It is important to also test strange inputs,
    # like dividing what zero and see that good exceptions are thrown.
    # What happens if you try create a card with numerical value 0 or -1?
    with assert_raises(ZeroDivisionError):
        1 / 0
