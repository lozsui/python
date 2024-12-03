# Intro

This code is supposed to show how a command line util can be setup.

# Run on Microsoft Windows 10

For this example to work requirements.txt and .venv in root folder can be used. As the time of this writing this is 'C:\Temp\python\requirements.txt' and 'C:\Temp\python\.venv'.

```
& C:/Temp/python/.venv/Scripts/Activate.ps1
(.venv) PS C:\Temp\python\cmd_util\cmd_util> python cli.py --help
(.venv) PS C:\Temp\python\cmd_util\cmd_util> python cli.py hello Sam
(.venv) PS C:\Temp\python\cmd_util\cmd_util> python cli.py goodbye Sam
```

# Links

- [Typer on pypi.org](https://pypi.org/project/typer)
