import numpy as np

#Index ile Elemanlara Erismek
a = np.random.randint(10, size = (3,5))
print(a)

#satir , sutun
#a[1,0] = 21
print(a[1,0])

a[2,0] = 2.2 #yaparsan ici int oldugu icin 2 olarak yapar direk
print(a[2,0])

#--------------------------------------------------------
#Slicing ile (alt kumelere erisme)
b = np.arange(24,38)
    #0. indexten 8.indexe kadar 2'ser artarak
print(b[0:8:2])

#2 boyutlu slice islemleri
m = np.random.randint(10, size = (5,5))
print(m,"\n")
print(m[:,0]) #0. sutunu basiyor.

print(m[0,:]) #= print(m[0]) #0. satiri basiyor.

print(m[0:2, 0:3]) #0-2'ye kadar satiri al , 0-3'e kadar sutunu al

print(m[:,0:2]) #tum satirlari al 0-2'e kadar sutunları al

#------------------------------------------------------------------
#Alt kume uzerinde islem yapmak

n = np.random.randint(10, size = (5,5))

#ana veri ustunde aldigimiz alt veriyi degistirirken ana veri degismesin
#istiyorsak yapmamiz gerekiyor.
alt_n = n[0:3, 0:2].copy() #ana array'e dokunmuyor.
alt_n[0,0] = 9999 #ana array'deki [0,0] degismedi

#--------------------------------------------------------------------
#Fancy Index ile Elemanlara Erismek
#Fancy = Fantastik,buyuleyici (cok onemli bir konu)****

v = np.arange(0, 30, 3)

al_getir = [1,3,5] #array icinden istedigimiz degerleri array tanimlayip
#icine yazarak bulabilmemize fancy methodu deniyor. Ozel bir islemi yok. Taktik sadece
print(v[al_getir])

#2 boyutta fancy

t = np.arange(9).reshape((3,3))

satir = np.array([0,1])
sutun = np.array([1,2])

print(t[satir,sutun])

#Basit index ile fancy index

t[0, [1,2]] #klasik index
t[0:, [1,2]] #0: slice , sonu fancy

#-------------------------------------------------------------------------
#Kosullu Eleman İslemleri

v = np.array([1, 2, 3, 4, 5])
print(v[v < 3]) #fency -> v vektoru icine git v<3 olanlari getir.
print(v * 2, v / 2)

#-----------------------------------------------------------------------
#Matematiksel islemler

v = np.array([1, 2, 3, 4, 5,])
#           ufunc
# v-1 = np.subtract(v, 1)
# v**3 = np.power(v, 3)
# v % 2 = np.mod(v, 2)
# |v| = np.absolute(np.array([-3]))
# help(np)
# cheatsheet (ör) -> numpy mathematics cheat sheet *****
# numpy statistics cheat sheet

np.mean(v) #ortalama
v.sum() , v.min() , v.max()

#------------------------------------------------------------------------

#Numpy ile Iki bilinmeyenli denklem cozumu

# 5x0+x1 = 12 , x0+3x1= 10
a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

x = np.linalg.solve(a, b)
print(x)