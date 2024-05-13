import random
import math

liste=[]

def randomuret():
    return  random.randint(20, 50)

b=0
while b<5:
    a=randomuret()
    liste.append(a)
    b+=1

newlist=[math.pow(i,2) for i in liste if i%2==0]
print(newlist)

