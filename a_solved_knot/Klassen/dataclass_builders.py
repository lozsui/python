from typing import NamedTuple
from dataclasses import dataclass


class NamedTupleDog(NamedTuple):
    name: str
    sex: chr


@dataclass
class DataclassDog:
    name: str
    sex: chr
