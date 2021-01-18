# -*- coding: utf-8 -*-

"""
No comment.
"""

import pandas as pd

import pytest

import ppl.popstuff as popstuff


@pytest.mark.parametrize("test_input,expected", [(3, 6), (33, 36), (-1, 2)])
def test_value_plus3(test_input, expected):
    """
    No comment.
    """
    assert popstuff.value_plus_3(test_input) == expected


@pytest.mark.parametrize("expected", ['aaa'])
def test_using_os(expected):
    """
    No comment.
    """
    assert popstuff.using_os() == expected


def test_get_coordinates():
    """
    No comment.
    """
    assert popstuff.get_coordinates('Peter Gugelhopf') == (1, 2)


def test_merge_xlsx():
    """
    No comment.
    """
    popstuff.merge_xlsx()
    my_df = pd.read_excel('xlsx_C.xlsx')
    author = my_df.iloc[1, 3]
    assert author == 'Peter Gugelhopf'


@pytest.mark.parametrize("test_input,expected", [('SIC', 118), ('CIR', 113)])
def test_code_to_number(test_input, expected):
    """
    No comment.
    """
    assert popstuff.code_to_number(test_input) == expected


def test_list_comprehension_one():
    """
    No comment.
    """
    concated_list = popstuff.list_comprehension_one()
    list_of_strings = ['1', '2', '3', '4', '5', '6']
    assert concated_list == list_of_strings


def test_maybe_combinatorics():
    """
    No comment.
    """
    rank_suit_tuples = popstuff.maybe_combinatorics()
    assert rank_suit_tuples[0] == ('2', 'spades')
    assert rank_suit_tuples[1] == ('3', 'spades')
    assert rank_suit_tuples[2] == ('4', 'spades')


def test_cantons_construct_one():
    """
    No comment.
    """
    cantons = popstuff.Cantons()
    canton = cantons[0]
    assert canton.name == 'Appenzell Innerrhoden'
    assert canton.capital == 'Appenzell'
