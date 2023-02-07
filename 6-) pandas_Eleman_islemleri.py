import numpy as np
import pandas as pd

a = np.array([1,2,3,42,53])
seri = pd.Series(a)

seri = pd.Series([121,200,150,33],
                 index = ["reg","loj","cart","rf"])

print(seri.index)
print(seri.keys)
print(list(seri.items()))
print(seri.values)
print("reg" in seri)

#fancy eleman
print(seri[["rf", "reg"]])
seri["reg"] = 130
print(seri[["reg"]])
print(seri["reg":"loj"])