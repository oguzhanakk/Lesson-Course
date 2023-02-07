"""
Python'da Demet Oluşturma
"""

demet = (1,2,3,4,5,6,7)

print(type(demet))

print(demet[-1])
print(demet[::-1])

print("-------")
#Count fonk. = Yazılan verinin o demette kaç defa geçtiğini söylüyor.
YeniDemet = (1,1,2,3,4,5,6,1,2,3,1)

print(YeniDemet.count(1))
print(YeniDemet.count(8))

print("-------")
#İndex fonk. = yazılan verinin (varsa) kaçıncı indexte oldugunu veriyor.
#(yoksa) hata verir.
Demet2 = ("Alex","Hasan","Kapo","Kemal")

print(Demet2.index("Kapo"))
print(Demet2.index("Kemal"))