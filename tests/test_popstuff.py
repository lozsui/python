# -*- coding: utf-8 -*-

"""
No comment.
"""

import pytest

from ppl.popstuff import value_plus_3


@pytest.mark.parametrize("test_input,expected", [(3, 6), (33, 36), (-1, 2)])
def test_value_plus3(test_input, expected):
    """
    No comment.
    """
    assert value_plus_3(test_input) == expected
