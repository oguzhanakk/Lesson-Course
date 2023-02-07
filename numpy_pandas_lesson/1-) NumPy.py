# NumPy -> Numerical Python'in kisaltilmisi
# Olusturma ve bicimlendirme , Eleman islemleri , kosullu eleman islemleri , hesaplamalı islemleri yapıcaz.
# Pandas'a gecicez -> veri analizi.
# 2 madde aynisi... ve ileri hesaplamali islemler.

import numpy as np
"""
ab = []
for i in range(0, len(a)):
    ab.append(a[i]*b[i])

print(ab)
"""
#Bunun numpy ile yapilan hali
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a*b)
# ==
print(type(a))
print(np.array([3.14, 4, 2, 13])) #icerde tek tip veri tutabiliyosun böyle yaparsan , ilk veri ne ise digerleri o oluyor.
print(np.array([3.14, 4, 2, 13], dtype = "int")) #Sona yazdigin seye gore veri tipleri belirleniyor.

#Sifirdan array olusturma
print(np.zeros(10, dtype = int))
print(np.ones((3,5), dtype = int))

print(np.full((2,4), 3))

print("-----------------")
print(np.arange(0,31, 3))

print(np.linspace(0,1,10)) #0-1 arasini 10'a boluyor.

print("-------------------")
print(np.random.normal(10, 4, (3,4))) #3,4 luk matris ortalamasi = 10 standart sapması = 4
print(np.random.randint(0,10, (3,2)))