import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msno
from ycimpute.imputer import knnimput
from ycimpute.imputer import iterforest
from ycimpute.imputer import EM

df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])

"""
#KNN numpy'da calisiyor, pd'yi np'ye sonra tekrar pd'ye cevirecegiz.
#numpy'a cevirme
var_names = list(df)
n_df = np.array(df)
#print(n_df[0:10]) #numpy'da head() yerine kullanilan kisim.

dff = knnimput.KNN(k = 4).complete(n_df) #k en yakin komsu sayisi

#pandasa geri cevir
dff = pd.DataFrame(dff, columns=var_names)

print(dff.isnull().sum())
"""

"""
#Random Forest
#print(df.isnull().sum()) = age de 177 bosluk var

#pandas'i numpy'a cevirdik
var_names = list(df)
n_df = np.array(df)

dff = iterforest.IterImput().complete(n_df)
#IterImput import icinden kaldirilmis

#numpy'i geri pandas'a cevirdik
dff = pd.DataFrame(dff, columns= var_names)

print(dff.isnull().sum()) #=0
"""

#EM
#pandas'i numpy'a cevirdik
var_names = list(df)
n_df = np.array(df)

#makine ogrenmesi kismi
dff = EM().complete(n_df)

#numpy'i geri pandas'a cevirdik
dff = pd.DataFrame(dff, columns= var_names)

print(dff.isnull().sum()) # =0
