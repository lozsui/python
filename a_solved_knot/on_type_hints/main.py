from dataclasses import dataclass

from methods import parse_token

@dataclass
class Animal:
    name: str


if __name__ == "__main__":
    animal = Animal("Yoy")
    parse_token(animal)
