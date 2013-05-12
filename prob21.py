def sum_of_divisors(n):
    s=0
    for i in xrange(1,n/2+1):
        if n%i==0:
            s+=i
    return s
div={}
s=0
for i in xrange(10000):
    if i==sum_of_divisors(sum_of_divisors(i)) and i!=sum_of_divisors(i):
        s+=i
print s
