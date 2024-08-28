import pytest

def concat_three_values(a, b, c):
    return f"{a} {b} {c}"

def add_up_numbers(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result

def test_no_unpacking():
    values = [
        "Apples",
        "Bananas",
        "Beer"
    ]
    with pytest.raises(TypeError):
        concat_three_values(values)

def test_unpacking():
    values = [
        "Apples",
        "Bananas",
        "Beer"
    ]
    result = concat_three_values(*values)
    assert "Apples Bananas Beer" == result

def test_add_up_numbers():
    assert add_up_numbers() == 0
    assert add_up_numbers(1,2) == 3
    assert add_up_numbers(1,2,3) == 6    