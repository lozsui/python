
def test_lambda():
    average = lambda x: sum(x) / len(x)
    assert 2.5 == average([1, 2, 3, 4])