import pandas as pd

df = pd.read_csv('mbarek.csv', sep=';')
print(df['titel'].str.split(expand=True).stack().value_counts())
