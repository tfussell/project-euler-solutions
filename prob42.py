print sum([1 for i in open('words.txt').read().split(',') if sum(['"abcdefghijklmnopqrstuvwxyz'.index(j) for j in i.lower()]) in [int(.5*n*(n+1)) for n in xrange(30)]])
