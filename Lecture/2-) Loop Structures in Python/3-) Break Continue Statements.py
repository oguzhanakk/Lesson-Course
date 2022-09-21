"""
Break ve Continue Deyimleri
"""

liste = list(range(10))

for i in liste:
    if (i % 2 == 0):
        continue
    print(i)
    

while (1):    
    isim = input("Kullanici isminizi giriniz.(cikmak icin a yaziniz.) : ")
    
    if(isim == "a"):
        break
    else:
        print("Hoşgeldin {}".format(isim))
        
