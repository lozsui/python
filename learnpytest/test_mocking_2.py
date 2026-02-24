from unittest import mock

import cards
import pytest
from cards.cli import app
from typer.testing import CliRunner

"""
Diese Test mit "-s" Option ausführen, damit man die Print-Statements
sieht. Noch besser ist Ausführen mit "-v -s".
"""

runner = CliRunner()

def test_mock_version():
    with mock.patch.object(cards, "__version__", "1.2.3"):
        result = runner.invoke(app, ["version"])
        assert result.stdout.rstrip() == "1.2.3"

"""
Dies ist ein 'Zwischenschritt'.
"""
def test_mock_CardsDB():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        print()
        print(f"       class:{MockCardsDB}")
        print(f"return_value:{MockCardsDB.return_value}")
        with cards.cli.cards_db() as db:
            print(f"      object:{db}")

def test_mock_path():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        MockCardsDB.return_value.path.return_value = "/foo/"
        with cards.cli.cards_db() as db:
            print()
            print(f"{db.path=}")
            print(f"{db.path()=}")

"""
Um zu verstehen, was hier passiert hilft es:

- cli.config anzugucken
- test_mock_CardsDB und test_mock_path zu verstehen
"""
@pytest.fixture()
def mock_cardsdb():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value

def test_config(mock_cardsdb):
    """
    Mit der Zeile unten wird db.path() aus cli.py gemocked.
    """
    mock_cardsdb.path.return_value = "/foo/"
    result = runner.invoke(app, ["config"])
    assert result.stdout.rstrip() == "/foo/"

"""
Diesen Test ist nur hier um zu zeigen, dass autospec (siehe
mock_cardsdb fixture) einem davor bewahrt im Test Attribute zu
haben, welche es im zu testenden Objekt gar nicht gibt.
"""
def test_autospec_helps(mock_cardsdb):
    with pytest.raises(AttributeError):
        mock_cardsdb.does_not_exist.return_value = "db has no attribute 'does_not_exist"
