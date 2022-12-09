import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

diamonds = sns.load_dataset('diamonds')
diamonds = diamonds.select_dtypes(include = ['float64', 'int64'])
df = diamonds.copy()
df = df.dropna()

clf = LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)
clf.fit_predict(df)
df_scores = clf.negative_outlier_factor_

#np.sort(df_scores)[0:20]
esik_deger = np.sort(df_scores)[13]

aykiri_tf = df_scores > esik_deger
#print(aykiri_tf)

##SILME YONTEMI
yeni_df = df[df_scores > esik_deger] #aykiri olmayanlarin bulundugu df
aykiri_df = df[df_scores < esik_deger] #aykiri olanlar df

##BASKILAMA YONTEMI
baski_deger = df[df_scores == esik_deger]
aykirilar = df[~aykiri_tf]

res = aykirilar.to_records(index = False)
res[:] = baski_deger.to_records(index = False)

df[~aykiri_tf] = pd.DataFrame(res, index = df[~aykiri_tf].index)
print(df[~aykiri_tf])

