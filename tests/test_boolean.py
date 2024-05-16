
def test_bigger_or_equal():
    bigger_or_equal = 42 >= 41
    assert bigger_or_equal
    bigger_or_equal = 42 >= 42
    assert bigger_or_equal
    bigger_or_equal = 42 >= 43
    assert not bigger_or_equal