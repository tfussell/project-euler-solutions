def p(x): return x*(3*x-1)/2
pents=[p(i) for i in xrange(3000)]
def isp(x):return not (.5+(.25+6*x)**.5)/3%1
c=0;i=1;j=2
while not (isp(p(j)-p(i)) and isp(p(j)+p(i))):
    j+=1
    if j==3000:i+=1;j=i
print p(j)-p(i)
