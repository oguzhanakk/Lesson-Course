"""
Fonksiyonlarda parametre Türleri
"""

def selamla(isim):
    print("Selam",isim)
    
selamla("Ahmet") # Parametre budur.


# illa bilgi olusturmak zorunda degilsin istersen koyup istersen koymayadabilirsin
print("---------------------------")

def selamla(isim = "isimsiz"):
    print("Selam",isim)
    
selamla() #deger koymadık
selamla("Murat") #deger koyduk

print("---------------------------")
def bilgiler (ad="Bİlgi yok",soyad = "Bilgi yok", numara = "Bilgi yok"):
    print(ad,soyad,numara)
    
bilgiler("Ali","Cem")

#Sadece numara vermek istersen özel olarak belirtmen lazım cünkü sonda
bilgiler(numara="1234")

print("---------------------------")
#Esnek sayida deger vermek istersen kac deger giricegin belli degilse

def toplama(*a):
    print(a)
    
toplama(1,2,3)
toplama(1,2,3,6,8,9)
#Printin helpinde de böyle yaziyor istedigin degeri verebilirsin

def toplama2(*a):
    toplamm = 0
    for i in a:
        toplamm += i
    print(toplamm)
    
toplama2(2,4,6,7)
toplama2(2,34,12,7)