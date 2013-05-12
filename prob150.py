from math import sqrt
from random import randint,shuffle,sample
def dist(a,b):
    return sqrt((a+b)**2-(a-b)**2)
def random_swap(li,temp):
    for i in xrange(temp):
        rand1,rand2=randint(0,len(li)-1),randint(0,len(li)-1)
        li[rand2],li[rand1]=li.pop(rand1),li.pop(rand2)
def cost(li):
    l=0
    for i in xrange(1,len(li)):l+=dist(li[i-1],li[i])
    return l
def average_change(li):
    
li=[]
for i in range(30,51):
    li.append(i*1000.0)
random_swap(li,5)
print li
