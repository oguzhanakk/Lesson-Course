"""
Fonksiyonlarda Global ve Yerel Değişkenler
"""

# Local Variable sadece fonksiyon ve sınıflarda oluyor.

c=10 #Global variable
def fonksiyon():
    c=12
    print(c) #Local variable

fonksiyon()
print(c)

print("----------------------")

#Global ifadesi (degiskeni komple degistiriyor.)

d=5
def fonksiyon2():
    global d  #Global d yi degistirmek icin kullandık
    d=3 #Global d yi 3 yaptik
    print(d)
    
fonksiyon2()
print(d)