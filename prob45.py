def p(n):return n*(3*n-1)/2
def h(n):return n*(2*n-1)
b=[p(i) for i in xrange(40000,0,-1)]
c=[h(i) for i in xrange(40000,0,-1) if h(i)<b[0]]
for i in c:
    if i in b:print i;break
