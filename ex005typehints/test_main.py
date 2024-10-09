import pytest

from methods import show_count
from methods import parse_token
from main import Animal


def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 childrens'


def test_parse_token():
    token = parse_token('ABCD')
    assert isinstance(token, str)

    token = parse_token('3.14')
    assert isinstance(token, float)


def test_parse_token_error():
    with pytest.raises(TypeError):
        animal = Animal(name="Ferdinand")
        parse_token(animal)
