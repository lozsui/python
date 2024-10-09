from typing import Protocol, Any
from collections.abc import Iterable
from typing import TypeVar


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LT = TypeVar('LT', bound=SupportsLessThan)

def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
