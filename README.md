# python
This is an attempt to consolidate my python Know-how.

## Setup Python Environment

### Debian Bullseye

#### Compilation for Debian Bullseye

According to [install-dependencies](https://devguide.python.org/setup/#install-dependencies) build dependencies can be installed as follows:
> apt build-dep python3.9

Next according to README.rst type:
> ./configure --prefix="/home/shb/python-3.9.1" --enable-optimizations
> make 
> make test
> ...snip
> 
> == Tests result: SUCCESS ==
> 
> 411 tests OK.
> 
> 14 tests skipped:
>    test_devpoll test_gdb test_ioctl test_kqueue test_msilib
>    test_ossaudiodev test_startfile test_tix test_tk test_ttk_guionly
>    test_winconsoleio test_winreg test_winsound test_zipfile64
>
> Total duration: 7 min 46 sec
> Tests result: SUCCESS
> make install

In case command above does not do the trick install these packages:
>  build-essential bzip2-doc libbz2-dev libffi-dev libgdbm-dev libncurses-dev libnss3-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev liblzma-dev tk-dev

#### Setting Up a Virtual Environment
Install pip and virtualenv:
> python3-pip python3-virtualenv

Set up virtual environment:
> mkdir ~/venv-play-python
> 
> virtualenv -p ~/python-3.9.1/bin/python3 venv-play-python

