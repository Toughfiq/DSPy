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

# 4. Plot bar chart dari data yang sudah dihitung diatas
plt.figure(figsize=(10, 6)) # membuat canvas kosong untuk plot dengan ukuran 10x6 inch
#menambahkan bar chart
ax = sns.countplot(data=gender_df, x='gender', order=gender_counts.index, palette='pastel') #countplot akan menghitung setiap kategori count
#x = 'gender' menunjukkan kolom yang dijadikan sumbu x
#order= gender_counts.index akan mengurutkan jumlah terbanyak berada paling kiri

# Menambah label angka total counts diatas tiap bar
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 5), 
                textcoords='offset points')

plt.title('Distribution of Gender Categories', fontsize=15) #judul grafik
plt.xlabel('Gender', fontsize=12) #judul sumbu x
plt.ylabel('Count', fontsize=12)#judul sumbu y
plt.xticks(rotation=45) #memiringkan label sumbu x aagr terbaca dan tidak bertumpuk
plt.tight_layout() # digunakan untuk menyesuaikan padding agar tidak terpotong
plt.show() #menampilkan hasil plot

#membuat perbandingan gender binary(male and female) dan juga  non-binary
def group_gender(value):
    if value in ['Male', 'Female']:
        return 'Binary'
    elif value in ['Non-binary', 'Genderfluid']:
        return 'Non-Binary/Fluid'
    else:
        return 'Other/Unspecified'
gender_df['gender_group'] = gender_df['gender'].apply(group_gender)

#Hitung frekuensi tiap kelompok
group_counts = gender_df['gender_group'].value_counts()
group_percent = gender_df['gender_group'].value_counts(normalize=True) * 100

#Buat pie chart untuk visualisasi perbandingan
plt.figure(figsize=(8, 8))
colors = ['#8ecae6', '#ffb703', '#adb5bd']  # Warna bisa kamu ganti sesuai selera

plt.pie(group_counts, 
        labels=group_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors,
        wedgeprops={'edgecolor': 'white'})

plt.title('Gender Group Distribution', fontsize=14)
plt.axis('equal')  # memastikan lingkaran utuh
plt.show()
