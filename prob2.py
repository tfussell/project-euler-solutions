i = [1,2,3]
isum=2
while i[2] < 4000000:
    i.pop(0)
    i.append(sum(i))
    print i[2]
    if i[2]%2==0:isum+=i[2]
print isum
