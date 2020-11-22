# -*- coding: utf-8 -*-

"""
Testing package ppl.
"""

import pytest

from ppl.popstuff import value_plus_3


@pytest.mark.parametrize("test_input,expected", [(3, 6), (33, 36), (-1, 2)])
def test_value_plus3(test_input, expected):
    """
    This text is for pylint.
    """
    assert value_plus_3(test_input) == expected
