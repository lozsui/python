# Index

- [API Refernce of pytest](https://docs.pytest.org/en/latest/reference/reference.html)
- [Command-Line Flags](#pytest-command-line-flags)
- [Here be Dragons](#here-be-dragons)
- [Run test(s)](#run-tests)
- [Setting Up on Micro$oft Window$ 10](#setting-up-on-microsoft-windows-10)

# Pointer to Next

- [Using “and,” “or,” “not,” and Parentheses with Markers](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0071.xhtml)

# Introduction

Code in this folder is supposed to help me while reading [Python Testing with Pytest by Brian Okken](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/).

# Setting Up on Microsoft Windows 10

Initialize .venv

```
PS C:\GIT\github\python\learnpytest> C:\GNOT\python\python.3.11.2\python.exe -m venv .venv
```

At work where I need a proxy configuaration I had to put pip.ini into root of .venv.

```
PS C:\Temp\python\learnpytest> cat .venv/pip.ini
[global]
proxy = http://proxy.highly.secure:8080
```

And finally...

```
PS C:\GIT\github\python\learnpytest> .venv/Scripts/Activate.ps1
(.venv) PS C:\GIT\github\python\learnpytest> python -m pip install --upgrade pip
(.venv) PS C:\GIT\github\python\learnpytest> pip install ./cards_proj
(.venv) C:\GIT\github\python\learnpytest> pip install -r requirements.txt
```

# Run tests

Alle Tests ausführen:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest
```

Beachte, dass 'test_xfail.py::test_xfail_strict' auf die Schnauze fällt. Das ist beabsichtigt zu Demonstrationszwecken.

Test einzeln ausführen:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest .\test_count.py
```

# Pytest Command-Line Flags

```
pytest --help # is your friend
```

## Run Test by Keyword

Im Beispiel unten wird 'test_AHY45rt33FYK' aus 'test_count.py' ausgeführt:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -k AHY45rt33FYK
```

Im Beispiel unten werden alle Tests aus 'test_count.py' ausgeführt:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -k count
```

## Run Tests by Marker

Im Beispiel unten wird 'test_AHY45rt33FYK' aus 'test_count.py' ausgeführt, weil dort ein entsprechender Marker gesetzt ist:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -m run_these_please
```

BEACHTE, DASS run_these_please NICHT IN pytest.ini AUFGEFÜHRT IST. OFFENBAR BRAUCHT ES DIES IN NEUEREN pytest-VERSIONEN NICHT MEHR.

Siehe [Marker Example](./test_count.py)

Ein weiteres Beispiel wie man Marker verwenden kann findet man in 'test_func_param.py::test_finish_simple'.

## Increase Verbosity "-v"

Wenn man Test mit "-v"-Option ausführt, kriegt man wie unten gezeigt insbesondere eine detaillierte Ausgabe, welche Test mit insbesondere welchen Parameter ausgeführt wurden.

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -v
...SNIP...
test_autouse.py::test_1 PASSED [  2%]
...SNIP...
test_func_param.py::test_finish [write a book-done] PASSED [ 31%]
test_func_param.py::test_finish [second edition-in prog] PASSED [ 34%]
test_func_param.py::test_finish [create a course-todo] PASSED [ 36%] 
...SNIP...
test_less_than.py::test_skip SKIPPED (Card doesn't support < comparision yet) [ 57%] 
...SNIP...
test_xfail.py::test_less_than XFAIL (Card < comparison not supported in 1.x) [ 95%] 
test_xfail.py::test_xpass XPASS (XPASS demo) [ 97%] 
test_xfail.py::test_xfail_strict FAILED [100%] 
```

## Show Print Statements "-s"

Mit dieser Option kann man sich Print-Statements aus Tests ausgeben lasssen. Ein Beispieltest, um dies auszuprobieren ist:

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -s test_count.py
test_count.py test_AHY45rt33FYK
```

## Show Extra Test Summary "-r"

```
show extra test summary info as specified by chars
(f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
(p)passed, (P)passed with output, (a)all except pP.
```

### "-rp" vs "-rf" simpel

Die Option "-rp" zeigt 'short test summary info' aller tests, welche erfolgreich sind. Wenn man die gleichen Tests mit der Option "rf" ausführt, dann wird kein 'short test summary info' angezeigt, weil keine Tests "failen".

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -rp test_count.py
=== short test summary info === 
PASSED test_count.py::test_AHY45rt33FYK
PASSED test_count.py::test_empty
PASSED test_count.py::test_two
```

### XFAIL - expected to fail (-rx)

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -rx .\test_xfail.py
...SNIP...
=== short test summary info === 
XFAIL test_xfail.py::test_less_than - Card < comparison not supported in 1.x
```

### XPASS - expected to fail but passed (-rX)

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -rX .\test_xfail.py
...SNIP...
=== short test summary info === 
XPASS test_xfail.py::test_xpass - XPASS demo
```

## Trace Config

```
pytest --trace-config
PLUGIN registered: <_pytest.config.PytestPluginManager object at 0x7efcd9535550>
PLUGIN registered: <_pytest.config.Config object at 0x7efcd93bd4d0>
PLUGIN registered: <module '_pytest.mark' from '/usr/local/lib/python3.11/site-packages/_pytest/mark/__init__.py'>
PLUGIN registered: <module '_pytest.main' from '/usr/local/lib/python3.11/site-packages/_pytest/main.py'>

SNIP

============================= test session starts ==============================
platform linux -- Python 3.11.13, pytest-8.3.3, pluggy-1.6.0
using: pytest-8.3.3
active plugins:
    139624442975568     : <_pytest.config.PytestPluginManager object at 0x7efcd9535550>
    pytestconfig        : <_pytest.config.Config object at 0x7efcd93bd4d0>
    mark                : /usr/local/lib/python3.11/site-packages/_pytest/mark/__init__.py

SNIP

    terminalreporter    : <_pytest.terminal.TerminalReporter object at 0x7efcd940bed0>
    logging-plugin      : <_pytest.logging.LoggingPlugin object at 0x7efcd946c350>
    funcmanage          : <_pytest.fixtures.FixtureManager object at 0x7efcd9446a50>
rootdir: /builds/OE-5060/acme-calc/acme-calc-utils
collected 2 items

SNIP
============================== 2 passed in 0.20s ===============================
```

## pytest.ini / "-c"

Mit der Option '-c' kann man explizit vorgeben, welches pytest-Konfigurationsdatei verwendet werden soll.

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest -c .\pytest-demo.ini .\test_count.py
```

## Keywords

This is quite impressiv. See [Using Keywords to Select Test Cases in Brians book](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0060.xhtml)

## setup-show

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest --setup-show .\test_count.py
======================================================================================= test session starts ========================================================================================
platform win32 -- Python 3.11.2, pytest-8.3.2, pluggy-1.5.0
rootdir: C:\Temp\python\learnpytest
collected 2 items

test_count.py
SETUP    S cards_db
        test_count.py::test_empty (fixtures used: cards_db).
        test_count.py::test_two (fixtures used: cards_db).
TEARDOWN S cards_db
```

## fixtures

fixtures shows us a list of all available fixtures our test can use. This list includes a bunch of builtin fixtures that we’ll look at in the next chapter, as well as those provided by plugins.

```
(.venv) PS C:\GIT\github\python\learnpytest> pytest --fixtures -v
```

## capture

'--capture=no' tells pytest to turn off output capture. By default, pytest captures all output (such as print statements, logs, or other standard output and error messages) generated by the tests. This means that when tests are run, the output is not immediately displayed in the terminal but is instead captured and only shown if a test fails or if pytest is explicitly instructed to show it.

```
PS C:\Temp\python\learnpytest> pytest -s test_autouse.py
PS C:\Temp\python\learnpytest> pytest --capture=no test_autouse.py
```

# Here be Dragons

## Questions to Scope

- What does 'scope="module"' mean.