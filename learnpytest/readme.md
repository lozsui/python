# Setting Up on Windows

```
PS C:\Temp\python\learnpytest> & C:/GNOT/python/python.3.11.2/python.exe -m venv .venv
PS C:\Temp\python\learnpytest> .venv/Scripts/Activate.ps1
(.venv) PS C:\Temp\python> python -m pip install  --proxy http://USER:PASSWORD@YOUR.PROXY:PORT --upgrade pip
(.venv) PS C:\Temp\python\learnpytest> pip install --proxy http://USER:PASSWORD@YOUR.PROXY:PORT ./cards_proj
```

As of July 9 this setup fails with error message as stated below.

```
ERROR: No matching distribution found for flit_core<4,>=3.2
```

# Run test(s)

```
pytest test_count.py
pytest -k test_empty
```

Next, https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0037.xhtml#sharing_conftest