# Zip fonksiyonu -> asagida manuel yaptigim seyi otomatik olarak yapıyor.

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
# ben bu listeleri 1-6 2-7 3-8 4-9 seklinde demet olarak listelemek istiyorum. Bunu manuel nasıl yaparız.

i = 0
sonuc = list()
while (i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i += 1
print(sonuc)

#--------------------------------------------

liste3 = [10,15,20,25,30]
liste4 = [7,14,21,28,35]

print(list(zip(liste3,liste4)))

#--------------------------------------------

liste5 = [10,15,20,25,30]
liste6 = [7,14,21,28,35]
liste7 = ["Python", "Php" , "Java"]

print(list(zip(liste5,liste6,liste7)))

#-------------------------------------------

for i,j in zip(liste6,liste7):
    print(i,j)
    
#------------------------------------------

sozluk1 = {"Elma" :1 , "Armut":2, "Kiraz":3}
sozluk2 = {"Sifir":0 , "Bir":1, "iki":2}

print(list(zip(sozluk1,sozluk2)))
print(list(zip(sozluk1.values(),sozluk2.values())))