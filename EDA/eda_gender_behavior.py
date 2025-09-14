import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
import sys, os

# Tambahkan path ke utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_columns
from utils.cleaning import clean_numeric

# ===== Config Database (kalau ingin ambil via SQL) =====
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}

# ===== Load data =====
eda_gender_behavior = load_columns([
    'gender', 'swipe_right_ratio', 'likes_received', 'app_usage_time_min'
])

# =============================================================================
# 1. Analisis Gender vs Swipe Right Ratio
# =============================================================================
def analyze_swipe_ratio(df):
    df = df.dropna(subset=['gender'])
    df = clean_numeric(df, 'swipe_right_ratio')

    print("\n=== Rata-rata Swipe Right Ratio per Gender ===")
    mean_table = df.groupby('gender')['swipe_right_ratio'].mean().sort_values(ascending=False)
    print(mean_table)
 
    # Uji ANOVA
    groups = [group['swipe_right_ratio'] for _, group in df.groupby('gender')]
    stat, p = f_oneway(*groups)
    print("\n=== Hasil Uji ANOVA ===")
    print(f"F-statistic: {stat:.3f}")
    print(f"P-value    : {p:.5f}")
    print("→ Terdapat perbedaan signifikan." if p < 0.05 else "→ Tidak terdapat perbedaan signifikan,antar gender")

    # Visualisasi boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='gender', y='swipe_right_ratio', hue='gender', palette='Set2', legend=False)
    plt.title('Distribusi Swipe Right Ratio Berdasarkan Gender')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()

# =============================================================================
# 2. Analisis Gender vs Likes Received
# =============================================================================
def analyze_likes_received(df):
    df = df.dropna(subset=['gender'])
    df = clean_numeric(df, 'likes_received')

    print("\n=== Rata-rata Likes Received per Gender ===")
    mean_likes = df.groupby('gender')['likes_received'].mean().sort_values(ascending=False)
    print(mean_likes)

    # Histogram per gender (menggunakan sampling)
    genders = df['gender'].unique()
    for gender in genders:
        subset = df[df['gender'] == gender].sample(n=min(5000, len(df)), random_state=42)
        plt.figure(figsize=(6, 4))
        plt.hist(subset['likes_received'], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Distribusi Likes Received - {gender}')
        plt.xlabel('Likes Received')
        plt.ylabel('Frekuensi')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# =============================================================================
# 3. Analisis Multivariat (Binning Time vs Likes)
# =============================================================================
def analyze_usage_vs_likes(df):
    df = df.dropna(subset=['gender'])
    df = clean_numeric(df, 'likes_received')
    df = clean_numeric(df, 'app_usage_time_min')

    # Binning waktu penggunaan
    df['usage_bin'] = pd.cut(
        df['app_usage_time_min'],
        bins=[0, 30, 60, 90, 120, 150, 200, 300, 600],
        labels=['0-30','30-60','60-90','90-120','120-150','150-200','200-300','300-600']
    )

    mean_likes = df.groupby(['gender', 'usage_bin'])['likes_received'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=mean_likes, x='usage_bin', y='likes_received', hue='gender', marker='o')
    plt.title('Rata-rata Likes Received per Gender vs Waktu Penggunaan')
    plt.xlabel('Waktu Penggunaan (menit, binned)')
    plt.ylabel('Rata-rata Likes Received')
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# =============================================================================
# Main Execution
# =============================================================================
if __name__ == "__main__":
    analyze_swipe_ratio(eda_gender_behavior)
    analyze_likes_received(eda_gender_behavior)
    analyze_usage_vs_likes(eda_gender_behavior)
