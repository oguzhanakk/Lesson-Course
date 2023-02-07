import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}
)

print(df.isnull()) #eksik degerleri true seklinde gosteriyor.
print(df.isnull().sum()) #sutunlarda toplam eksik degerleri gosteriyor.
print(df.notnull().sum()) #sutunlarda toplam eksik olmayan degerleri gosteriyor.

print(df[df.isnull().any(axis = 1)]) #Fancy ile en az 1 eksik degeri olan satirlari getiriyor. ***

print(df[df.notnull().all(axis = 1)]) #hepsi dolu olan satirlar

print(df[df["V1"].notnull() & df["V2"].notnull()]) # V1, V2 sutunlarindaki eksik degeri olmayanlar

##Eksik degerleri olan satirlarin direk silinmesi
df = df.dropna() , df.dropna(inplace=True) #kalici siliyor.

##Basit deger atama
df["V1"] = df["V1"].fillna(df["V1"].mean()) #V1 deki sutunlari V1'in ortalamasi ile dolduruyor.
df["V2"] = df["V2"].fillna(0) #V2 deki eksik kisimlara 0 dolduruyor.

df.apply(lambda x: x.fillna(x.mean()), axis = 0) #tum satirlardaki eksik degerleri ortalama ile doldurma