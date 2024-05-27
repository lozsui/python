"""
Inspired by https://github.com/PacktPublishing/The-Complete-Python-Course/tree/master/1_intro/lectures
"""

def test_int_is_int():
    my_int = 35
    assert isinstance(my_int, int)
    assert not isinstance(my_int, float)

def test_float_is_float():
    my_float = 35.25
    assert not isinstance(my_float, int)
    assert isinstance(my_float, float)

def test_integer_division():
    result = 12 // 3
    assert isinstance(result, int)

def test_integer_division_rounded():
    result = 8 // 3
    assert isinstance(result, int)
    assert result == 2

def test_float_division():
    result = 12 / 3
    assert isinstance(result, float)

def test_modulo():
    result = 13 % 5
    assert result == 3

