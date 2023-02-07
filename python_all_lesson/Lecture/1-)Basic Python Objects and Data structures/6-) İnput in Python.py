"""
input Fonksiyonu
"""

sayi1 = int(input("Lutfen bir sayi girin: "))
print("Girdiginiz sayi {x} dir".format(x=sayi1))

print("--------------")

Ad = input("Adinizi giriniz: ")
Soyad = input("Soyadinizi giriniz: ")
TcNo = int(input("Tc'nizi giriniz: "))

BilgilerListesi = [Ad,Soyad,TcNo]

print("Adiniz {a} dir.".format(a=BilgilerListesi[0]))

BilgilerListesi.append("Adamsin")
#Bilgiler.pop(0)
print(BilgilerListesi)

print("------------------------")

Ad = input("Adinizi giriniz: ")
Soyad = input("Soyadinizi giriniz: ")
TcNo = int(input("Tc'nizi giriniz: "))

BilgilerSozlugu = {"isim": Ad,"soyisim" : Soyad,"numara": TcNo}

print(BilgilerSozlugu.values())