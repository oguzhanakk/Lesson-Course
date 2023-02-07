import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64'])
df = df.dropna()

df_table = df["table"]
#print(df_table.head())

Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3-Q1

alt_sinir = Q1 - 1.5*IQR
ust_sinir = Q3 + 1.5*IQR

#print((df_table < alt_sinir) | (df_table > ust_sinir)) #True donenler aykiri deger olanlar

aykiri_tf = (df_table < alt_sinir) | (df_table > ust_sinir)

#print(df_table[aykiri_tf]) #Fancy ile aykiri degerleri basmak
#print(df_table[aykiri_tf].index.tolist()) #sadece indexlerin liste hali

##Silme kismi
df_table = pd.DataFrame(df_table)
#print(df_table.shape)

temiz_df = df_table[~((df_table < alt_sinir) | (df_table > ust_sinir)).any(axis = 1)]
#print(df_table.shape)
#print(temiz_df.shape)

##Ortalama ile doldurma
df_table[aykiri_tf] = df_table.mean()
#print(df_table[aykiri_tf])

##Baskilama Yontemi
#ust taraftaysa = ust sinir degerine esitlenir
#alt taraftaysa = alt sinir degerine esitlenir
#cok fazla aykiri ise ortalamaya esitlemek mantikli olmayabilir.
aykiri_tf_alt = (df_table < alt_sinir)
aykiri_tf_ust = (df_table > ust_sinir)

df_table[aykiri_tf_alt] = alt_sinir
df_table[aykiri_tf_ust] = ust_sinir

