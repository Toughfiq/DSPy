import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Soybean.csv', usecols= ['Number of Pods (NP)'])
pods = df['Number of Pods (NP)']

# Contoh analisis dasar
print(pods.describe())