"""
It is said that in Python functions are 'first class citizens'. While I don't understand that
in all the details, I think this is about things that are an implication of
that.
"""

import pytest

@pytest.fixture
def the_answer():
    return 42

# Hint: fcc in test_function_as_fcc stands for first class citizen.
def test_function_as_fcc(the_answer):
    assert 42 == the_answer

