import numpy as np
import pandas as pd

"""
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
V4 = np.array(["IT","IT","IK","IK","IK","IK","IK","IT","IT"])

df = pd.DataFrame(
        {"maas" : V1,
         "V2" : V2,
         "V3" : V3,
        "departman" : V4}
)

print(df)
print(df.groupby("departman")["maas"].mean())

df["maas"].fillna(df.groupby("departman")["maas"].transform("mean"))
#Departman'a gore grupladik, maas'i sectik.
#NaN degerlere departmanlardaki ortalama maasi atadik.
"""
#***************************************************

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
V4 = np.array(["IT","IT","IK","IK","IK","IK","IK","IT","IT"])

df = pd.DataFrame(
        {"maas" : V1,
         "V2" : V2,
         "V3" : V3,
        "departman" : V4}
)

df["departman"].fillna(df["departman"].mode()[0])
#Departman'da mode(en çok tekrar eden) degeri NaN degerlere atıyoruz.

df["departman"].fillna(method = "bfill")
#NaN degerleri sonraki degerin aynısı ile dolduruyor.

df["departman"].fillna(method = "ffill")
#NaN degerleri kendinden onceki degerin aynısı ile dolduruyor.