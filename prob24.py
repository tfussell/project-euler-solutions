def xpermutations(items):
    return xcombinations(items, len(items))

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

out=[]
for i in xpermutations('0123456789'):
    out.append(i)
print 'Done'
print 'Sorting'
out.sort()
print out[999999]
