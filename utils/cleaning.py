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