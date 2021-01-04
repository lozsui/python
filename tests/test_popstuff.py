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
