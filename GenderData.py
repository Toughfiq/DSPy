import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
Gender = pd.read_csv('DatingBehave.csv', usecols=['gender'])

# 2.pembersihan data 
def GenderType(value):
    if pd.isna(value):  #Menyaring value kosong
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

Gender['gender'] = Gender['gender'].apply(GenderType)

# 3.perhitungan data
gender_counts = Gender['gender'].value_counts()
gender_percent = Gender['gender'].value_counts(normalize=True) * 100

print("Unique values:", Gender['gender'].unique())
print("\nCounts:\n", gender_counts)
print("\nPercentages:\n", gender_percent.round(2))

# 4. Plot histogram
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=Gender, x='gender', order=gender_counts.index, palette='viridis')

# Add counts on top of bars
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 5), 
                textcoords='offset points')

plt.title('Distribution of Gender Categories', fontsize=15)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Plot pie chart for percentages (alternative visualization)
plt.figure(figsize=(8, 8))
gender_percent.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution (%)', fontsize=15)
plt.ylabel('')  # Hide y-label
plt.tight_layout()
plt.show()