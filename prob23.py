import psyco
psyco.full()
import time
def isAbundant(x):
    t=0
    for i in xrange(1,x/2+1):
        if x%i==0:t+=i
        if t>x:return 1
    return 0
x=[i for i in xrange(1,28123) if isAbundant(i)]
print '1'
y=[i+j for i in x for j in x if i+j<28123]
print '1.5'
t=set()
for i in y:
    t.add(i)
print '2'
print sum([i for i in xrange(1,28123) if i not in t])
