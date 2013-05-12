fid={}
fi={}
a='14159265358979323846264338327950288419716939937510'
b='58209749445923078164062862089986280348253421170679'
def fib(n):
	if n not in fid:
		if n<2:
			fid[n]=n
		else:
			fid[n]=fib(n-1)+fib(n-2)
	return fid[n]
def f(n):
    if n not in fi:
        if n==1:
            fi[n]=a
        elif n==2:
            fi[n]=b  
        else:
            fi[n]=f(n-1)+f(n-2)
    return fi[n]
t=0
for z in xrange(0,17):
    i=1
    s=((127+19*z)*7**z)
    while fib(i)<s/10+1:
        i+=1
    e=f(i)[s-1]
    t+=int(e)
    print z,e
