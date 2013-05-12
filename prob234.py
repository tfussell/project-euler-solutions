def ups(n):
    n=1
    while p[n]<x:
        n+=1
    return n
def lps(x):
    n=len(p)-1
    while p[n]>x:
        n-=1
    return n
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
high=999966663333
p=primes(int(high**.5))
i=4
t=0
while i<=high:
    s=i**.5
    if i%lps(s)^i%ups(s):t+=i
