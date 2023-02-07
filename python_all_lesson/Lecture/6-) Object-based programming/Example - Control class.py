import random
import time

class Kumanda():
    def __init__(self,tv_durumu='Kapali',tv_ses=0,kanal_listesi=['TRT'],kanal="trt"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        
    def tv_ac(self):
        if(self.tv_durumu == 'Acik'):
            print('Televizyon zaten acik')
        else:
            print("Televizyon aciliyor...")
            self.tv_durumu = 'Acik'
            
    def tv_kapat(self):
        if(self.tv_durumu == 'Kapali'):
            print('Televizyon zaten kapali')
        else:
            print("Televizyon kapatiliyor...")
            self.tv_durumu = 'Kapali'
            
    def ses_ayarlari(self):
        while True:
            cevap = input('Sesi azalt: <\nSesi arttir : >\nCikis : cikis ')
            
            if(cevap == '<'):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print('Ses',self.tv_ses)
                    
            elif(cevap == '>'):
                    if(self.tv_ses != 31):
                        self.tv_ses += 1
                        print('Ses',self.tv_ses)
                
            else:
                    print('Ses güncellendi:',self.tv_ses)
                    break
                        
    def kanal_ekle(self,kanal_ismi):
        
        print("Kanal ekleniyor...")
        time.sleep(1)
        
        self.kanal_listesi.append(kanal_ismi)
        
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        
        print("Su anki kanal: ",self.kanal)
        
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv durumu : {}\nTv ses : {}\nKanal listesi : {}\nŞu anki kanal : {}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)
    
    
kumanda = Kumanda()
    
print("""
      
      Televizyon Uygulamasi
      
      1. Tv ac
      2. Tv kapat
      3. Ses ayarlari
      4. Kanal ekle
      5. Kanal sayisini ogrenme
      6. Rastgele kanala gecme
      7. Televizyon bilgileri
      
      Cikmak icin 'q' ya basin.
      
      """)
      
while True : 
    
    islem = input('islemi seciniz: ')
    
    if(islem == 'q'):
        print('Program sonlandiriliyor.')
        break
    
    elif(islem == '1'):
        kumanda.tv_ac()
        
    elif(islem == '2'):
        kumanda.tv_kapat()
        
    elif(islem == '3'):
        kumanda.ses_ayarlari()
        
    elif(islem == '4'):
        kanal_isimleri = input('Kanal isimlerini "," ile ayirarak girin : ')
        
        kanal_listesi = kanal_isimleri.split(",") #ögrenmedigin bir fonksiyon
        
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
        
    elif(islem == '5'):
        print('kanal sayisi: ',len(kumanda))
        
    elif(islem == '6'):
        kumanda.rastgele_kanal()
        
        
    elif(islem == '7'):
        print(kumanda)
        
    else:
        print("Gecersiz islem.")
      
      
      
      
      
      
      
      
      