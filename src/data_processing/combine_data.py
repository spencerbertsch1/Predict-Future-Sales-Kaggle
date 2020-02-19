"""

Combine the files from the kaggle competition into a single dataframe

This file can be run as a python script by calling the main method at the bottom of the file.

"""

# native imports
import argparse
import path
import datetime

# package imports
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

"""
Import raw data from .csv files for cleaning and combination
"""

def import_data(path: str):
    path = '/Users/spencerbertsch/Desktop/Courses/Coursera/Predict-Future-Sales-Kaggle/src/data/'
    transactions    = pd.read_csv(str(path + 'sales_train.csv'))
    items           = pd.read_csv(str(path + 'items.csv'))
    item_categories = pd.read_csv(str(path + 'item_categories.csv'))
    shops           = pd.read_csv(str(path + 'shops.csv'))
    return(transactions, items, item_categories, shops)

def format_data(transactions):
    transactions.date = transactions.date.apply(lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
    # we can now look at the updated data type for the date feature
    print(transactions.info())

    #This line of code was borrowed from: https://www.kaggle.com/jagangupta/time-series-basics-exploring-traditional-ts
    monthly_sales = transactions.groupby(["date_block_num", "shop_id", "item_id"])[
        "date", "item_price", "item_cnt_day"].agg({"date": ["min", 'max'], "item_price": "mean", "item_cnt_day": "sum"})

    print(monthly_sales.head(10))


if __name__ == '__main__':
    print('...combining csv files...')
    parser = argparse.ArgumentParser(description='Import csv files for merging')
    parser.add_argument('--import_path', type=str,
                        help='path to the directory containing all csv files for import')

    args = parser.parse_args()
    import_path = args.import_path
    print(import_path)

    # import data
    transactions, items, item_categories, shops = import_data(path=import_path)
    format_data(transactions)


