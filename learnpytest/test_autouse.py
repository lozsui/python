"""
Autouse fixtures don't have to be named by the test function.
"""

import pytest
import time


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """Report the time at the end of a session"""
    yield
    now = time.time()
    formatted_time = time.strftime("%d %b %X", time.localtime(now))
    print("--")
    print(
        f"finished {formatted_time}"
    )


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print("\ntest duration : {:0.3} seconds".format(delta))


def test_1():
    """Simulate long-ish running test"""
    time.sleep(1)


def test_2():
    """Simulate sighlty longer test"""
    time.sleep(1.23)