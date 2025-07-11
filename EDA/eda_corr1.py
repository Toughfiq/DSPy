import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns
from utils.cleaning import *
#Ambil config Databases dulu
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
eda_corr_df = load_columns(['gender', 'sexual_orientation']) #gunakan list untuk load beberapa collumns
eda_corr_df['gender'] = eda_corr_df['gender'].apply(clean_gender)
eda_corr_df['sexual_orientation'] = eda_corr_df['sexual_orientation'].apply(clean_orientation)
cross_tab = pd.crosstab(eda_corr_df['gender'], eda_corr_df['sexual_orientation'])
print(cross_tab)
plt.figure(figsize=(10, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Gender vs Sexual Orientation")
plt.xlabel("Sexual Orientation")
plt.ylabel("Gender")
plt.tight_layout()
plt.show()
