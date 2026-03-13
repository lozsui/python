# Introduction

Wenn man mit Modulen arbeitet, hat man manchmal das Problem, dass die Module nicht gefunden werden. Hier halte ich ein Projekt vor, wo diese Probleme nicht auftreten.

Für das Ausführen der 'pytests' scheint 'pytest.ini' im tests-Ordner entscheidend zu sein.

In 'launch.json' gibt es insbesondere

```
        {
            "name": "Proj Structure main",
            "type": "python",
            "request": "launch",
            "module": "a_project_structure.src.main",
            "console": "integratedTerminal",
            "args": ["-c", "config.json"]
        }
```

Dies hilt einem, um mit dem Debugger durch a_project_structure.src.main zu stolpern.

# Installing Requirments / Setup

Siehe README.md in a_solved_knot im Abschnitt 'Virtual Environments'.

HINT: ES KANN DAS '.venv' VON 'a_solved_knot' VERWENDET WERDEN.

# Run Tests

```
PS C:\Temp\python> .\a_solved_knot\.venv\Scripts\Activate.ps1
(.venv) PS C:\Temp\python\a_project_structure> pytest
```