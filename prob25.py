d={}
def fibo(n):
    if n not in d: 
        if n < 2:
            d[n]=1
        else:
            d[n]=fibo(n - 1) + fibo(n - 2)
    return d[n]
i=1
a=''
while len(a)<1000:
    a=str(fibo(i))
    i+=1
print i
