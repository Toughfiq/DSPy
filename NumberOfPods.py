import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Soybean.csv', usecols= ['Number of Pods (NP)'])
pods = df['Number of Pods (NP)']

# Contoh analisis dasar
print(pods.describe())
# mencoba mencari Z-score
Zscore = (df['Number of Pods (NP)'] - df['Number of Pods (NP)'].mean()) / df['Number of Pods (NP)'].std()
print("Z-score =")
print(Zscore)

# Buat plot distribusi
plt.figure(figsize=(10,6))
sns.histplot(pods, kde=True, bins=30, color='crimson')

# Tambahkan elemen visual
plt.title('Distribusi Persebaran Kedelai berdasar Varietas')
plt.xlabel('Jumlah ')
plt.ylabel('Frekuensi')
plt.grid(True)

# Tampilkan plot
plt.show()