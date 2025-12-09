# Inhaltsverzeichnis

- [Virtual Environment auf Windows](#virtual-Environment-auf-Windows)
- [Virtual Environment auf Linux](#virtual-Environment-auf-Linux)



# Einleitung

Es geht hier darum mein Python wissen zu repetieren und es in meinen Alltag einzubetten.

# On Built in Functions

## test_filter.py

Beispiel zum Filtern einer Zahlenliste oder einer Objektliste (Personen).

# On CMD Util

This code is supposed to show how a command line util can be setup. Es benützt die Libraty [Typer on pypi.org](https://pypi.org/project/typer).

## Getting Started mit Command Line Util

    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py --help
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello --help
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello Samuel
    (.venv) shb@lx1g9:~/003-github.com/python/a_solved_knot/cmd_util$ python cli.py hello "Hans Jürgen"

# On Exceptions

TODO: Write something about it.

# On Klassen

Bei Luciano Ramalho (Fluent Python) habe ich zu 'Data Class Builder' dazugelernt. Wie man im Buch 'Fluent Python' liest kann man als 'Shortcuts' die unten genannten Konstrukte brauchen, um 'data classes' zu schreiben:

- collections.namedtuple
- typing.NamedTuple
- @dataclasses.dataclass

Spannend finde ich in seinem Buch folgenden Hinweis: "After covering those class builders, we will discuss why Data Class is also the name of a code smell: a coding pattern that may be a symptom of poor object-oriented design.'

# On Logging

In 'on_fastapi' kann man schauen, wie logging im Kontext von fastapi und uvicorn konfiguriert werden kann.

Example one to five are copied from ['Logging HOWTO by Vinay Sajip'](https://docs.python.org/3/howto/logging.html). They
can be considered as simple getting started examples.

> The basic classes defined by the module, together with their attributes and methods, are listed in the sections below.
> - Loggers expose the interface that application code directly uses.
> - Handlers send the log records (created by loggers) to the appropriate destination.
> - Filters provide a finer grained facility for determining which log records to output.
> - Formatters specify the layout of log records in the final output.

Source: https://docs.python.org/3/library/logging.html

Für die Logging-Beispiele sind inbesondere folgende Packete wichtig:

- python-json-logger==4.0.0
- asgi-correlation-id==4.3.4

## Formatter

- https://docs.python.org/3/library/logging.html#formatter-objects

Für Möglichkeiten für den Formatierungsstring (siehe fmt im Listing unten) siehe
https://docs.python.org/3/library/logging.html#logrecord-attributes.

```
formatter = logging.Formatter(
    fmt="%(filename)s %(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
    style="%",
)
```

## Log Levels

- https://docs.python.org/3/library/logging.html#logging-levels

## Weitere Links

- ['Capture Log Fixture in Pytest'](../learnpytest/test_log.py)

# On Mathematics

Siehe auch https://docs.python.org/3/library/numeric.html

## test_decimal_round.py

Ein Anfang um zu lernen wie man mit Python zahlen runden kann. TODO: Herausfinden wie man 1/3 auf 1.35 runden kann.

# On os

## file_listener.py

Ein Beispiel zur Methode 'os.listdir(MEIN_PFAD)'.

# On Parse Things

Mein Beispiel hier benützt 'xml.etree.ElementTree'. 'ElementTree' scheint geeignet zu sein für einfaches XML 'parsing' sowie Manipulation.

# On Visualizing Dataflow

Das funktioniert noch nicht.

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

### Aktuell verwendetes .venv

Im Listing unten ist gezeigt, wie man herausfindet, in welchem .venv man sich gerade befindet.

    (.venv) PS C:\Temp\python> python
    >>> import sys
    >>> print(sys.prefix)
    C:\Temp\python\a_solved_knot\.venv

### Virtual Environment auf Linux

    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ python -m venv .venv
    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ source .venv/bin/activate

### Virtual Environment auf Windows

Im Listing unten ein Beispiel wie ein '.venv' auf Windows aktiviert wird.

    PS C:\Temp\python\a_solved_knot> python.exe -m venv .venv
    PS C:\Temp\python\a_solved_knot> .\.venv\Scripts\Activate.ps1

Im Listing unten ist gezeigt wie pip auf Windows aktualsiert werden kann.

    (.venv) PS C:\Temp\python\a_solved_knot> python -m pip install --upgrade pip
