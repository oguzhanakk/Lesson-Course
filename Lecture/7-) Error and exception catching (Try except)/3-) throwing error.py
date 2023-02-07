"""
        Hata fırlatmak
"""

'raise HataAdi(opsiyonel hata mesaji)'

def terscevir(s):
    if(type(s) != str):
        raise ValueError("Lutfen string degeri giriniz.")
    else:
        return s[::-1]
    
    
try:
    print(terscevir(12))
    
except:
    print("Fonksiyon hata verdi.")