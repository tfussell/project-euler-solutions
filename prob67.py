import time
start=time.time()
tri=[[int(s) for s in i.split()] for i in open('tri.txt')]
def maxSum(L):
    d={}
    def m(x,y):
        if (x,y) not in d:
            if y==len(tri)-1:d[(x,y)]=tri[y][x]
            else:d[(x,y)]=tri[y][x]+max([m(x,y+1),m(x+1,y+1)])
        return d[(x,y)]
    return m(0,0)
print maxSum(tri)
print time.time()-start
