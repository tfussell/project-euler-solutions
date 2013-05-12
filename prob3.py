import math

def factor(n):
    highest = 0
    i = 2
    while i < math.sqrt(n)+1:
        if not n%i:
            if isPrime(i):highest = i
        i+=1
    return highest

def isPrime(n):
    i = 2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

print factor(600851475143)
