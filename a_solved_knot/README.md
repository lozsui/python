# Inhaltsverzeichnis

- [Virtual Environment auf Windows](#virtual-Environment-auf-Windows)
- [Virtual Environment auf Linux](#virtual-Environment-auf-Linux)



# Einleitung

Es geht hier darum mein Python wissen zu repetieren und es in meinen Alltag einzubetten.

# CMD Util

This code is supposed to show how a command line util can be setup. Es benützt die Libraty [Typer on pypi.org](https://pypi.org/project/typer).

## Getting Started mit Command Line Util

    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py --help
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello --help
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello Samuel
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello "Hans Jürgen"

# Klassen

Bei Luciano Ramalho (Fluent Python) habe ich zu 'Data Class Builder' dazugelernt. Wie man im Buch 'Fluent Python' liest kann man als 'Shortcuts' die unten genannten Konstrukte brauchen, um 'data classes' zu schreiben:

- collections.namedtuple
- typing.NamedTuple
- @dataclasses.dataclass

Spannend finde ich in seinem Buch folgenden Hinweis: "After covering those class builders, we will discuss why Data Class is also the name of a code smell: a coding pattern that may be a symptom of poor object-oriented design.'

# Parse Things

Mein Beispiel hier benützt 'xml.etree.ElementTree'. 'ElementTree' scheint geeignet zu sein für einfaches XML 'parsing' sowie Manipulation.

# Anhang

## pytests ausführen

Im Listing unten ist gezeigt, wie alle Tests aus 'a solved knot' auf einmal ausgeführt werden können.

    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot$ pytest

Im Listing unten ist gezeigt, wie die Tests aus dem Abschnitt 'classes' ausgeführt werden können.

    (.venv) rupert@lx1g9:~/003-github.com/python/a_solved_knot$ pytest classes/test_classes.py

## VS Code Extensions

    rupert@lx1g9:~/003-github.com/python$ code --list-extensions
    ms-python.debugpy
    ms-python.python
    ms-python.vscode-pylance
    ms-python.vscode-python-envs

Stand 16. Oktober 2025

## pip

### Installierte Packete anzeigen

    (.venv) shb@lx1g9:~/003-github.com/python$ pip list

## Virtual Environments

### Virtual Environment auf Linux

    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ python -m venv .venv
    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ source .venv/bin/activate

### Virtual Environment auf Windows

Im Listing unten ein Beispiel wie ein '.venv' auf Windows aktiviert wird.

    PS C:\Temp\python\a_solved_knot> python.exe -m venv .venv
    PS C:\Temp\python\a_solved_knot> .\.venv\Scripts\Activate.ps1
    