import seaborn as sns
import numpy as np
import pandas as pd
df = sns.load_dataset('tips')

"""
#0-1 donusumu
#Genelde erkek-kadin halinde kullaniliyor
#Yani 2 secenek varsa
from sklearn.preprocessing import LabelEncoder
lbe = LabelEncoder()

df["yeni_sex"] = lbe.fit_transform(df["sex"])
#dataframe'e yeni sutun olarak ekledik, eskisi kalsin
print(df)
"""

"""
#1 ve digerleri(0) donusumu
#birden fazla secenek varsa sen sadece 1 ile ilgileniyosan
df["yeni_day"] = np.where(df["day"].str.contains("Sun"), 1, 0)
print(df)
"""

"""
#Cok sinifli donusum
#birden fazla degiskeni sayilara donusturmek
from sklearn.preprocessing import LabelEncoder
lbe = LabelEncoder

a = lbe.fit_transform(df["day"],df["day"])
print(a)
#yanlis cikarimlar olusturabilir stringi sayisal degere cevirmek
#bunu duzeltmek icin "One-Hot" Donusumu yapicaz.
""" 

#One-Hot donusumu
#kac degisken varsa hepsi icin bir sutun olusturuyor.
#o sutunlarda dogruysa 1 yanlissa 0 haline getiriyor.
df_one_hot_sex = pd.get_dummies(df, columns=["sex"], prefix = ["sex"])
#print(df_one_hot_sex.head())
#Dummy Degisken tuzagi = cinsiyeti ele alinca ikiside ayni sorun cikartabiliyor.
df_one_hot_day = pd.get_dummies(df, columns=["day"], prefix = ["day"])
print(df_one_hot_day.columns)
#one-hot yeni degisken olarak ekledigi icin, degiskenlerin agirligini
#gorebilme hakki veriyor.
