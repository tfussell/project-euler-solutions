from math import sqrt,floor
for i in xrange(999999999,-1,-1):
    n=sqrt(int("1%s2%s3%s4%s5%s6%s7%s8%s9%s0"%(tuple(str(i).rjust(9,'0')))))
    if n==floor(n):break
print n
