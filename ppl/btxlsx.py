# -*- coding: utf-8 -*-

"""
Excel and VBA can be replaced by python, pandas et al. So, btxlsx stands for
'better than excel'.
"""

import os

import pandas as pd


def concat_xlsx_sheets():
    os.chdir('../files')
    first_records = pd.read_excel('pandas-001.xlsx')
    second_records = pd.read_excel('pandas-002.xlsx')
    frames = [first_records, second_records]
    df = pd.concat(frames, sort=False)
    return df


def group_and_sum():
    df = concat_xlsx_sheets()
    return df.groupby(by=['Item'])['Quantity'].sum()

    """
    index = result.index
    array = result.array
    my_dataframe = pd.DataFrame(array,
                                index=index,
                                columns=['Aggregated Quantities'])
    print(result['Car'])
    print('stop here')
    """

"""
def next():
    result = df.groupby(by=['Patient'])['Minuten'].sum()
    index = result.index
    array = result.array
    my_dataframe = pd.DataFrame(array, index=index, columns=['Agg Duration'])
    prices = my_dataframe['Agg Duration'] * (176.50/60.0)
    df_all = pd.merge(my_dataframe, prices, left_index=True, right_index=True)
    df_all['Agg Duration_y'].sum()
    print(df_all['Agg Duration_y'].sum() - 176.50)
    print(df_all)
    return 1300.0
"""


def create_df():
    index = [0, 1, 2]
    array = [['Car', 4], ['Tomato', 6], ['Carpet', 14]]
    columns = ['Item', 'Quantity']
    return pd.DataFrame(array, index=index, columns=columns)
