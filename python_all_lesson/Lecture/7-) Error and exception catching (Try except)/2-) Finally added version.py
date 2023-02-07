"""
 Try Except yanina    Finally blogu
"""

'Finally hata olsa da olmasa da mutlaka calisicak kisim'

try:
    a=int(input("Sayi1: "))
    b=int(input("sayi2: "))
    
except:
    print("Programda hata var")
    
finally:
    print("Helalke finally calisti")