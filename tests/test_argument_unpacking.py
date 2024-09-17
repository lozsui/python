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

def concat_kw_args(**kwargs):
    concated_str = ""
    for k, v in kwargs.items():
        concated_str += f"{str(k)}: {v} "
    return concated_str

def test_kw_args():
    result = concat_kw_args(person_1="Sam", person_2="Hans")
    assert "person_1: Sam person_2: Hans " == result

def test_kw_args_two():
    result = concat_kw_args(person_1="Sam", person_2="Hans", person_3="Hermann")
    assert "person_1: Sam person_2: Hans person_3: Hermann " == result