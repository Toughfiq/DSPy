import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data dengan nama kolom yang benar
df = pd.read_csv('Soybean.csv', usecols=['Number of Pods (NP', 'Parameters'])

pods = df['Number of Pods (NP)']
param = df['Parameters']

# Analisis dasar
print("Deskripsi Pods:")
print(pods.describe())

print("\nKorelasi:")
print(df.corr())

# Z-score
Zscore = (pods - pods.mean()) / pods.std()
print("\nZ-score:")
print(Zscore)

# Plot histogram
plt.figure(figsize=(10,6))
sns.histplot(pods, kde=True, bins=30, color='crimson')

# Scatter plot
sns.scatterplot(x=param, y=pods)
plt.title('Scatter Plot Parameter vs Jumlah Polong')
plt.xlabel('Parameter')
plt.ylabel('Jumlah Polong')
plt.grid(True)

# Tampilkan
plt.show()