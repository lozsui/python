from dataclasses import dataclass
from collections.abc import Iterable


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
    fuel_tank_size: int


def concat_cars(cars: list[Car]) -> str:
    concated_cars = ''
    for car in cars:
        concated_cars = concated_cars + str(car)
    return concated_cars

def concat_vehicles(vehicles: Iterable[Vehicle]) -> str:
    concated_vehicles = ''
    for vehicle in vehicles:
        concated_vehicles = concated_vehicles + str(vehicle)
    return concated_vehicles

if __name__ == "__main__":
    bicycles = [
        Bicycle("Scott"),
        Bicycle("Bianchi")
    ]
    """
    In der Zeile unten kriegt man einen Fehler, weil:

    'incompatible type "list[Bicycle]"; expected "list[Car]"
    """
    concat_cars(bicycles)
    concat_vehicles(bicycles)

    vehicles = [
        Bicycle("Scott"),
        ElectricCar("Tesla"),
        PetrolOrDieselCar("Mercedes")
    ]
    concat_vehicles(vehicles)
