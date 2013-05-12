for i in range(9999,1,-1):
    s=[str(i*j) for j in range(1,5) if len(''.join(locals()['_[1]']))<9]
    if list(sorted(list(''.join(s))))==list('123456789'):print ''.join(s);break
