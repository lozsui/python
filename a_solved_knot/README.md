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

# On Debug

Im launch.json hat es in 'configurations' zwei Konfigurationen: 'Debug Simple' und 'Debug With EVN File'. Mit 'Debug Simple' kann man irgendeine Datei öffnen, auf das 'Run/Debug' Icon gehen, 'Debug Simple' auswählen und so das aktuell geöffnete Skript ausführen oder eben debuggen. Wenn das Skript ein '.env' benötigt, geht man analog vor, benützt aber 'Debug With ENV File'.

Zum Ausprobieren kann man 'hello_world.py' oder 'debug_with_env_file.py' im Ordner 'on_debug' verwenden.

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

# On Open Ports

Es handelt sich um ein Kommandozeilen-Programm. Man kann es benützen, um mit Python zu prüfen, ob auf einem Host Port XY geöffnet ist.

```
(.venv) PS C:\Temp\python\a_solved_knot\on_open_ports> python.exe .\check_port.py --help
```

# On os

## file_listener.py

Ein Beispiel zur Methode 'os.listdir(MEIN_PFAD)'.

# On Parsing Things

Mein Beispiel hier benützt 'xml.etree.ElementTree'. 'ElementTree' scheint geeignet zu sein für einfaches XML 'parsing' sowie Manipulation.

# On Pydantic

Es hat erst ein Beispiel wie man 'Settings' (eine Konfiguration) in einem Ojekt 'Settings' darstellen kann.

# On Requests

'requests==2.32.5' im requirements.txt ist insbesondere für die Requests-Beispiele da.

Beispiele wie das Packet 'requests' benutzt werden kann:

- Plain Vanilla Verwendung
- Verwendung mit einem Proxy
- Abfragen eines Token
- Authorisierung mit Verwendung eines Token

## Getting Started

Im selben Ordner wo requests_examples.py gespeichert ist, muss es eine Datei 'proxy_settings.py' geben mit einem Inhalt wie im Listing unten gezeigt.

```
proxies = {
    "http": "http://secret:sauce@foo:8080",
    "https": "http://secret:sauce@foo:8080",
}
```

```
python requests_examples.py --help
```

# On SNB API

On playing with data api of Swiss National Bank. And an exmple on Plotting data using matplotlib.pyplot.

# On Type Hints

Bei Ramalho (2022) has a chapter 8 'Type Hints in Functions' and chapter 15 'More About Type Hints'.

Die Beispiele dieses Abschnitts bedürfen der Installtion des Python-Packets mypy (siehe ../requirements.txt).

TIPP: Am besten den Code in 'on_type_hints' lesen und wenn man nicht versteht, was passiert eine KI fragen. MIT DEM CODE HERUMSPIELEN!

Siehe im Listing unten 'to get started'.

    (.venv) PS C:\Temp\python\a_solved_knot\on_type_hints> mypy .

# On Visualizing Dataflow

Das funktioniert noch nicht.

# Anhang

## Links

- Ramelhos (2022) examples can be found on [github](https://github.com/fluentpython/example-code-2e/tree/master/

## Literatur

- Ramalho 2022: Ramalho, Luciano; Fluent Python 2nd Edition, 2022

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
