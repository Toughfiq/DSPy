import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('DatingBehave.csv')
print(df.describe(include= 'all'))
#saat di describe banyak terjadi NaN, analisis gua sementara karena file bersifat object sehingga mean
#nya menjadi tidak bisa ditemui berdasar cara menghitung jumlah keseluruhan dibagi banyaknya data
print(df.info())