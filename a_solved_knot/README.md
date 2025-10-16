# Inhaltsverzeichnis

- [Virtual Environment auf Windows](#virtual-Environment-auf-Windows)
- [Virtual Environment auf Linux](#virtual-Environment-auf-Linux)

# Einleitung

Es geht hier darum mein Python wissen zu repetieren und es in meinen Alltag einzubetten.

# Klassen

Zur Zeit noch keinen Inhalt

# Anhang

## pytests ausführen

Im Listing unten ist gezeigt, wie die Tests auf dem Abschnitt 'classes' ausgeführt werden können.

    (.venv) rupert@lx1g9:~/003-github.com/python/a_solved_knot$ pytest classes/test_classes.py

## VS Code Extensions

    rupert@lx1g9:~/003-github.com/python$ code --list-extensions
    ms-python.debugpy
    ms-python.python
    ms-python.vscode-pylance
    ms-python.vscode-python-envs

Stand 16. Oktober 2025

## Virtual Environment auf Linux

    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ python -m venv .venv
    rupert@lx1g9:~/003-github.com/python/a_solved_knot$ source .venv/bin/activate

## Virtual Environment auf Windows

Im Listing unten ein Beispiel wie ein '.venv' auf Windows aktiviert wird.

    PS C:\Temp\python> .venv/Scripts/Activate.ps1
    (.venv) PS C:\Temp\python\classes> pytest


