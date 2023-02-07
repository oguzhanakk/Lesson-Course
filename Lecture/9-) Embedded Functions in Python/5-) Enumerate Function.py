# Enumerate Fonksiyonu -> Asagidaki ornegi otomatik yapmaya yariyor.

# listedeki veriler ile index sayılarını 2'li gruplandıran bir liste yapmak istiyoruz.
liste = ["Elma", "Armut", "Muz", "Kiraz"]

i = 0
sonuc = list()

while (i < len(liste)):
    sonuc.append((i,liste[i]))
    i += 1

print(sonuc)

#-------------------------------------------------------------------

print(list(enumerate(liste)))

#-------------------------------------------------------------------

for i,j in enumerate(liste):
    print(i,j)
    
#------------------------------------------------------------------

liste = ["a","b","c","d","e","f","g"]

#indexi çift olanlari bastiracagiz.
for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)