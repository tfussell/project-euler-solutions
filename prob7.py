from primalitytest import isPrime
numprimes,n=1,1
while not numprimes==10001:
    n+=2
    if isPrime(n):numprimes+=1
print n
