import psyco
psyco.full

x=10**9
x-=4
x=x/5

s=0
for i in xrange(1,x+1):
    s+=26+20*i
    print 26+20*i

print s
