import time
import psyco
psyco.full()
memo={1:1}
def chainLength(num):
    if not memo.has_key(num):
        if num&1:memo[num]=chainLength((num*3+1)/2)+2
        else:memo[num]=chainLength(num/2)+1
    return memo[num]
start=time.time()
for i in xrange(1,10000000):chainLength(i)
print memo.keys().index(max(memo.values()))+1
print time.time()-start
