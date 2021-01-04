"""
No comment.
"""

import pandas as pd

import pytest

import ppl.btxlsx


def test_create_df():
    df = ppl.btxlsx.create_df()
    array = [['Car', 4], ['Tomato', 6], ['Carpet', 14]]
    assert df.iloc[0]['Item'] == 'Car'
    assert df.iloc[0]['Quantity'] == 4
    assert df.iloc[1]['Item'] == 'Tomato'
    assert df.iloc[1]['Quantity'] == 6
    assert df.iloc[2]['Item'] == 'Carpet'
    assert df.iloc[2]['Quantity'] == 14


def test_concat_xlsx_sheets():
    """
    No comment.
    """
    df = ppl.btxlsx.concat_xlsx_sheets()
    series_object = df.iloc[0]
    assert series_object['Item'] == 'Tomato'
    assert series_object['Quantity'] == 3
    series_object = df.iloc[7]
    assert series_object['Item'] == 'Carpet'
    assert series_object['Quantity'] == 12


@pytest.mark.parametrize("test_input,expected", [
    ('Car', 6),
    ('Tomato', 11),
    ('Carpet', 18),
    ('Toy', 154)])
def test_group_and_sum(test_input, expected):
    df = ppl.btxlsx.group_and_sum()
    assert df[test_input] == expected
