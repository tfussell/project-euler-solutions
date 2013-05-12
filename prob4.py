def bin(n):
    bStr = ''
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return int(bStr)
f=0
for i in xrange(1,1000000):
    a=list(str(i))
    a.reverse()
    a=int(''.join(a))
    b=i
    c=str(bin(b))
    c=list(c)
    c.reverse()
    c=int(''.join(c))
    if a==b and bin(a)==c:
        f+=b
print f
