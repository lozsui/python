# -*- coding: utf-8 -*-

"""
Idiosyncratic python things.
"""

import os
import collections

import pandas as pd


def value_plus_3(arg):
    """
    :param arg: Number
    :return: Number
    """
    return arg + 3


def using_os():
    """
    :return:
    """
    os.chdir('../files')
    file_list = os.listdir()
    if 'aaa' in file_list:
        return 'aaa'
    return None


def get_coordinates(author_to_find):
    """
    Pass the name of an author. Get row number and column number of
    'cell' where author is found. It is possibly not the smartest way
    to do that.
    """
    os.chdir('../files')
    # I used when debugging on VS code.
    # os.chdir('/home/shb/003-Git/github.com/lozsui/python/files')
    my_df = pd.read_excel('xlsx_B.xlsx')
    column_number = 0
    name_number_map = {}
    for col in my_df.columns:
        name_number_map[col] = column_number
        column_number += 1
    row_column_tuple = None
    for row in my_df.itertuples():
        author = row.Author
        if author == author_to_find:
            row_column_tuple = row.Index, name_number_map['Author']
    return row_column_tuple


def merge_xlsx():
    """
    Fill column Author in xlsx_A.xlsx with values found in xlsx_B.xlsx. Create
    xlsx_C.xlsx with merged Author information.
    """
    os.chdir('../files')
    # I used when debugging on VS code.
    # os.chdir('/home/shb/003-Git/github.com/lozsui/python/files')
    my_df_1 = pd.read_excel('xlsx_A.xlsx')
    my_df_2 = pd.read_excel('xlsx_B.xlsx')
    col_name_to_int_map = {
        'Author': 2,
        'Function': 0,
    }
    for row in my_df_1.itertuples():
        author = str(row[col_name_to_int_map['Author'] + 1])
        function = row[col_name_to_int_map['Function'] + 1]
        for other_row in my_df_2.itertuples():
            other_author = other_row[col_name_to_int_map['Author'] + 1]
            other_function = other_row[col_name_to_int_map['Function'] + 1]
            if function == other_function and author == 'nan':
                col_number = col_name_to_int_map['Author']
                my_df_1.iat[row.Index, col_number] = other_author
    my_df_1.to_excel('xlsx_C.xlsx')


def code_to_number(letter_code):
    d = {
        'S': 40,
        'C': 39,
        'I': 39,
        'R': 35,
        'E': 34,
        'A': 20,
    }
    return d[letter_code[0]] + d[letter_code[1]] + d[letter_code[2]]


def list_comprehension_one():
    part_one = [str(n) for n in range(1, 4)]
    part_two = [str(n) for n in range(4, 7)]
    return part_one + part_two


def maybe_combinatorics():
    """
    From 'A Pythonic Card Deck' by Luciano Ramalho (https://github.com/fluentpython/example-code-2e)
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    rank_suit_tuples = [(rank, suit) for suit in suits for rank in ranks]
    return rank_suit_tuples


Canton = collections.namedtuple('Canton', ['name', 'capital'])


class Cantons:

    def __init__(self):
        self._cantons = [
            Canton('Appenzell Innerrhoden', 'Appenzell'),
            Canton('Appenzell Ausserrhoden', 'Herisau'),
            Canton('Basel-Landschaft', 'Liestal'),
            Canton('Graubünden', 'Chur'),
            Canton('Jura', 'Delsberg'),
            Canton('Nidwalden', 'Stans'),
            Canton('Obwalden', 'Sarnen'),
            Canton('Thurgau', 'Frauenfeld'),
            Canton('Ticino', 'Bellinzona'),
            Canton('Uri', 'Altdorf'),
            Canton('Wallis', 'Sitten'),
            Canton('Vaud', 'Lausanne'),]

    def __len__(self):
        return len(self._cantons)

    def __getitem__(self, item):
        return self._cantons[item]


def tnr():
    cantons = Cantons()
    print(len(cantons))
    print(cantons[0])


if __name__ == "__main__":
    tnr()
