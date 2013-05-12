upper=1.1
lower=1.0
t=0
while t!=-600000000000:
    r=(upper+lower)/2.0
    t=sum((900-3*k)*r**(k-1) for k in range (1,5001))
    if t<-600000000000:upper=r
    else:lower=r
