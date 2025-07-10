import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('DatingBehave.csv')
print(df.describe(include= 'all'))
#saat di describe banyak terjadi NaN,Karena NaN berarti not a number dan sesuai dengan type file saat ini
print(df.info())