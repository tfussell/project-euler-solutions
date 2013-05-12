#it's ugly :(
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
p=primes(1000000)
a=[i for i in xrange(3,10000,2) if i not in p]
for i in a:
    l=0
    while p[l]<i:
        l+=1
        c=1
        s=p[l]+2*c**2
        while s<i:
            s=p[l]+2*c**2
            if s==i:break
            c+=1
        if s==i:break
    if s!=i:break
print i
            
