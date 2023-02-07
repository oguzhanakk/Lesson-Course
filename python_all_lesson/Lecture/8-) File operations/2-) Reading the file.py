"""
Dosya Okuma islemleri
"""

'Dosyayi Okuma'


okumaDosyasi = open("Okuma.txt","w")
okumaDosyasi.write("Oguzhan Akkoyunlu\nAdnan Akkoyunlu\nilayda lekic\nOrcun karaer")
okumaDosyasi.close()


try:
    okumaDosyasi = open("OlmayanDosya.txt","r")
except:
    print("Okumak istediginiz dosya bulunamadi\n")

'-----------------------------------------------------------'

"For dongusuyle okuma"

okumaDosyasi = open("okuma.txt","r")

for i in okumaDosyasi:
    print(i,end="")
    
okumaDosyasi.close()

print("\n")

'-----------------------------------------------------------'

"Read fonksiyonu"

okumaDosyasi = open("okuma.txt","r")

icerik = okumaDosyasi.read() #okumaDosyasi.read(10) yazabilirsin yazmazsan tamamini okur.

print(icerik)

okumaDosyasi.close()

'-----------------------------------------------------------'

"Readline() fonksiyonu"

#Her cagirildiginda dosyanin sadece 1 satirini okur. imlec 1 satır atlayarak devam eder.

okumaDosyasi = open("okuma.txt","r")

print(okumaDosyasi.readline())
print(okumaDosyasi.readline())

okumaDosyasi.close()

'-----------------------------------------------------------'

"Readlines() fonksiyonu"

#Txt dosyasini liste olarak cevirir.

okumaDosyasi = open("okuma.txt","r")

liste = okumaDosyasi.readlines()

print(liste)

okumaDosyasi.close()











