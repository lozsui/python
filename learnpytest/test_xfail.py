import pytest
from packaging.version import parse
import cards
from cards import Card

"""
Siehe auch "-r" Option im REAME.md.
"""


@pytest.mark.xfail(
        parse(cards.__version__).major < 2,
        reason="Card < comparison not supported in 1.x"
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2

"""
Obwohl 'c1 == c2' False ist, gibt es kein 'failed' sondern ein XPASS (expected to fail but passed).
"""
@pytest.mark.xfail(reason="XPASS demo")
def test_xpass():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2

"""
Im Gegensatz zu 'test_xpass' wird hier mit 'strict=True' explizit verlangt, dass 'failed' kommt.
"""
@pytest.mark.xfail(reason="strict demo", strict=True)
def test_xfail_strict():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
