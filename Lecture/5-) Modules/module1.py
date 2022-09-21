"""
Kendi modulumuzu yazmak
"""

'Picler diyari modulumuzu'

Picler_isimleri=['Oguzhan','Kapo','Berkay','Nihat','Kemal']

def selamla(isim):
    """
    Bu fonksiyon vericeginiz pic ismini selamlamaya yarar.
    """
    
    print('Selam pic',isim)
    
def enKaraktersiziBulma(isim1,isim2,isim3):
    """
    Bu fonksiyon vericeginiz 3 isimden en karakterisizi soyler
    """

    if((isim1 or isim2 or isim3) in Picler_isimleri[0]):
        print("En pic isim : ",Picler_isimleri[0])
        
    else:
        print("Bunlar kral cocuklardir.")
    