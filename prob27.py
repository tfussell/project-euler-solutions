from primalitytest import isPrime
def num_con_primes(a,b):
    n=0
    while isPrime(abs(n**2+a*n+b)):
        n+=1
    return n
longest=(-1,-999,-999)
for a in xrange(-999,1000):
    for b in xrange(-999,1000):
        c=num_con_primes(a,b)
        if c>longest[0]:longest=(c,a,b)
print longest[1]*longest[2]
