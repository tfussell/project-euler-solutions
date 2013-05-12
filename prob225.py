import psyco
psyco.full()

def tribonacci():
    a=1
    b=1
    c=1
    for i in xrange(10000):
        yield a+b+c
        #$#print i
        a,b,c=b,c,a+b+c

def remove_multiples(li,x):
    print x
    mult=0
    while mult*x<max(li):
        mult+=1
        if mult*x in li:
            li.remove(x)
    #print x,num_removed
##num_of_odds=0
##current=1
##odds_list=[]
##for i in xrange(10000):
##    odds_list.append(27+i*2)
print "created odds list"
t=tribonacci()
for i in t:
    #remove_multiples(odds_list,i)
    print i
print odds_list[123]
