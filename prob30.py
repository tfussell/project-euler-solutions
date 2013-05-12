import psyco
psyco.full()
s=0
for i in xrange(2,1000000):
    t=0
    for j in str(i):
        t+=int(j)**5
    if i==t:s+=i
print s
