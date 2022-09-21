"""
Python'da Mantıksal ve karşılaştırma operatörleri
"""

print(bool(3))
print(bool(0))

# Sayı 0 mı negatif mi pozitif mi onu bulma
number = float(input("Bir sayi giriniz: "))

if (number >= 0):
    if (number == 0):
        print("Girdiginiz sayi 0'dir.")
    else:
        print("Girdiginiz sayi pozitiftir.")
else:
    print("Girdiginiz sayi negatiftir.\n")
    
# Hesap Makinesi
print("""****************
işlemler;

1.Toplama işlemi

2.Çikarma işlemi
      
3.Çarpma işlemi

4.Bolme işlemi
****************""")

a = int(input("1.sayiyi giriniz: "))
b = int(input("2.sayiyi giiniz: "))

işlem = input("işlemi giriniz: ")

if işlem == "1":
    print("{} ile {} toplami {}".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} çikarimi {}".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} çarpimi {}".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} bölümü {}".format(a,b,a/b))