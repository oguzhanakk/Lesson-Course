import numpy as np
import pandas as pd

#Loc & iloc --> konularina deginecegiz.

m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])

#print(df)

# loc : tanimlandigi sekli ile secim yapmak icin kullanilir.
#print(df.loc[0:3]) # -> 0 1 2 3 u aldi. (dahil ediyo)

# iloc : alisik oldugumuz indeksleme mantigi ile secim yapar.
#print(df.iloc[0:3]) # -> 0 1 2 yi aldi. (dahil etmiyo)

print(df.loc[0:3, "var3"])

print(df.iloc[0:3, "var3"]) #hata veriyor.
