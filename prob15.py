m={}
def numways(x,y):
    if str(x)+' '+str(y) not in m:
        if not x or not y:m[str(x)+' '+str(y)]=1
        else:m[str(x)+' '+str(y)]=numways(x-1,y)+numways(x,y-1)
    return m[str(x)+' '+str(y)]
print numways(19,20)*2
