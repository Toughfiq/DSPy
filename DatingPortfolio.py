import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('DatingBehave.csv')
print(df.describe(include = 'number'))
print(df.info())
