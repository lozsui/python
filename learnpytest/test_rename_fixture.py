import pytest


@pytest.fixture(name="ultimate_answer")
def ultimate_answer_fixture():
    """Example how renaming a fixture is done"""
    return 42


def test_everything(ultimate_answer):
    assert ultimate_answer == 42
