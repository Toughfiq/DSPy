import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_connection import load_column, load_columns
from utils.cleaning import *
from scipy.stats import chi2_contingency
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
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Lakukan uji chi-square
chi2, p, dof, expected = chi2_contingency(cross_tab)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}") 
'''
Hasil value chi square nya adalah 0.7 -> ini berarti 
tidak ada hubungan signifikan 
antara gender dan sexual orientation nya atau 
dengan kata lain independen satu sama lain.
'''

######### Coba kelompokkan gender untuk melihat apakah ada perilaku dari berbagai kelompok #########
def group_gender(value):
    if value in ['Male', 'Female']:
        return 'Binary'
    elif value in ['Non-binary', 'Genderfluid']:
        return 'Non-Binary/Fluid'
    else:
        return 'Other/Unspecified'
eda_corr_df['gender_group'] = eda_corr_df['gender'].apply(group_gender)
#Buat cross tab untuk korelasi baru
cross_tab = pd.crosstab(eda_corr_df['gender_group'], eda_corr_df['sexual_orientation'])

# Visualisasi
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='BuPu')
plt.title("Grouped Gender vs Sexual Orientation")
plt.xticks(rotation=15)
plt.show()

# Chi-square test
chi2, p, dof, expected = chi2_contingency(cross_tab)
print(f"Chi-square: {chi2:.2f}, p-value: {p:.4f}")
'''
Berdasarkan uji chi-square antara gender (baik dalam bentuk asli maupun setelah dikelompokkan) 
dan sexual orientation, diperoleh p-value yang jauh di atas 0.05. Hal ini menunjukkan 
tidak terdapat hubungan statistik yang signifikan antara gender dan orientasi seksual 
dalam dataset ini.Hal ini juga dapat menunjukkan bahwa 
orientasi seksual dalam data ini terdistribusi cukup merata lintas kelompok gender."
'''
# ==== Gender vs Income Bracket ====
eda_income = load_columns(['gender', 'income_bracket']) #gunakan list untuk load beberapa collumns
eda_income['gender'] = eda_income['gender'].apply(clean_gender)
eda_income['income_bracket'] = eda_income['income_bracket'].apply(clean_Income)
cross_tab = pd.crosstab(eda_income['gender'], eda_income['income_bracket'])
print(cross_tab)
plt.figure(figsize=(10, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Gender vs Income Bracket")
plt.xlabel("Income Bracket")
plt.ylabel("Gender")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Lakukan uji chi-square
chi2, p, dof, expected = chi2_contingency(cross_tab)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")