import sys
sys.setrecursionlimit(2000)
from math import exp
def tetration(a,b):
    s=a
    for i in xrange(b-1):
        s=a**s
        s=int(str(s)[-8:])
    return s
print tetration(3,2)
