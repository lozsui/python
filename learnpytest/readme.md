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
PS C:\Temp\python\learnpytest> & C:/GNOT/python/python.3.11.2/python.exe -m venv .venv
```

At work where I need a proxy configuaration I had to put pip.ini into root of .venv.

```
PS C:\Temp\python\learnpytest> cat .venv/pip.ini
[global]
proxy = http://proxy.highly.secure:8080
```

And finally...

```
PS C:\Temp\python\learnpytest> .venv/Scripts/Activate.ps1
(.venv) PS C:\Temp\python\learnpytest> python.exe -m pip install --upgrade pip
(.venv) PS C:\Temp\python\learnpytest> pip install ./cards_proj
(.venv) PS C:\Temp\python\learnpytest> pip install -r requirements.txt
```

# Run tests

```
pytest test_count.py
pytest -k test_empty
```

# Pytest Command-Line Flags

```
pytest --help # is your friend
```


## Run Tests by Marker

```
pytest -m markerxy
```

See [Marker Example](./test_start.py)

## Show Print Statements "-s"

```
pytest -s test_whatever.py
Basic Test.
```

## Show Extra Test Summary "-r"

```
pytest -ra test_whatever.py
=== short test summary info === 
SKIPPED [1] test_whatever.py:5: Method XY not implemented yet
```

## Keywords

This is quite impressiv. See [Using Keywords to Select Test Cases in Brians book](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0060.xhtml)

## setup-show

```
PS C:\Temp\python\learnpytest> pytest --setup-show .\test_count.py
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
PS C:\Temp\python\learnpytest> pytest --fixtures -v
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
