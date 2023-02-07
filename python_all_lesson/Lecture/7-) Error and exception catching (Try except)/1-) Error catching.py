"""
Hata ve istisna yakalama
"""

try:
    a = int ("sd5423ad")
    print("Program burada")
    
except:
    print("Hata yakalandi.")
    
'---------------------------------------'

try:
    a=int(input("sayi1: "))
    b=int(input("sayi2: "))
    
    print1(a/b)
    
'except(ValueError , zeroDivisonError) : de yazabilirsin.'
    
except ValueError:
    print("Dogru degeri giriniz.")
except ZeroDivisionError:
    print("Sayi 0'a bolunemez")