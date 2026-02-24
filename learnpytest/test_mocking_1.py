from typer.testing import CliRunner
from cards.cli import app
import shlex


"""
Diese Tests mit "-s" Option ausführen, damit man die Print-Statements
sieht.

test_typer_runner benützt die 'produktive'Datenbank. Wo sich die produktive
Datenbank befindet, findet man mit

cards config
C:/Users/olmert/cards_db

heraus.
"""
runner = CliRunner()
def test_typer_runner():
    result = runner.invoke(app, ["version"])
    print()
    print(f"version: {result.stdout}")
    result = runner.invoke(app, ["list", "-o", "brian"])
    print(f"list:\n{result.stdout}")


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_cards_cli():
    result = cards_cli("version")
    print()
    print(f"version: {result}")

    result = cards_cli("list -o brian")
    print(f"list:\n{result}")
