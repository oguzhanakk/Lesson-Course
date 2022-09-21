"""
Kodlama örnekleri (2 tane)
"""

# birincisi oyuncu kaydetme

print("Oyuncu Kaydetme Programi")

Ad = input("Oyuncu adi: ")
Soyad = input("Oyuncu Soyadi: ")
Takim = input("Oyuncunun Takimi: ")

bilgiler = [Ad,Soyad,Takim]

#sleep(5)
print("\nBilgiler kaydediliyor...\n")

print("Oyuncunun Adi : {}\nOyuncunun Soyadi : {}\nOyuncunun Takimi: {}\n".format(Ad,Soyad,Takim))

print("Bilgiler Kaydedildi...")

# ikincisi Kok bulma

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci kok : {}\nIkinci kok : {}\n".format(x1,x2))