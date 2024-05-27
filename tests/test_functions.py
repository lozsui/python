"""
Inspired by https://github.com/PacktPublishing/The-Complete-Python-Course/tree/master/2_intro_to_python/lectures

It is said that in Python functions are 'first class citizens'. While I don't understand that
in all the details, I think this is about things that are an implication of
that.
"""

import pytest

@pytest.fixture
def the_answer():
    return 42

# Hint: fcc in test_function_as_fcc stands for first class citizen.
# First class citizen feature is probably used for pytest.fixtures and
# that is why it put this code blow.
def test_function_fixture(the_answer):
    assert 42 == the_answer

def test_function_as_fcc():
    def the_answer():
        return 42
    my_func = the_answer
    assert 42 == my_func()

def test_function_as_fcc2():
    def the_answer(arg):
        return arg
    my_func = the_answer
    assert 42 == my_func(42)