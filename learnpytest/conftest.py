"""
Hint: Although conftest.py is a Python module, it should not be imported
by test files. The conftest.py file gets read by pytest automatically, so
you don’t have import conftest anywhere.
"""
from pathlib import Path  # used in chapter 3 
from tempfile import TemporaryDirectory # used in chapter 3 
import cards
import pytest


def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"


def pytest_addoption(parser):
    """This is called a 'hook function'"""
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="new db for each test",
    )


@pytest.fixture(scope=db_scope)
def db_chapter3_version():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    """CardsDB object connected to a temporary database"""
    db_path = tmp_path_factory.mktemp("cards_db")
    db_ = cards.CardsDB(db_path)
    yield db_
    db_.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def some_cards():
    """List of different card objects"""
    return [
        cards.Card("write app on appuio", "todo"),
        cards.Card("migrate lpz timerec to docker", "done"),
        cards.Card("read pytest book by brian", "todo"),
        cards.Card("become happy as larry", "todo"),
    ]


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    """CardsDB oject that's been populated with 'some_cards'"""
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db

