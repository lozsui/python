# python
This is an attempt to consolidate my python Know-how.

## Setup Python Environment

### Debian Bullseye

#### Compilation for Debian Bullseye

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

#### Setting Up a Virtual Environment

Assume the Python interpreter was installed to 'C:\GNOT\Python' and this project is cloned to 'C:\GIT\GITHUB\python'.

> PS C:\GIT\GITHUB\python> & C:/GNOT/Python/python.exe -m venv .venv

#### Install Requirements

> PS C:\GIT\GITHUB\python> & C:/GIT/GITHUB/python/.venv/Scripts/Activate.ps1
> 
> (.venv) PS C:\GIT\GITHUB\python> python -m pip install -r requirements.txt

If there is a proxy:

>  (.venv) PS C:\GIT\GITHUB\python> python -m pip install --proxy http://USER:PASSWORD@YOUR.PROXY:PORT -r requirements.txt

#### Run Tests

Activate your .venv and type command as in listing below.

> PS C:\GIT\GITHUB\python> & C:/GIT/GITHUB/python/.venv/Scripts/Activate.ps1
> 
> python -m pytest