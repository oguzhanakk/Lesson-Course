"""
Python'da For Döngüsü
"""

#İn Operatörü
print(5 in [1,2,3,4])
print(3 in [1,2,3,4])
print("p" in "python")
print("p" in "ali")

#For Döngüsü
liste = [1,2,3,4]

for i in liste:
    print(i)
    
toplam1 = 0
toplam2 = 0

for i in liste:
    toplam1 += i
print("Listedeki sayilarin toplami = {}".format(toplam1))

for i in liste:
    if i % 2 == 0:
        toplam2 += i
print("Listedeki cift sayilarin toplami = {}".format(toplam2))

"""
#String de gezinme
s = "Python"

for i in s:
    print(i)
    
#Demette gezinme
demet = (1,2,3,5,7,9)

for a in demet :
    print(a)
"""

#Demette 2,3 boyut

liste = [(1,2),(3,4),(5,6),(7,8)]

for i,j in liste:
    print("i:{} , j:{}".format(i,j))
    
# Sözlükte gezinmek

Sözlük = {"bir":1 , "iki":2 , "üc":3}

for i in Sözlük.values():
    print(i)
    
for i,j in Sözlük.items():
    print(i,j)