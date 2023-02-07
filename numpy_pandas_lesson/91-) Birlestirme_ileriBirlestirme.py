import numpy as np
import pandas as pd
#Birlestirme isleri
m = np.random.randint(1,30, size = (5,3))
df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])
df2 = df1+99

x = pd.concat([df1,df2], ignore_index=True)
#ignore_index=True olunca 0,1,2,3,4 0,1,2,3,4 hatasi kalkiyor.
#print(x)

df2.columns = ["var1","var2","deg3"]
#pd.concat([df1, df2]) farklı sutun oldugunda concat yaparsak hatali bir birlestirme yapiyor.
y = pd.concat([df1, df2], join = "inner") #kesisimleri aliyo birbirine uyusmayan seyleri almiyor.

#z = pd.concat([df1, df2], join_axes = [df1.columns], ignore_index=True)
#df1'e gore farklı degerleri df1'den aliyor

#---------------------------------------------------------------------------
#Ileri birlestirme isleri

df3 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'], 'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'IK']})
df4 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'], 'ilk_giris': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2) #birebir birlestirme
#birlestirmeyi hangi degiskene gore yaptigini kendisi belirtiyor
pd.merge(df1, df2, on = "calisanlar") #kendin birlestirmek istersen

df3 = pd.merge(df1, df2) # çoktan çoka #coktan teke 'de birlestirme yapabilirsin.
