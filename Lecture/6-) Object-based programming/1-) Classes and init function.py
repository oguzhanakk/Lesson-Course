"""
Nesne tabanlı programlama konusu (class , method , inheritance(kalıtım) , overriding(iptal etme) , özel methodlar)
"""

"""
class Araba():
    Model = "Reanult Megane"
    Renk = "Gumus"
    Beygir = 110
    Silindir = 4
    
araba1 = Araba()
araba2 = Araba()

print(araba1.Silindir)
print(araba2.Model)
"""

'-----------------------------------------------'

'__init__ fonksiyonu ile özelleştirme'

class Araba():
    def __init__(self,model,renk,beygir,silindir):
        print("İnit fonksiyonu cagirildi")
        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir
        
araba1 = Araba("Renault","Gumus",110,4)
araba2 = Araba("Peugeot","Siyah",230,6)

print(araba1.beygir,araba2.beygir,araba1.model,araba2.model)
