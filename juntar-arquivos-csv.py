import pandas as pd
a = pd.read_csv('a.csv',sep=';', encoding='cp1252')
b = pd.read_csv('b.csv',sep=';', encoding='cp1252')
base = pd.concat([a,b], axis=1, sort=False)
#base.to_csv("base.csv", index=False)
base.to_excel("base.xlsx", index=False)