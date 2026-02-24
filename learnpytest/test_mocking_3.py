from unittest import mock
import pytest
import cards
from cards.cli import app
import shlex
from typer.testing import CliRunner


runner = CliRunner()

"""
Genau gleich wie in test_mocking_2.py
"""
def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


"""
Genau gleich wie in test_mocking_2.py
"""
@pytest.fixture()
def mock_cardsdb():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value


"""
HBD: Diese Beispiel habe ich noch nicht durch und durch verstanden.

Mein aktuelles Verständnis: Die Methode 'assert_called_with' überprüft
lediglich, ob die Methode 'add_card' mit den korrekten Argumenten
aufgerufen wurde.

'assert_called_with' ist eine Funktion aus der unittest.mock Werkzeugkiste (siehe
https://docs.python.org/3/library/unittest.mock.html).
"""
def test_add_with_owner(mock_cardsdb):
    """
    Beachte, dass 'add' dem CLI-Kommando entspricht.
    """
    cards_cli("add Theory about Everything -o Sam")
    expected = cards.Card("Theory about Everything", owner="Sam", state="todo")
    mock_cardsdb.add_card.assert_called_with(expected)


"""
'side_effect' ist eine Funktion aus der unittest.mock Werkzeugkiste (siehe
https://docs.python.org/3/library/unittest.mock.html).
"""
def test_delete_invalid(mock_cardsdb):
    mock_cardsdb.delete_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("delete 42")
    assert "Error: Invalid card id 42" in out