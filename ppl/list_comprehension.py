# -*- coding: utf-8 -*-

"""
List comprehension examples.
"""


def add_one(list):
    return [elem + 1 for elem in list]


def select_numbers(list):
    return [elem for elem in list if type(elem) is str]
