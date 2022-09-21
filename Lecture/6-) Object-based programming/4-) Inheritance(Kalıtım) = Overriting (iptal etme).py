"""
Nesne tabanlı programlama - Overriding (iptal etme)(Kalıtım konusunda)
"""

'Miras aldigimiz methodu ayni isimle tanimlarsak cagirinca miras aldigin degil kendi methodun calisir'

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
        
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.rütbesi = rütbesi
    
    def zam_yap(self,zamMiktari):
        self.maas += zamMiktari
        

yönetici1 = Yonetici("Oğuzhan", 3000, "Mühendislik", "Patron")

yönetici1.bilgileriGoster()
yönetici1.departmanDegis("Ögretmen")
yönetici1.bilgileriGoster()