import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}
)

#Kategorik Degisken Kiriliminda Deger Atama





"""
##Sayısal degiskenlerde atama
df["V1"].fillna(df["V1"].mean()) #V1 sutunundaki NaN'lari V1 ortalamasi ile dolduruyor.
##Tum degiskenler icin birinci yol
df.apply(lambda x: x.fillna(x.mean()), axis = 0) #axis=1 satir bazli ortalama ile dolduruyo tum NaN'lari , axis=0 sutun bazli
#kalici olması icin df = df.apply()

##Ikinci yol
df.fillna(df.mean()[:]) #ilk yolun aynisi sutun bazli
#Asama-asama doldurma
df.fillna(df.mean()["V1":"V2"]) #V1 den V2'ye kadar kismi ortalama ile doldurdu.
df["V3"].fillna(df["V3"].median())  #V3'u V3'un medyani ile doldurdu
##Ucuncu yol
df.where(pd.notna(df), df.mean(), axis = "columns")
"""

"""
df.dropna() #1 tane eksik deger varsa satiri siliyor.
df.dropna(how = "all") #satirdaki hepsi eksikse siliyor.
df.dropna(axis = 1) #sutun bazli eksik veri varsa sutunu siliyor.
df.dropna(axis = 1, how = all) #sutunda bazli silme axis = 1 , sutunda hepsi NaN ise o sutunu siliyor
df.dropna(inplace=True) #eklersen sonuna kalici olarak yapar bu islemleri
"""