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

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def replace(indicies,li,n):
    for i in indicies:
        li[i]=n

def numPrimes(li):
    tot=0
    for i in li:
        if int(i) in pList:
            tot+=1
    return tot
counter=0
whole=[]
global pList
pList = primes(1000000)
while numPrimes(whole)!=8:
    n=pList[counter]
    print n,
    whole=[]
    n=str(n)
    combs=[]
    for j in xrange(len(n)):
        combs+=[i for i in xuniqueCombinations([x for x in xrange(len(n))],j+1)]
    for i in combs:
        for k in xrange(10):
            t=list(n)
            replace(i,t,str(k))
            if ''.join(t)!=n and ''.join(t) not in whole:
                whole+=[''.join(t)]
    print numPrimes(whole)
    counter+=1
print n,counter,whole
