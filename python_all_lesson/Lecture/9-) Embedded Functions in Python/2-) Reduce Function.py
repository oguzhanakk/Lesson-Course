# Reduce fonksiyonu -> reduce(function , iterasyon yapılabilen veritipi -> liste...)
# Once listedeki ilk 2 elemanı alır fonksiyona uygular sonra cıkan sonucu alır 3 eleman ile birlikte uygular
#böyle böyle devam eder.

from functools import reduce

def toplama(x,y):
    return x + y

print(reduce(toplama,[12,2,5,10]))

print(reduce(lambda x,y : x * y , [1,2,3,4,5]))

list1 = [1,2,3,4,5]
print(reduce(lambda x,y : x * y , list1))


print("------------------------")

def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y
    
print(reduce(maksimum,[-2,3,1,4,10]))