def cancelled(a,b):
    a,b=str(a),str(b)
    if a[0]==b[1]:
        if b[0]!='0':return float(int(a[1]))/int(b[0])
    if a[1]==b[0]:
        if b[1]!='0':return float(int(a[0]))/int(b[1])
    return a,b
t=[[i,j] for i in xrange(11,98) for j in xrange(i+1,99) if float(i)/j==cancelled(i,j)]
d,n=1,1
for i,j in t:
    d*=i
    n*=j
print n/d
