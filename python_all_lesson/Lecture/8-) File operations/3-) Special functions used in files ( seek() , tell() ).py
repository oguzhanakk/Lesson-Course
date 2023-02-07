"""
Dosyalarda kullanilan ozel fonksiyonlar
"""

OkumaDosyasi = open("UcuncuDers.txt","w")
OkumaDosyasi.write("Oguzhan Akkoyunlu\nEmre Kara\nCem Bolukbasi")
OkumaDosyasi.close()

'Dosyayi otomatik kapatma'

with open("UcuncuDers.txt","r") as OkumaDosyasi:
    for i in OkumaDosyasi:
        print(i)
        
"------------------------------------------------------------"

'Dosyalari ileri geri sarmak'

#Seek(5) -> imleci 5 birim goturmek icin
#tell() -> hangi imlecte oldugumuzu ogrenmek icin

with open("UcuncuDers.txt","r") as OkumaDosyasi:
    
    OkumaDosyasi.seek(5)
    icerik = OkumaDosyasi.read(10)
    print(icerik)
    print(OkumaDosyasi.tell())