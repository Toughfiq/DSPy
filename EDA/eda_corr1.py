import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns
#Ambil config Databases dulu
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
eda_corr_df = load_columns(['gender', 'sexual_orientation']) #gunakan list untuk load beberapa collumns
print(eda_corr_df['sexual_orientation'].unique)