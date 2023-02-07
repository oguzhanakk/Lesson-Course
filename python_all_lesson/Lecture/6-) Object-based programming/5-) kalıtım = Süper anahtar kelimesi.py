"""
Overriding konusunda Süper anahtar kelimesi
"""

class calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin init foknsiyonu")
        
        self.isim = isim
        self.maas = maas
        self.departman = departman
        
    def departmanDegis(self,yeniDepartman):
        print("Calisan initi objesi")
        self.departman = yeniDepartman
        
    def bilgileriGoster(self):
        print("isim:",self.isim,"Maas:",self.maas,"Departman:",self.departman)
        

class Yonetici(calisan):
    
    def __init__(self,isim,maas,departman,rütbesi): #Calisan initini iptal etti
        print("Yonetici sinifinin init fonksiyonu")
   
        super().__init__(isim,maas,departman) #self.isim , self.maas , self.departman
                                              # tek tek yazmak yerine super anahtar kullanilir
                                              # Hem calisan initi calisir hem yönetici initi
        self.rütbesi = rütbesi
    
    def zam_yap(self,zamMiktari):
        self.maas += zamMiktari
        

yonetici1 = Yonetici("Oguzhan", 4000, "Muhendislik", "Patron")

yonetici1.bilgileriGoster()
yonetici1.departmanDegis("Hademe")
yonetici1.bilgileriGoster()
