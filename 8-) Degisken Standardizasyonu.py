import numpy as np
import pandas as pd
V1 = np.array([1,3,6,5,7])
V2 = np.array([7,7,5,8,12])
V3 = np.array([6,12,5,6,14])
df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3})

df = df.astype(float)

#Standardizasyon
from sklearn import preprocessing
a = preprocessing.scale(df)
#print(a)
#butun degerleri kendine gore bir sayilara donusturdu
#makine ogrenmesinde cok kullanilacak
#copy=True oluyor orjinal yapisini bozmaz.

#Normalizasyon
b = preprocessing.normalize(df)
#print(b)
#ayni seyi 0 ile 1 arasi haline getiriyor.

#Min-Max donusumu
c = preprocessing.MinMaxScaler(feature_range= (10,20))
d = c.fit_transform(df)
print(d)
#ayni seyi istedigin araliklarda yapiyosun.