import psyco
psyco.full()
import time
a=time.time()
def triangles():
    num=0
    s=1
    while s<10000000000:
        num+=s
        s+=1
        yield num
def prime_factors(n):
    factors = []
    lastresult = n
    if n == 1:
        return [1]
    while 1:
        if lastresult == 1:
            break
        c = 2
        while 1:
            if lastresult % c == 0:
                break
            c += 1
        factors.append(c)
        lastresult /= c
    return factors
def count_exponents(li):
    temp=[]
    for i in li:
        if i not in temp:
            temp.append(i)
    out=[li.count(i) for i in temp]
    product=1
    for i in out:
        product*=i+1
    return product
for start in triangles():
    h=prime_factors(start)
    if count_exponents(h)>500:
        print start,h
        break
print time.time()-a
