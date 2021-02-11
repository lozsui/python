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


def test_my_first_genexps_example():
    dishes = fp.create_dishes_three()
    # assert len(dishes) == 4
    # TypeError: object of type 'generator' has no len()
    expected_dishes = [
        'rigatoni al pesto',
        'spaghetti al pesto',
        'rigatoni alla bolognese',
        'spaghetti alla bolognese',
    ]
    i = 0
    print()
    for d in dishes:
        assert d == expected_dishes[i]
        i += 1


def test_tuples_one():
    calling_codes = [('Afghanistan', '+93'), ('Australia', '+61'), ]
    i = 0
    for calling_code in calling_codes:
        """
        The % formatting operator understands tuples and
        treats each item as a separate field.
        """
        cc = '%s: %s' % calling_code
        if i == 0:
            assert cc == 'Afghanistan: +93'
        else:
            assert cc == 'Australia: +61'
        i += 1


def test_tuples_two():
    calling_codes = [('Afghanistan', '+93'), ('Australia', '+61'), ]
    i = 0
    for country, _ in calling_codes:
        if i == 0:
            assert country == 'Afghanistan'
        else:
            assert country == 'Australia'
        i += 1


def test_tuples_swap():
    first = 'Samuel'
    second = 'Bächler'
    first, second = second, first
    assert first == 'Bächler'
    assert second == 'Samuel'


def test_prefixing_with_star():
    t = (20, 8)
    quotient, remainder = divmod(*t)
    assert quotient == 2
    assert remainder == 4


def test_if_object_is_changeable():
    """
    'changeable_tuple' is changable since something can be added to
    list [3, 4].
    """
    changeable_tuple = (1, 2, [3, 4])
    unchangeable_tuple = (1, 2, (3, 4))
    b_false = False
    b_true = True
    # changeable_tuple[0] = 10
    # TypeError: 'tuple' object does not support item assignment
    assert b_false == fp.fixed(changeable_tuple)
    assert b_true == fp.fixed(unchangeable_tuple)


def test_github_communication():
    assert 1 == 1
