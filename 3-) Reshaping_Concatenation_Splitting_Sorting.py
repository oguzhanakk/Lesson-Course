import numpy as np

#Reshaping (sekillendirme)
# elimizdeki array'den baska bir array olusturmak.
# tek boyuttan 2 boyuta , 2 boyuttan tek boyuta gecisler icin.
a = np.arange(1,10) #vektor

np.arange(1,10).reshape(3,3)

b = a.reshape(1,9) #vektoru matris yaptik. (2 boyut)

#------------------------------------------------------------------
#Concatenation (birlestirme)

x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])

np.concatenate([x,y,z])

#iki boyutta
a1 = np.array([[1,2,3],
               [4,5,6]])

np.concatenate([a1,a1])

np.concatenate([a1,a1], axis = 1) #sutun bazinda birlestirir (axis = 1)(yan)
#satir bazinda birlestirir (axis = 0)(alt)

#--------------------------------------------------------------------
#Splitting (ayirma)

q = np.array([1,2,3,99,99,3,2,1])

a,b,c = np.split(q, [3,5])

#iki boyutlu ayirma

m = np.arange(16).reshape(4,4)
#print(m,"\n")

ust, alt = np.vsplit(m, [2])
#print(ust,"\n")
sag, sol = np.hsplit(m, [2])
#print(sag)

#-------------------------------------------------------------------
#Sorting (siralama)

v = np.array([2,1,4,3,5])

#print(np.sort(v)) #bunu direk bastiginda siralamis oluyo orjinalini degistirmiyo
v.sort() #bu orjinalini degistirmis oluyor.
#print(v)

#iki boyutlu siralama
                #ort,standart sapma
k = np.random.normal(20,5, (3,3))

#print(np.sort(k, axis = 1)) #satira gore siraliyor.
#print(np.sort(k, axis = 0)) #sutuna gore siraliyor.
