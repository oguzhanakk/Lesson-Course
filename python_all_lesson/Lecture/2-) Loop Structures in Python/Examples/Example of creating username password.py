"""
Kullanici Giriş Fonksiyonu
"""

print("""Merhabalar Hoşgeldiniz

      1. Üye olmak icin
      
      2. Hesaba giris yapmak icin
      
      3. Siteden Çikmak için
      
      5.Kullanıcı adı şifrelere bakma(gizli)
      """)

HesapsızGirilmez = 0
Olusturulan_hesap_sayisi = 0

kullaniciListesi = list()
SifreListesi = list()

while(True):    
    islem = input("Ne islem yapacaginizi seciniz: ")
    
    if (islem == "1"):
        Kullanici_adi = input("Kullanici adini giriniz: ")
        Sifre = input("Sifrenizi giriniz: ")
        
        kullaniciListesi.append(Kullanici_adi)
        SifreListesi.append(Sifre)
        
        Olusturulan_hesap_sayisi += 1
        HesapsızGirilmez = 1
    
    elif (islem == "5"):
        print(kullaniciListesi,SifreListesi)
    
    elif (islem == "2" and HesapsızGirilmez == 1):
        DogruGiristeCikma=0
        while(DogruGiristeCikma<10):
            kullanici_kontrol = input("kullanici adinizi tekrar giriniz: ")
            sifre_kontrol = input("Sifrenizi tekrar giriniz: ")
        
            for i in range(0,Olusturulan_hesap_sayisi):        
                if(kullaniciListesi[i] == kullanici_kontrol and SifreListesi[i] == sifre_kontrol):
                    print("Tebrikler basariyla giris yaptiniz.")
                    print(i)
                    DogruGiristeCikma=11
                    break
                elif(i==Olusturulan_hesap_sayisi-1):
                    print("Malesef Böyle bir hesap bulunmamaktadir.")
                    
                
    elif (islem == "3"):
        break
    
    else:
        print("Yanlis Tusa bastiniz.")