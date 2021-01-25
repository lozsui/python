# -*- coding: utf-8 -*-

"""
No comment.
"""

from ppl.fp import Vector


def test_to_string():
    v = Vector(3, 8)
    str_v = str(v)
    assert str_v == 'Vector(3, 8)'


def test_vector_addition():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_multiply_vector_with_scalar():
    v1 = Vector(1, 2)
    v2 = v1 * 5
    assert v2.x == 5
    assert v2.y == 10


def test_absolute_vector_value():
    v = Vector(4, 3)
    assert 5 == abs(v)
