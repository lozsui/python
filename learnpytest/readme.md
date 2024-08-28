# Introduction

Code in this folder is supposed to help me while reading [Python Testing with Pytest by Brian Okken](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/).

My bookmark: [Sharing Fixtures in conftest.py](https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0037.xhtml#sharing_conftest)

# Setting Up on Micro$oft Window$ 10

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

# Run test(s)

```
pytest test_count.py
pytest -k test_empty
```

Next, https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0037.xhtml#sharing_conftest