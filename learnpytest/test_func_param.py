"""
In this test the same thing is done by

- @pytest.mark.parametrize
- Using a fixture
- Using test generation

"""


import pytest
from cards import Card


def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second edition", state="in prog"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card("write a book", state="done"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card("create a course", state="todo"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ]
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)


    cards_db.finish(index)


    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish_simple(cards_db, start_state):
    c = Card("One fits all", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.fixture(params=["done", "in prog", "todo"], name="start_state")
def start_state_fixture(request):
    return request.param


def test_finish_with_fixture(cards_db, start_state):
    c = Card("One fits all", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def pytest_generate_tests(metafunc):
    if "start_state_gen" in metafunc.fixturenames:
        metafunc.parametrize("start_state_gen", ["done", "in prog", "todo"])


def test_finish_test_generation(cards_db, start_state_gen):
    c = Card("One fits all", state=start_state_gen)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
    