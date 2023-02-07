"""
Dosya işlemleri
"""

'Dosyayi acma ve dosyaya yazma'


'open(dosya_adi , dosya_erisme_kipi)'
'w dosya kipi = oyle bir dosya yoksa olusturuyor , varsa silip tekrar olusturuyor.'

file = open("bilgiler.txt","w")
file.write("Oguzhan Akkoyunlu\n")
file.close()

file = open("bilgiler.txt","a")
file.write("Adnan Can Akkoyunlu")
file.close()
