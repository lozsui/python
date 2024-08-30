import pytest
from packaging.version import parse
import cards
from cards import Card


@pytest.mark.skip(reason="Card doesn't support < comparision yet")
def test_skip():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


@pytest.mark.skipif(
        parse(cards.__version__).major < 2,
        reason="Card < comparision not supported in 1.x"        
)
def test_skip_if():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2


