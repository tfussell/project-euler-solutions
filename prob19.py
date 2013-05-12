mcode=[6,2,2,5,0,3,5,1,4,6,2,4]
t=0
for year in xrange(1901,2000):
    if year%4==0:leap=True
    else:leap=False
    for m in mcode:
        if not(int(str(year)[2:])+int(str(year)[2:])/4+1+m+leap*1)%7:t+=1
for m in mcode:
    if not(int(str(year)[2:])+int(str(year)[2:])/4+m+leap*1)%7:t+=1
print t-1
