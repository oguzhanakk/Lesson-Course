"""
Python'da Sözlük (Dictionary)
"""

Sozluk1 = {"bir":1 , "iki":2, "üç":3}

print(type(Sozluk1))

bosSozluk = {}

print(Sozluk1["iki"])

# eleman ekleme -> elemanı basa ekliyo fakat anahtar kelimeyle eristigimiz
#icin nereye ekledigi pek önemli degil 
Sozluk1["bes"] = 5

#sözlükte value degistirme
Sozluk1["bir"] = 20
print(Sozluk1)


print(Sozluk1["bes"])

Sozluk2 = {"ilk" : [1,2,3,4], "ikinci" : [[1,2],[3,4],[5,6]]}

print(Sozluk2["ilk"])

print("---------------\n")
#İç içe sözlükler
icice = {"sayilar" : {"bir":1,"iki":2,"üc":3},"meyveler": {"kiraz":"yaz","erik":"kıs"}}

print(icice["sayilar"])
print(icice["meyveler"]["kiraz"])

#Fonksiyonları
print("-----------\n")
#keys = anahtar kelimeleri veriyor
print(Sozluk1.keys())
#values = degerleri veriyor
print(Sozluk1.values())
#items = demet haline getiriyor
print(Sozluk1.items())