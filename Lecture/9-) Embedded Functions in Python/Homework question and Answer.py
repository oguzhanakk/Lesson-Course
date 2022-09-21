#Question-1 Answer (map)

list1 = [(3,4),(10,3),(5,6),(1,9)]

def Calculate_area(tuple):
    return tuple[0] * tuple[1]

print("Question-1 Answer:")
print(list(map(Calculate_area,list1)))
print("-----------------------------")

#-----------------------------------------------------------
#Question-2 Answer (filter)

list2 = [(3,4,5),(6,8,10),(3,10,7)]

def triangle_control(tuple):
    if( tuple[0]**2 + tuple[1]**2 == tuple[2]**2 ):
        return True
    
print("Question-2 Answer:")
print(list(filter(triangle_control,list2)))
print("-----------------------------")

#-----------------------------------------------------------
#Question-3 Answer (filter and reduce)
from functools import reduce

list3 = [1,2,3,4,5,6,7,8,9,10]
    
even_number = list(filter(lambda x : x%2 == 0 , list3))

print("Question-3 Answer:")
print(reduce(lambda x,y : x + y , even_number))
print("-----------------------------")

#----------------------------------------------------------
#Question-4 Answer (zip)

Name = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
Surname = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

print("Question-4 Answer:\n")
for i,j in zip(Name,Surname):
    print(i,j)
    
#------------------------------------------------------------
print("\n---------------------------")

def include_latter(name):
    for i in range(0,len(name)):
        if(name[i] == "n"):
            return True
            
    
print(list(filter(include_latter , ["Cem" , "Ali" , "Ahmet" , "Oguzhan"])))









