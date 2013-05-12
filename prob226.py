def blancmange(x,depth):
    return sum([(sawtooth((2**n)*x)/2**n) for n in xrange(depth+1)])
def sawtooth(x):
    return abs(round(x)-x)
print [blancmange(n/10.0,0) for n in xrange(11)]
