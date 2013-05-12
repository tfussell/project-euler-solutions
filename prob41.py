#started with 1-9 and moved down
from primalitytest import isPrime
def permutations(items,n=-1):
    if n==-1:n=len(items)
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in permutations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

z=list(permutations('1234567'))
m=0
for i in z:
	if isPrime(int(''.join(i))):
		if int(''.join(i))>m:m=int(''.join(i))
if m:print m
else:print 'not found'
