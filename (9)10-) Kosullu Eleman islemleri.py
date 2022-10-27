import numpy as np
import pandas as pd

m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])

#print(df[0:2]["var1"]) #-> bu sekilde calisir.
#print(df[0:2]["var1","var2"]) #-> bu sekilde calismaz , bunu fancy ile calistirabiliriz.
#print(df[0:2][["var1","var2"]]) #-> fancy'li hali

#print(df[df.var1 > 15]) #var1 sutunundaki ifadelerde 15'den buyuk olanlar (hepsini gosteriyor)
#print(df[df.var1 > 15]["var1"]) #var1'i gosteriyor sadece

#print(df[(df.var1 > 15) & (df.var3 < 15)]) #2 kosul olusturmak
#print(df.loc[(df.var1 > 15),["var1","var2"]]) #loc olmasa hata veriyor.
print(df[(df.var1 > 15)][["var1","var2"]]) #loc olmasa fancy ile bu sekilde yapman lazım
