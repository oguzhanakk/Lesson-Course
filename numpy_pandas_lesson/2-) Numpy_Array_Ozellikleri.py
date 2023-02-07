#Numpy Array Ozellikleri

# ndim : boyut sayisi
# shape : boyut bilgisi
# size : toplam eleman sayisi
# dtype : array veri tipi

import numpy as np

a = np.random.randint(10, size = 10)
print(a.ndim) # 1 boyutlu
print(a.shape) # tek boyutu var 10 elemanli
print(a.size) # 10 eleman sayisi
print(a.dtype) # icindeki data tipi

print()
b = np.random.randint(10, size = (3,5))
print(b.ndim) # 2 boyutlu
print(b.shape) # 1 boyutta 3 , 2. boyutta 5 eleman var
print(b.size) # 15 eleman sayisi
print(b.dtype) # icindeki data tipi