from pathlib import Path
from tempfile import TemporaryDirectory
import pytest

import cards


@pytest.fixture(scope='function')
def cards_db():
    print("\n ...cards_db fixture starting, change scope and see what happens...")
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_empty(cards_db):
        count = cards_db.count()
        assert count == 0

def test_two(cards_db):
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))
    count = cards_db.count()
    assert count == 2
