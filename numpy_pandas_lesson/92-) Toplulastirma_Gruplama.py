#Toplulastirma ozellikleri
import seaborn as sns

df = sns.load_dataset("planets")
#print(df.head())
#print(df.shape)

#print(df.mean())
"""
print("mean : {}".format(df["mass"].mean()))
print("count : {}".format(df["mass"].count()))
print("min : {}".format(df["mass"].min()))
print("max : {}".format(df["mass"].max()))
print("sum : {}".format(df["mass"].sum()))
print("standart sapma : {}".format(df["mass"].std()))
print("variance : {}".format(df["mass"].var()))
"""

#print(df.describe().T) #Butun ozellikleri tek tek uyguluyor. .T tersten yapiyor.

#-------------------------------------------------------------
#Gruplama Islemleri
import numpy as np
import pandas as pd

df2 = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])

x = df2.groupby("gruplar")
print(x)
print(x.mean())
print(x.sum())
