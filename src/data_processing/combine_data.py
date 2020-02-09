"""

Combine the files from the kaggle competition into a single dataframe

"""

# Imports
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

"""
Import raw data from .csv files for cleaning and combination
"""
transactions    = pd.read_csv(os.path.join(DATA_FOLDER, 'sales_train.csv.gz'))
items           = pd.read_csv(os.path.join(DATA_FOLDER, 'items.csv'))
item_categories = pd.read_csv(os.path.join(DATA_FOLDER, 'item_categories.csv'))
shops           = pd.read_csv(os.path.join(DATA_FOLDER, 'shops.csv'))