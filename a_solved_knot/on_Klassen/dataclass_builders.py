from typing import NamedTuple
from dataclasses import dataclass

class Dog():

    def __init__(self, name, sex):
        self.name: str = name
        self.sex: str = sex
    
    def __repr__(self):
        return f"Dog(name='{self.name}', sex='{self.sex}')"


class NamedTupleDog(NamedTuple):
    name: str
    sex: chr


@dataclass
class DataclassDog:
    name: str
    sex: chr
