#should work but doesnt :( vvvvv
#print [sum([i*j for i in xrange(a,b) for j in xrange(c,d) if int(''.join(list(reversed(sorted(list(str(i)+str(j)+str(i*j)))))))==987654321 and i*j not in locals()['_[1]']]) for a,b,c,d in [[0,10,1000,10000],[10,100,100,1000]]]
li=[]
for i in xrange(0,10):
    for j in xrange(1000,10000):
        p=i*j
        if int(''.join(list(reversed(sorted(list(str(i)+str(j)+str(p)))))))==987654321 and p not in li:
            li.append(p)
for i in xrange(10,100):
    for j in xrange(100,1000):
        p=i*j
        if int(''.join(list(reversed(sorted(list(str(i)+str(j)+str(p)))))))==987654321 and p not in li:
            li.append(p)
print sum(li)
