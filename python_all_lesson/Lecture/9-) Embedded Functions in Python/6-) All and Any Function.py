# All Fonksiyonu -> Asagidaki ornegi otomatik yapmaya yariyor.

#bütün degerler true ise true , en az birisi false ise false dondurmek istiyoruz.
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
        
liste2 = [True,False,True,False,True]

print(hepsi(liste2))
print(hepsi([1,2,3,4,5]))

#iclerinden bi tane bile true varsa true oluyor. Diger durumlarda false oluyor.
def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

print(herhangi(liste2))
print(herhangi([0,0,0,0,0,0]))

#-----------------------------------------------------------------------------
print("")

print(all([1,2,3,4,5,6,0]))
print(any([1,2,3,4,5,6,0""]))