import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns
from utils.cleaning import *
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
eda_gvsr_df = load_columns(['gender', 'swipe_right_ratio'])
print(eda_gvsr_df.head())
print(eda_gvsr_df.info())
print(eda_gvsr_df['swipe_right_ratio'].value_counts(dropna=False))
eda_gvsr_df['swipe_right_ratio'].drop_duplicates().to_csv('swipe.csv', index=False)
