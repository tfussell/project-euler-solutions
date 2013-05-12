def fact(x): return (1 if x==0 else x * fact(x-1))
fact_table=dict([[i,fact(i)] for i in xrange(0,10)])
for i in xrange(3,1000000):
    if i==sum([fact_table[int(j)] for j in str(i)]):
        print i
