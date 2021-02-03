# -*- coding: utf-8 -*-

"""
In this file I am experimenting with examples by Luciano Ramalho in
his book Fluent Python 2nd edition.
"""

import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)


def square_numbers(list_arg):
    return [x*x for x in list_arg]


def create_dishes():
    paste = ['rigatoni', 'spaghetti']
    sauces = ['al pesto', 'alla bolognese']
    return [(pasta, sauce) for pasta in paste for sauce in sauces]


def create_dishes_two():
    paste = ['rigatoni', 'spaghetti']
    sauces = ['al pesto', 'alla bolognese']
    return [(pasta, sauce) for sauce in sauces for pasta in paste]

