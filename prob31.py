##import psyco
##import time
##psyco.full()
##
##start=time.time()
##
##t=0
##for a in xrange(201):
##    for b in xrange(101):
##        for c in xrange(41):
##            for d in xrange(21):
##                for e in xrange(11):
##                    for f in xrange(5):
##                        for g in xrange(3):
##                                if g*100+2*b+5*c+10*d+20*e+50*f+a==200:
##                                    t+=1
##    print a
##print t,time.time()-start
coins = [ 200, 100, 50, 20, 10, 5, 2, 1 ]
 
def foo (rest, i = 0):
    if i == len (coins) - 1:
        return rest % coins[i] == 0
    else:
        return sum (foo (rest - j*coins[i], i + 1)
                    for j in xrange (rest / coins[i] + 1))
 
print foo (200)
