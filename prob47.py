def num_uniq_pfactors(n):
    factors = []
    lastresult = n
    if n == 1:
        return [1]
    while 1:
        if lastresult == 1:
            break
        c = 2
        while 1:
            if lastresult % c == 0:
                break
            c += 1
        if c not in factors:
            factors.append(c)
        lastresult /= c
    return len(factors)
i=1
while num_uniq_pfactors(i)!=4 or num_uniq_pfactors(i+1)!=4 or num_uniq_pfactors(i+2)!=4 or num_uniq_pfactors(i+3)!=4:
    i+=1
print i
