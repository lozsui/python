from dataclasses import dataclass
from typing import TypeVar


@dataclass
class Vehicle:
    name: str


class Bicycle(Vehicle):
    gears: int


class Car(Vehicle):
    hair_color: str


class ElectricCar(Car):
    battery_size: int


class PetrolOrDieselCar(Car):
    tanz_size: int


TypeVar('T', bound=Car)

def concat_cars(cars: list[Car]) -> str:
    concated_cars = ''
    for car in cars:
        concated_cars = concated_cars + str(car)
    return concated_cars

if __name__ == "__main__":
    cars = [
        ElectricCar("Tesla"),
        PetrolOrDieselCar("BMW")
    ]
    concat_cars(cars)
    bicycles = [
        Bicycle("Scott"),
        Bicycle("Bianchi")
    ]
    concat_cars(bicycles)