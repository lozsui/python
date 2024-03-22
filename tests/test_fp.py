# -*- coding: utf-8 -*-

"""
No comment.
"""

import ppl.fp as fp


def test_to_string():
    """
    How __repr__ is used behind the scene.
    some more...
    """
    my_vector = fp.Vector(3, 8)
    str_v = str(my_vector)
    assert str_v == 'Vector(3, 8)'


def test_vector_addition():
    """
    Operator overloading example.
    """
    v_1 = fp.Vector(1, 2)
    v_2 = fp.Vector(3, 4)
    v_3 = v_1 + v_2
    assert v_3.x == 4
    assert v_3.y == 6


def test_multiply_vector_with_scalar():
    """
    Another operator overloading example.
    """
    v_1 = fp.Vector(1, 2)
    v_2 = v_1 * 5
    assert v_2.x == 5
    assert v_2.y == 10


def test_absolute_vector_value():
    """
    How __abs__ is used behind the scene.
    """
    v_1 = fp.Vector(4, 3)
    assert abs(v_1) == 5


def test_my_listcomp_one():
    """
    List comprehension ~ listcomp
    """
    one_two_three = [1, 2, 3, ]
    squared = fp.square_numbers(one_two_three)
    assert squared[0] == 1
    assert squared[1] == 4
    assert squared[2] == 9


def test_two_for_loops_listcomp_one():
    """
    Kind of nested listcomp.
    """
    dishes = fp.create_dishes()
    assert len(dishes) == 4
    assert dishes[0] == ('rigatoni', 'al pesto')
    assert dishes[1] == ('rigatoni', 'alla bolognese')
    assert dishes[2] == ('spaghetti', 'al pesto')
    assert dishes[3] == ('spaghetti', 'alla bolognese')


def test_two_for_loops_listcomp_two():
    """
    Shows outcome when nesting is in reversed order.
    """
    dishes = fp.create_dishes_two()
    assert len(dishes) == 4
    assert dishes[0] == ('rigatoni', 'al pesto')
    assert dishes[1] == ('spaghetti', 'al pesto')
    assert dishes[2] == ('rigatoni', 'alla bolognese')
    assert dishes[3] == ('spaghetti', 'alla bolognese')


def test_my_first_genexps_example():
    """
    genexp, unpacking, formatting
    """
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
    for dish in dishes:
        assert dish == expected_dishes[i]
        i += 1


def test_tuples_one():
    """
    The % formatting operator understands tuples and
    treats each item as a separate field. See for loop below.
    """
    calling_codes = [('Afghanistan', '+93'), ('Australia', '+61'), ]
    i = 0
    for calling_code in calling_codes:
        concated_cc = '%s: %s' % calling_code
        if i == 0:
            assert concated_cc == 'Afghanistan: +93'
        else:
            assert concated_cc == 'Australia: +61'
        i += 1


def test_tuples_two():
    """
    How to only use one part of the tuple.
    """
    calling_codes = [('Afghanistan', '+93'), ('Australia', '+61'), ]
    i = 0
    for country, _ in calling_codes:
        if i == 0:
            assert country == 'Afghanistan'
        else:
            assert country == 'Australia'
        i += 1


def test_tuples_swap():
    """
    Trick to swap variables
    """
    first = 'Samuel'
    second = 'Bächler'
    first, second = second, first
    assert first == 'Bächler'
    assert second == 'Samuel'


def test_prefixing_with_star():
    """
    Usage of star (asterisk) as method argument.
    """
    t_1 = (20, 8)
    quotient, remainder = divmod(*t_1)
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


S = '0123456789'


def test_slicing_example():
    """
    Slicing
    """
    step = 2
    assert S[::step] == '02468'
    start = 7
    assert S[start::step] == '79'
    step = 3
    assert S[::step] == '0369'
    stop = 7
    assert S[:stop:step] == '036'
    assert S[::10] == '0'


def test_slicing_in_reverse():
    """
    Slicing in reverse
    """
    assert S[::-1] == '9876543210'
    assert S[3::-1] == '3210'
    assert S[::-2] == '97531'
    assert S[3::-2] == '31'
    assert S[::-3] == '9630'
    assert S[::10] == '0'


def test_slice_method_example():
    """
    How slice can be used to handle fixed with formatted lines.
    """
    row = '01234567890123456789'
    row = 'Samuel Bächler    42'
    first_name = slice(0, 7)
    last_name = slice(7, 18)
    age = slice(18, 20)
    assert row[first_name] == 'Samuel '
    assert row[last_name] == 'Bächler    '
    assert row[age] == '42'


def test_mute_pylint_warning():
    """
    In case comment below is not in this bogus function pylint will complain
    'String statement has no effect [pointless-string-statement]'.

    In fp.ipynb in the notebooks section there are examples on

        - Grabbing Excess Items: a, b, *rest = range(5)
        - Grabbing Excess Items: a, *middle, b = range(5)
        - Nested Unpacking: person, age, height, (father, mother) in persons
        - Splitting: my_list[:2]
    """


def test_sequence_with_asterisk():
    """
    Multiply a list by a scalar.
    """
    my_abc = 'abc'
    assert my_abc[0] == 'a'
    assert 3 * my_abc == 'abcabcabc'
    l_1 = [1, 2]
    assert [1, 2, 1, 2, 1, 2] == 3 * l_1


def test_augmented_assignment_operators():
    """
    When augmented operator is used on mutable objects (e.g. list) then
    mostly '__iadd__' (in place addition) is used behind the scenes. Therefore
    the object remains the same.
    In case an augmented operator is used on immutable objects a new object
    will always be created.
    """
    l_1 = [1, 2]
    l_1_id = id(l_1)
    l_1 *= 3
    assert l_1_id == id(l_1)
    t_1 = (1, 2)
    t_1_id = id(t_1)
    t_1 *= 3
    assert t_1_id != id(t_1)
