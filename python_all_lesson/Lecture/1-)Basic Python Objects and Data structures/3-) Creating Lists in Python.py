"""
Phytonda liste olusturma
"""

liste1 = ["Elma",35,"selam",3.14,5]
print(liste1)

liste2 = [6]
print(liste2)

print(len(liste1))

print(liste1+liste2)

#Liste1'in ilk iki elemanını degistirmek
liste1[:2] = [10,11]

print(liste1)

liste3 = [10,11,12,"alex"]

#append = listenin sonuna ekleme
liste3.append("Python")
print(liste3)

#pop = listeden atma sayıyı yazarsan o indeks yazmazsan son indeksi
liste3.pop(0)
print(liste3)

#sort = sıralama (harf sırası veya küçükten büyüge)
liste4 = [10,15,8,9,19,5]
liste4.sort()
print(liste4)
print(liste4.count(10))

#iç içe listeler
İçiçeListe = [[3,4],[5,7],[8,9]]
print(İçiçeListe[1][0])
