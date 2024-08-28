import cards


def test_empty(cards_db):
        count = cards_db.count()
        assert count == 0

def test_two(cards_db):
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))
    count = cards_db.count()
    assert count == 2
