# Map fonksiyonu ->  map(fonksiyon, iterasyon yapılabilicek veri tipi ör : liste demet ...)
# yazdığımız liste veya demetteki objeleri tek tek alıp fonksiyonun içine göndericek.

def double(x):
    return x * 2

print(list(map(double,[1,2,3,4,5,6])))

print(list(map(lambda x : x**2 , (1,2,3,4,5,6,7,8,9,10))))


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y,z : x*y*z,liste1,liste2,liste3)))