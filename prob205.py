def sixesbelow(n):
    numpete,numdraws,numcolin=0,0,0
    for i in xrange(6):
        for j in xrange(6):
            for k in xrange(6):
                for l in xrange(6):
                    for m in xrange(6):
                        for n in xrange(6):
                            o=i+j+k+l+m+n
                            if o<n:
                                numpete+=1
                            elif o==n:
                                numdraws+=1
                            else:
                                numcolin+=1
    return numpete,numdraws,numcolin
for i in xrange(4**9):
    print sixesbelow(i)
