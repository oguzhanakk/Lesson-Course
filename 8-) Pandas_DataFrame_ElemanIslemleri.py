import numpy as np
import pandas as pd

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

sozluk = {"var1": s1, "var2": s2, "var3": s3}

df = pd.DataFrame(sozluk)
#print(df)
#print(df[0:1])

df.index = ["a","b","c","d","e"]
#print(df["c":"e"])

#silme
#print(df.drop("a", axis = 0)) #df'i komple degistirmedi.
df.drop("a", axis = 0, inplace = True) #inplace kalici olarak siliyor.

#topluca silmek icin fancy kullaniyoruz.
l = ["c","e"]
#df.drop(l, axis = 0, inplace = True)
#print(df)

#degiskenler icin...
l = ["var1","var4","var2"]
for i in l:
    print(i in df)

df["var4"] = df["var1"] / df["var2"] #var4 olmadigi icin onu göremiyor ve onu olusturuyor.

#degisken silmek
df.drop("var4", axis = 1, inplace = True)
print(df)