# -*- coding: utf-8 -*-

"""
No comment.
"""

import ppl.fp as fp


def test_to_string():
    v = fp.Vector(3, 8)
    str_v = str(v)
    assert str_v == 'Vector(3, 8)'


def test_vector_addition():
    v1 = fp.Vector(1, 2)
    v2 = fp.Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_multiply_vector_with_scalar():
    v1 = fp.Vector(1, 2)
    v2 = v1 * 5
    assert v2.x == 5
    assert v2.y == 10


def test_absolute_vector_value():
    v = fp.Vector(4, 3)
    assert 5 == abs(v)


def test_my_listcomp_one():
    one_two_three = [1, 2, 3, ]
    squared = fp.square_numbers(one_two_three)
    assert squared[0] == 1
    assert squared[1] == 4
    assert squared[2] == 9


def test_two_for_loops_listcomp_one():
    dishes = fp.create_dishes()
    assert len(dishes) == 4
    assert dishes[0] == ('rigatoni', 'al pesto')
    assert dishes[1] == ('rigatoni', 'alla bolognese')
    assert dishes[2] == ('spaghetti', 'al pesto')
    assert dishes[3] == ('spaghetti', 'alla bolognese')


def test_two_for_loops_listcomp_two():
    dishes = fp.create_dishes_two()
    assert len(dishes) == 4
    assert dishes[0] == ('rigatoni', 'al pesto')
    assert dishes[1] == ('spaghetti', 'al pesto')
    assert dishes[2] == ('rigatoni', 'alla bolognese')
    assert dishes[3] == ('spaghetti', 'alla bolognese')
