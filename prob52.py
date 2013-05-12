def stringCount(n):
    li = []
    for i in n:
        if i not in li:
            li.append(i)
    for i in xrange(len(li)):
        li[i] = (li[i],n.count(li[i]))
    return li

def compareLists(l1,l2):
    diff=[]
    for i in l1:
        if i not in l2:
            diff.append(i)
    return diff==[] and len(l1)==len(l2)

j=1
i=125874
while j!=7:
    j=1
    while j<7 and compareLists(stringCount(str(i)),stringCount(str(j*i))):
        if j>5:print i,j,i*j
        j+=1
    i+=1
