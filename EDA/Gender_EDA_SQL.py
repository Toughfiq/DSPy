import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns

#Load data menggunakan database config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
gender_df = load_column('gender')
#Memulai pembersihan data
def Gender_Def (value):
    if pd.isna(value): #Fungsi pd.isna() mengecek satu nilai (value) apakah NaN atau tidak.
        return 'Unknown'
    value = str(value).strip()  # Mengganti spasi atau white space menjadi type string agar terbaca
    if value.lower() == 'female':
        return 'Female'
    elif value.lower() == 'male':
        return 'Male'
    elif value.lower() == 'genderfluid':
        return 'Genderfluid'
    elif value.lower() in ['non-binary', 'nonbinary']: #mencegah adanya kesalah menulis
        return 'Non-binary'
    elif value.lower() in ['prefer not to say', 'prefer not to answer']:
        return 'Prefer Not to Say'
    else:
        return value.title()  # Kapitalisasi respon lain  
gender_df['gender'] = gender_df['gender'].apply(Gender_Def) #inisiasi data yang sudah dibersihkan kembali ke gender_df

# 3.perhitungan data
gender_counts = gender_df['gender'].value_counts()
gender_percent = gender_df['gender'].value_counts(normalize=True) * 100

print("Unique values:", gender_df['gender'].unique()) #mengambil unique value setelah pembersihan
print("\nCounts:\n", gender_counts) #menghitung frekuensi tiap gender yang ada
print("\nPercentages:\n", gender_percent.round(2)) #menampilkan presentase dengan pembulatan 2 desimal
