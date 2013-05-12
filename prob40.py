from math import log
def digit(d):
    c=0
    l=0
    tl=0
    s=''
    while tl<d:
        c+=1
        s+=str(c)
        l=int(log(c,10))+1
        tl+=l
    print s,c,l,tl,d,tl-d
    return str(c)[len(str(c))-1-(tl-d)]
