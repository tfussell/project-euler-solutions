from primalitytest import isPrime
from math import log

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]
x=primes(20000000)
high=10
n=0
print len(x)
while high>1:
    i=x[n]
    for j in xrange(2,int(high)+1):
        x.append(i**j)
    n+=1
    high=log(20000000,i)
print x[-1000:]
