"""
Run it with 'pytest -v -m smoke test_start.py'

and put

[pytest]
markers =
    smoke: subset of tests

into a file called pytest.ini.
"""


import pytest
from cards import Card, InvalidCardId


@pytest.mark.smoke
def test_start(cards_db):
    """
    stat changes state form "todo" to "in prog"
    """
    i = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(i)
    assert cards_db.get_card(i).state == "in prog"


@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    any_number = 123 # any number will be invalid, db is empty
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)
