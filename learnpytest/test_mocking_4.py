from typer.testing import CliRunner
from cards.cli import app
import cards
import pytest
import shlex

"""
Im Gegensatz zu den Tests in test_mocking_3.py testet man
hier realitätsnaher.

Es wird eine Test-Datenbank benützt, welche durch das fixture
'cards_db' gegeben ist.
"""

runner = CliRunner()


@pytest.fixture(scope="module")
def db_path(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    return db_path

@pytest.fixture()
def cards_db(db_path, monkeypatch):
    monkeypatch.setenv("CARDS_DB_DIR", str(db_path))
    db_ = cards.CardsDB(db_path)
    db_.delete_all()
    yield db_
    db_.close()

"""
Test-Methode die zeigt, weshalb 'cards_cli' und 'cards_db' die
gleiche Datenbank benutzen.

Das fixture cards_db die Umgebungsvariable 'CARDS_DB_DIR' der
Werte von 'CARDS_DB_DIR' ist bestimmt durch das fixture 'db_path'.
"""
def test_show_config(cards_db, db_path):
    print()
    print(runner.invoke(app, "config").stdout.rstrip())
    print(db_path)


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    print()
    print(runner.invoke(app, "config").stdout.rstrip())
    output = result.stdout.rstrip()
    return output
    
def test_add_with_owner(cards_db):
    cards_cli("add A Theroy about Everyting -o Sam")
    expected = cards.Card("A Theroy about Everyting", owner="Sam", state="todo")
    all_cards = cards_db.list_cards()
    assert len(all_cards) == 1
    assert all_cards[0] == expected

