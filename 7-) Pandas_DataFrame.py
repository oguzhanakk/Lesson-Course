import pandas as pd
import numpy as np

l = [1,2,39,67,90]

pd.DataFrame(l, columns = ["degisken_ismi"])

m = np.arange(1,10).reshape((3,3))
a = pd.DataFrame(m, columns = ["var1","var2","var3"])
#print(m,"\n")
#print(a)

#df isimlendirme

df = pd.DataFrame(m, columns = ["var1","var2","var3"])
#print(df.head)
df.columns = ("deg1","deg2","deg3")
print(df)
print(df.axes, df.shape, df.ndim, df.size, df.values)
print(df.head(2), df.tail(2))

x = np.array([1,2,3,4,5])
y = pd.DataFrame(x, columns = ["deg1"])
print(y)