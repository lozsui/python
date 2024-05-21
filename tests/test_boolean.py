
def test_bigger_or_equal():
    bigger_or_equal = 42 >= 41
    assert bigger_or_equal
    bigger_or_equal = 42 >= 42
    assert bigger_or_equal
    bigger_or_equal = 42 >= 43
    assert not bigger_or_equal

def test_in_between():
    my_number = 5
    my_number_between_0_and_10 = my_number > 0 and my_number < 10
    assert my_number_between_0_and_10

def test_and_or():
    assert bool("Sam")
    assert bool(42)
    assert not bool("")
    assert not bool(0)

    # Some hints about and
    second_if_true_or_false = "Sam" and "Hermann"
    assert second_if_true_or_false == "Hermann"
    second_if_true_or_false = "Sam" and ""
    assert second_if_true_or_false == ""

    # Some hints about or
    first_if_both_true = "Sam" or "Hermann"
    assert first_if_both_true == "Sam"
    # and so on...


