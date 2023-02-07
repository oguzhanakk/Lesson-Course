"""
Nesne tabanli programlama - İnheritance(Kalitim)
"""

class calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin init foknsiyonu")
        
        self.isim = isim
        self.maas = maas
        self.departman = departman
        
    def departmanDegis(self,yeniDepartman):
        self.departman = yeniDepartman
        
    def bilgileriGoster(self):
        print("isim:",self.isim,"Maas:",self.maas,"Departman:",self.departman)
        

class Yonetici(calisan):
    
    def zam_yap(self,zamMiktari):
        self.maas += zamMiktari

ilkYonetici = Yonetici("Oguzhan",7000,"Mühendislik")

ilkYonetici.bilgileriGoster()
ilkYonetici.zam_yap(30000)
ilkYonetici.bilgileriGoster()