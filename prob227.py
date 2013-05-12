from random import randint
p=50
while not p==1 or p==100:
    a=randint(1,6)
    if a==1:p-=1
    elif a==6:p+=1
    print p
