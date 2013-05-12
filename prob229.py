from math import sqrt
def fits_all_rules(a):
    w,x,y,z=1,0,0,0
    for i,j in count_exponents(prime_factors(3600)):
        if not abs(i-3)%4:
            if j!=2:w=0
    for i in xrange(2,a):
        for j in xrange(2,i):
            if not x:
                if i**2+2*j**2==a:
                    x=1
                    print '2',i,j
            if not y:
                if i**2+3*30**2==a:
                    y=1
                    print '3',i,j
            if not z:
                if i**2+7*j**2==a:
                    z=1
                    print '4',i,j
    print w,x,y,z
    return w and x and y and z
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
    out=[(i,li.count(i)) for i in temp]
    return out
