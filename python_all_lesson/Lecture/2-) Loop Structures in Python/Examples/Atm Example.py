print("""
Atm'ye Hosgeldiniz...

İslemler:

1.Bakiye Sorgulama
2.Para Yatırma
3.Para Cekme

(Cikmak icin q ya basiniz.)      
""")

Bakiye = 1000

while True:
    
    islem = input("Giriceginiz islemi seciniz: ")
    
    if(islem == "q"):
        print("ELveda Kardeşim.")
        break
    
    elif(islem == "1"):
        print("naber")
        
    elif(islem == "2"):
        print("sa")
        
    elif(islem == "3"):
        print("as")
        
    else:
        print("Yanlis giris yaptiniz.")
    