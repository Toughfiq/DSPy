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

#=================================Analisis 1 gender vs Swipe Right=============
eda_gender_behavior = load_columns(['gender', 'swipe_right_ratio','likes_received','app_usage_time_min']) #gunakan list untuk load beberapa collumns
# ==== Bersihkan Data ====
# Pastikan tidak ada nilai kosong
eda_clean_gvsr = eda_gender_behavior.dropna(subset=['gender', 'swipe_right_ratio'])

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
#-=============================Analisis Gender vs Likes recieved =========================
# ==== Bersihkan Data ====
# Pastikan tidak ada nilai kosong
eda_clean_gvlr = eda_gender_behavior.dropna(subset=['gender', 'likes_received'])

# Pastikan kolom numerik dalam format float
eda_clean_gvlr['likes_received'] = pd.to_numeric(eda_clean_gvlr['likes_received'], errors='coerce')
eda_clean_gvlr = eda_clean_gvlr.dropna(subset=['likes_received'])

# ==== Tampilkan Rata-rata per Gender ====
print("\n=== Rata-rata likes recieve per Gender ===")
mean_likes = eda_clean_gvlr.groupby('gender')['likes_received'].mean().sort_values(ascending=False)
print(mean_likes)

#================= Test histogram setiap gender vs likes recieved nya===============
genders = eda_clean_gvlr['gender'].unique()

for gender in genders:
    subset = eda_clean_gvlr[eda_clean_gvlr['gender'] == gender]
    
    plt.figure(figsize=(6, 4))
    plt.hist(subset['likes_received'], bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Distribusi Likes Received untuk Gender: {gender}')
    plt.xlabel('Likes Received')
    plt.ylabel('Frekuensi')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
'''
hasil yang dihasilkan oleh histogram menunjukkan beberapa multimodal dalam distribusinya walau
tidak terlalu signifikan, kedepannya mungkin bisa dilihat korelasinya dengan app usage minutes
apakah terjadi korelasi diantara itu.
'''
# ====== Scatter plot multivariat dengan waktu numerik ======
eda_clean_multi = eda_gender_behavior.dropna(
    subset=['gender', 'likes_received', 'app_usage_time_min']
).copy()

# Konversi likes_received dan waktu ke numeric
eda_clean_multi['likes_received'] = pd.to_numeric(
    eda_clean_multi['likes_received'], errors='coerce'
)
eda_clean_multi['app_usage_time_min'] = pd.to_numeric(
    eda_clean_multi['app_usage_time_min'], errors='coerce'
)

# Drop NaN sisa
eda_clean_multi = eda_clean_multi.dropna(subset=['likes_received', 'app_usage_time_min'])

# Scatter plot per gender
genders = eda_clean_multi['gender'].unique()

for gender in eda_clean_multi['gender'].unique():
    subset = eda_clean_multi[eda_clean_multi['gender'] == gender]
    
    plt.figure(figsize=(8, 6))
    sns.kdeplot(
        data=subset,
        x='app_usage_time_min',
        y='likes_received',
        fill=True,
        cmap='Blues',
        levels=30,  # semakin besar = semakin detail
        thresh=0.05 # filter kepadatan sangat kecil
    )
    plt.xlabel('App Usage Time (minutes)')
    plt.ylabel('Likes Received')
    plt.title(f'Density Plot: {gender}')
    plt.tight_layout()
    plt.show()

#================= trend line =============
# Scatter plot + Trend line per gender
genders = eda_clean_multi['gender'].unique()

for gender in genders:
    subset = eda_clean_multi[eda_clean_multi['gender'] == gender]
    
    plt.figure(figsize=(6, 4))
    
    # Scatter plot
    sns.scatterplot(
        data=subset,
        x='app_usage_time_min',
        y='likes_received',
        color='skyblue',
        alpha=0.5
    )
    
    # Trend line (regresi linear)
    sns.regplot(
        data=subset,
        x='app_usage_time_min',
        y='likes_received',
        scatter=False,
        color='red',
        line_kws={'linewidth': 2}
    )
    
    plt.title(f'Likes Received vs App Usage Time (menit) - {gender}')
    plt.xlabel('App Usage Time (menit)')
    plt.ylabel('Likes Received')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
