"""
Lambda ifadeleriyle fonksiyon tanımlama
"""

# Lambda = Kısa fonksiyonları tek satırla olusturmaya yarıyor.

print("1. Fonksiyon icin:")

def ikiyleCarp(x):
    return x*2
print(ikiyleCarp(4))

ikiyleCarpLambda = lambda x: x*2
print(ikiyleCarpLambda(4))

#------------------------------------
print()
print("2. fonksiyon icin:")

def toplama(x,y,z):
    return x+y+z
print(toplama(10,12,12))

toplamaLambda = lambda x,y,z : x+y+z
print(toplamaLambda(10,12,12))

#------------------------------------
print()
print("3. fonksiyon icin:")

def tersCevir(s):
    return s[::-1]
print("Selamlar herkese")

tersCevirLambda = lambda s : s[::-1]
print("Selamlar herkese")

#------------------------------------
print()
print("4. fonksiyon icin:")

def CiftTek(sayi):
    return sayi % 2 == 0
print(CiftTek(4))

CiftTekLambda = lambda sayi : sayi % 2 == 0
print(CiftTekLambda(4))