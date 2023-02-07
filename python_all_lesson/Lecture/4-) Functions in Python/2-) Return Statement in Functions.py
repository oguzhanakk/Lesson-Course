"""
Fonksiyonlarda return deyimi
"""

"""def toplama(a,b,c):
    print(a+b+c)
    
def carp(a):
    print(a*2)
    
toplam = toplama(a,b,c)
print(carp(toplam))  hata verir cünkü toplam notype return olmalı """


def toplama(a,b,c):
    return a+b+c

def carp(a):
    return a*2

print(carp(toplama(3,4,5)))

toplam = toplama(3,4,5)
print(carp(toplam))