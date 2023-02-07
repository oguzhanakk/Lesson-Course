# Filter fonksiyonu -> filter(foknsiyon, iterasyon yapilabilen veritipi -> liste...)
# Fonksiyon objesi true veya false donen bir fonksiyon almak zorunda , listedekileri tek tek koyuyor sadece
#true olanlari gosteriyor.

print(list(filter(lambda x : x % 2 == 0 , [1,2,3,4,5,6,7,8])))


def asal_mi(x):
    i = 2
    
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        while(i < x):
            if(x % i == 0):
                return False
            i += 1
        return True
    

list1 = [1,2,3,4,5,6,7,8]
print(list(filter(asal_mi , list1)))
print(list(filter(asal_mi , range(1,50))))