# -*- coding: utf-8 -*-

"""
No comment.
"""

import ppl.list_comprehension as lc


def test_first_list_comprehension():
    """ Test first_list_comprehension """
    result = lc.add_one([1, 2, 3])
    assert result[0] == 2
    assert result[1] == 3
    assert result[2] == 4

def test_select_strings():
    result = lc.select_numbers(["Hans Jürgen", 3, "Hermann", 42])
    assert result[0] == "Hans Jürgen"
    assert result[1] == "Hermann"
    assert len(result) == 2