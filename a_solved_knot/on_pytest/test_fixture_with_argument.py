import pytest
from typing import Callable, Optional

@pytest.fixture(scope="session", name="with_argument")
def fixture_with_argument() -> Callable[[Optional[str]], str]:
    def _inner(argument: Optional[str] = None) -> str:
        if not argument:
            return "No argument passed"
        return argument
    return _inner

def test_with_argument_fixture(with_argument):
    assert "No argument passed" == with_argument()
    assert "Passed argument" == with_argument("Passed argument")
