# -*- coding: utf-8 -*-

"""
Idiosyncratic python things.
"""

import os

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
    'cell' where author is found. It is possibly not the smartest wqy
    to do that.
    """
    os.chdir('../files')
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
