infile=open("p22names.txt")
for i in infile:
    o=i.split(',')
a='"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
o.sort()
def nscore(n):
    t=0
    for i in n:
        t+=a.index(i)
    return t
t=0
for i,j in enumerate(o):
    t+=(i+1)*nscore(j)
print t
infile.close()
