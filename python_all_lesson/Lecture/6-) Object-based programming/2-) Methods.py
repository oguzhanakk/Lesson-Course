"""
Methodlar ve özelleştirme
"""

class Yazilimci():
    def __init__(self,isim,soyisim,maas,bildigiDiller):
        self.isim = ali
        self.soyisim = cem
        self.maas = veli
        self.bildigiDiller = selam
        
    def bilgileriGoster(self):
        print("""
              Yazilimci objesinin ozellikleri
              
              isim = {}
              soyisim = {}
              maas = {}
              bildigi diller = {}
              
              """.format(self.isim,self.soyisim,self.maas,self.bildigiDiller))
              
    def dil_ekle(self,yeniDil):
        self.bildigiDiller.append(yeniDil)
        
    def zam_yap(self,zamMiktari):
        self.maas += zamMiktari
              
yazilimci1 = Yazilimci("Oguzhan","Akkoyunlu",3000,['C','Python'])
yazilimci2 = Yazilimci("Adnan","Akkoyunlu",4000,'Yok')

yazilimci1.bilgileriGoster()
yazilimci2.bilgileriGoster()

yazilimci1.dil_ekle('Java')
yazilimci2.zam_yap(9000)

yazilimci1.bilgileriGoster()
yazilimci2.bilgileriGoster()