"""
cards_db, some_cards und non_empty_db sind fixtures, welche
in conftest.py definiert sind. Schau dort für weitere
Details.
"""

def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)
    for c in some_cards:
        cards_db.add_card(c)
    assert cards_db.count() == expected_count

def test_non_empty(some_cards, non_empty_db):
    assert len(some_cards) == non_empty_db.count()