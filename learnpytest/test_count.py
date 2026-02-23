import cards
import pytest

@pytest.mark.run_these_please
def test_AHY45rt33FYK():
        print("test_AHY45rt33FYK")
        assert True == True

def test_empty(cards_db):
        count = cards_db.count()
        assert count == 0

def test_two(cards_db):
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))
    count = cards_db.count()
    assert count == 2
