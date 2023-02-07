#Fonksiyonlar

"""a = [1,2,3,4]

help(a.append)"""

def selamla():
    print("selam")
    
selamla()


def faktoriyelHesaplayici(sayi):
    faktoriyel = 1
    
    if(sayi==0 or sayi==1):
        print(faktoriyel)
    
    else:
        while(sayi>=1):
            faktoriyel *= sayi
            sayi -= 1
        
        print(faktoriyel)
        
faktoriyelHesaplayici(10)


def KullaniciFonksiyonu (isim,soyisim):
    
    if(isim == "Oğuzhan" and soyisim == "Akkoyunlu"):
        print("Doğru kisi giris yaptı.")
 
kullaniciAdi = input(str("kullanici adinizi giriniz: "))
kullaniciSoyadi = input(str("kullanici soyadinizi giriniz: "))
KullaniciFonksiyonu(kullaniciAdi,kullaniciSoyadi)
