print("""
Faktoriyel Bulma Programi
(cikmak icin : q)
""")

while True:
    sayi = input("Faktoriyelini bulmak istediginiz sayiyi girin: ")
    
    if(sayi == "q"):
        print("Elveda bro.")
        break
    
    else:
        sayi = int(sayi)
        
        faktoriyel = 1
        
        for i in range(2,sayi+1):
            faktoriyel *= i
            
        print(faktoriyel)
        
#------------------------------------------------------------------

print("""
Fibonacci Programi
""")

a=1
b=1

fibonacci = [a,b]

sayi = int(input("Kac basamak fibonacci ilerlesin: "))

for i in range(sayi):
    
    a,b = b,a+b
    
    fibonacci.append(b)
    
print(fibonacci)