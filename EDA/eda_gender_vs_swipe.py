import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns
from utils.cleaning import *
from scipy.stats import f_oneway
######### lakukan config database dan ambil dari database SQL###############
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
eda_gsvr_df = load_columns(['gender', 'swipe_right_ratio']) #gunakan list untuk load beberapa collumns

# ==== Bersihkan Data ====
# Pastikan tidak ada nilai kosong
eda_clean_gvsr = eda_gsvr_df.dropna(subset=['gender', 'swipe_right_ratio'])

# Pastikan kolom numerik dalam format float
eda_clean_gvsr['swipe_right_ratio'] = pd.to_numeric(eda_clean_gvsr['swipe_right_ratio'], errors='coerce')
eda_clean_gvsr = eda_clean_gvsr.dropna(subset=['swipe_right_ratio'])

# ==== Tampilkan Rata-rata per Gender ====
print("\n=== Rata-rata Swipe Right Ratio per Gender ===")
mean_table = eda_clean_gvsr.groupby('gender')['swipe_right_ratio'].mean().sort_values(ascending=False)
print(mean_table)

# ==== Lakukan Uji ANOVA ====
# Buat list grup berdasarkan gender
groups = [group['swipe_right_ratio'] for name, group in eda_clean_gvsr.groupby('gender')]

# Lakukan uji ANOVA
stat, p = f_oneway(*groups)
print("\n=== Hasil Uji ANOVA ===")
print(f"F-statistic: {stat:.3f}")
print(f"P-value    : {p:.5f}")

# Interpretasi singkat
if p < 0.05:
    print("→ Terdapat perbedaan yang signifikan antara setidaknya satu kategori gender.")
else:
    print("→ Tidak terdapat perbedaan yang signifikan antara kategori gender.")

# ==== Visualisasi Boxplot ====
plt.figure(figsize=(8, 5))
sns.boxplot(data=eda_clean_gvsr, x='gender', y='swipe_right_ratio', palette='Set2')
plt.title('Distribusi Swipe Right Ratio Berdasarkan Gender')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
