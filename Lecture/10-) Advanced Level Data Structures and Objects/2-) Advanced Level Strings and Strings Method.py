#https://www.tutorialspoint.com/python3/python_strings.htm
#https://nbviewer.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/%C4%B0leri%20Seviye%20Veri%20Yap%C4%B1lar%C4%B1%20ve%20Objeler/%C4%B0leri%20Seviye%20Karakter%20Dizileri%20%28Stringler%29.ipynb

# upper() and lower()
strings1 = "AhmEt CeM"

print(strings1.lower())
print(strings1.upper())

# replace(x,y) -> Stringteki x degerlerini y ile degistirir
strings2 = "ahmak aglatan adamsin sen"

print(strings2.replace("a" , "o"))
print(strings2.replace(" " , "-"))
print(strings2.replace("aglatan" , "cem"))


# startswith(x) -> string x ile basliyorsa True , baslamiyorsa False
# endswith(x) -> string x ile bitiyorsa True , bitmiyorsa False
strings3 = "Oguzhan Akkoyunlu"

print(strings3.startswith("O"))
print(strings3.startswith("a"))
print(strings3.endswith("Akkoyunlu"))

# split(x) -> verilen bir x degerine gore string parcalara ayrilarak her bir parca listeye atilir.
strings4 = "Python Programlama Dili"
strings5 = "Oguzhan-Cem-Akkoyunlu-Dem"

print(strings4.split(" "))
print(strings5.split("-"))

# strip(x) -> stringin basinda ve sonunda bulunan x degerini siler.
# lstrip(x) -> stringin sadece basinda bulunan x degerini siler.
# rstrip(x) -> stringin sadece sonunda bulunan x degerini siler.
strings6 = "                         Fenerbahce1907             "

print(strings6.strip())
print(strings6.strip(" F"))
