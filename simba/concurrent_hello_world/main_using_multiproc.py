import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin,
                      args=('thinking', done),
                      name='Spinner-Process')
    print(f'spinner object: {spinner}')
    """
    Above print statement prints something like
    spinner object: <Process name='Spinner-Process' parent=3028 initial>

    3028is the process ID of the Python instance running
    main_using_multiproc.py
    """
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Anwer: {result}')

if __name__ == '__main__':
    main()
