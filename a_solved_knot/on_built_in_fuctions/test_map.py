def test_map_one():
    str_list = ['blah ', ' blub', ' foo ', '   bar             ']
    stripped_str_list = list(map(str.strip, str_list))
    for i in range(0, len(str_list)):
        assert str_list[i].strip() == stripped_str_list[i]

def test_ramalhos_example():
    """
    The map and filter functions are still built-ins in Python 3, but since
    the introduction of list comprehensions and generator expressions, they
    are not as important (Ramalho 2022).
    """
    def factorial(n):
        """returns n!"""
        return 1 if n < 2 else n * factorial(n - 1)
    factorials = list(map(factorial, range(6)))
    assert factorials[0] == 1
    assert factorials[1] == 1
    assert factorials[2] == 2
    assert factorials[3] == 6
    assert factorials[4] == 24
    assert factorials[5] == 120
