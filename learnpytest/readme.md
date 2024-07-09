# Setting Up

```
PS C:\Temp\python> .venv/Scripts/Activate.ps1
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