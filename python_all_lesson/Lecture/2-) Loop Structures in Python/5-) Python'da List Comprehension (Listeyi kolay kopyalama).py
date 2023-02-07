"""
Python'da List Comprehension
"""

# Bir Listeyi başka bir listeye for döngüsü kurmadan aktarma...

#For ile aktarma
liste1 = [1,2,3,4,5]
liste2 = list()

for i in liste1:
    liste2.append(i)
    
#List Comprehension ile aktarma
liste1 = [1,2,3,4,5]
liste2 = [i for i in liste1]

liste3 = [3,4,5]
liste4 = [i*2 for i in liste3]

liste5 = [(1,2),(3,4),(5,6)]
liste6 = [i*j for i,j in liste5]

s = "Python"
liste8 = [i*3 for i in s]

print(liste2,liste4,liste6,liste8)

#iç içe listeyi tekli olarak alma
liste10 = [[1,2,3],[4,5,6,7],[8,9,10,11]]

#for ile
liste11 = list()

for i in liste10:
    for x in i:
        liste11.append(x)
        
#List comprehension ile
liste12 = [x for i in liste10 for x in i]

print(liste11,liste12)
