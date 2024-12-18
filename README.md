# python

An attempt to consolidate my python Know-how.

## Index

- [Challenges](#challenges)
- [Classes](./classes/readme.md)
- [Further Reading](#further-reading)
  - [The Complete Python Course](#the-complete-python-course)
- [Git Configuration](#git-configuration)
- [Logging](./ex001logging/README.md)
- [Pytest](./learnpytest/readme.md)
- [Setting Up a Virtual Environmen](#setting-up-a-virtual-environment)

## Git Configuration

>snip...
>
>[remote "origin"]<br>
>	url = https://GITHUB_USER:TOKEN@github.com/lozsui/python.git<br>
>	fetch = +refs/heads/*:refs/remotes/origin/*


## Setup Python Environment

I try to use .venv in root folder of this project for most things. See [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)

### Ubuntu 22.04.2 LTS

#### Setup Virtual Environment and Install Requirements

Create a virtual environment in the root folder of this project.

>python3 -m venv tests/.venv<br>
>source tests/.venv/bin/activate<br>
>(.venv) lozsui@host:~/python$ pip install -r requirements.txt

#### Run Tests

>source tests/.venv/bin/activate
>(.venv) lozsui@host:~/python$ export $(cat tests/.env | grep -v '^#')
>(.venv) lozsui@host:~/python/tests$ pytest test_*
>(.venv) lozsui@host:~/python/tests$ pytest -s test_*


### Debian Bullseye

#### Compilation for Debian Bullseye (the hard way)

1. [Get the source code](https://devguide.python.org/setup/#get-the-source-code)
2. [Install dependencies](https://devguide.python.org/setup/#install-dependencies)
3. Compile and install according to readme.rst

According to [install-dependencies](https://devguide.python.org/setup/#install-dependencies) build dependencies can be installed as follows:

> git clone https://github.com/python/cpython.git
> 
> git checkout v3.10.4
> 
> mkdir -p ~/python/python3.10.4_debug
> 
> ./configure --prefix="~/python/python3.10.4_debug" --with-pydebug
> 
> make
> 
> make test
> 
> make install

#### Setting Up a Virtual Environment

Set up virtual environment:
> mkdir ~/python/python-env
> 
> cd ~/python/python3.10.4_debug/
> 
> bin/virtualenv -p ~/python/python3.10.4_debug/bin/python3 ~/python/python-env

#### Install Requirements
> source ~/python/python-env/bin/activate
> 
> python -m pip install -r ~/003-GitHub/python/requirements.txt

#### Run Tests
> source ~/python/python-env/bin/activate
> 
> cd ~/003-GitHub/python/tests
> 
> python -m pytest

### Windows 10

#### Setting Up a Virtual Environment Windows

Assume the Python interpreter was installed to 'C:\GNOT\Python' and this project is cloned to 'C:\GIT\GITHUB\python'.

> PS C:\GIT\GITHUB\python> & C:/GNOT/Python/python.exe -m venv .venv

or

> PS C:\GIT\GITHUB\python> & python.exe -m venv .venv

or

> & C:/GNOT/python/python.3.11.2/python.exe -m venv .venv

if PS knows the path to your python binary. Put pip.ini like shown below into .venv folder.

```
[global]
proxy = http://proxy.highly.secure:8080
```

#### Install Requirements

> PS C:\Temp\python> .venv/Scripts/Activate.ps1
> (.venv) PS C:\Temp\python> python.exe -m pip install --upgrade pip
> (.venv) PS C:\Temp\python> python -m pip install -r requirements.txt

#### Run Tests

Activate your .venv and type command as in listing below.

> PS C:\GIT\GITHUB\python> & C:/GIT/GITHUB/python/.venv/Scripts/Activate.ps1
> 
> pytest

!!! Hint on 'No module named 'cards': This is because of 'test_count.py'. Either comment out these tests or install cards like so:

    (venv) $ cd .\learnpytest\
    (venv) $ pip install ./cards_proj/

# Challenges

- [Explore Python Package and Project Manager uv](https://docs.astral.sh/uv/)
- [Read Logging Tutorial](https://docs.python.org/3/howto/logging.html)
- [xfail of pytest boggles my mind](./learnpytest/test_xfail.py)

# Further Reading

## The Complete Python Course

Jose Salvatierra Fuentes created quite a nice course on Python. Code Snippets of this course on here: [Code on 'The Complete Python Course' on github](https://github.com/PacktPublishing/The-Complete-Python-Course).
