import mysql.connector
import pandas as pd
# ========================================
# Cleaning Orientation
# ========================================
def clean_orientation(value):
    if pd.isna(value):
        return 'Unknown'
    value = str(value).strip().lower()
    if value in ['straight', 'heterosexual']:
        return 'Straight'
    elif value in ['gay', 'homosexual']:
        return 'Gay'
    elif value in ['bisexual']:
        return 'Bisexual'
    elif value in ['asexual']:
        return 'Asexual'
    elif value in ['pansexual']:
        return 'Pansexual'
    elif value in ['queer']:
        return 'Queer'
    elif value in ['lesbian']:
        return 'Lesbian'
    elif value in ['demisexual']:
        return 'Demisexual'
    else:
        return value.title()
# ========================================
# Cleaning gender
# ========================================  
def clean_gender (value):
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