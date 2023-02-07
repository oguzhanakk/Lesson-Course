#Pandas
#-> Numpy'in gelismisi Python data analysis (Panel data)
import pandas as pd
#-> Numpy'dan farkı index degerleri icindeki degerlerle birlikte tutulur.
#-> index - seri degerleri seklinde tutuluyor.
seri = pd.Series([10,88,3,4,5])
#print(seri)
"""
print(type(seri))
print(seri.axes) #index bilgileri (kactan baslamis kaca kadar)
print(seri.dtype)
print(seri.size) #terim sayisi
print(seri.ndim) #boyutu
print(seri.values) #-> sadece degerleri almak icin.
print(seri.head(3)) #-> kac tane veri istersen onu yazip onu cekiyosun
print(seri.tail(3)) #-> tersten kac tane veriyi cekmek istiyosan
"""

seri2 = pd.Series([99,22,323,33,5], index = [1,3,5,7,9])
seri3 = pd.Series([99,22,313,44,6], index = ["a","b","c","d","e"])

#print(seri3["a":"c"])

#Sozluk uzerinden liste olusturmak.
sozluk = {"reg":10, "log":11, "cart":12}
seri = pd.Series(sozluk)
#print(sozluk)

#iki seriyi birlestirerek seri olusturma
pd.concat([seri,seri])