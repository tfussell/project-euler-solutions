import psyco
psyco.full()
o=[]
def printer(x):
	s=int(''.join([str(i) for i in x]))
	x=s
	if not x%17:
		x=int(x/10)
		if not x%13:
			x=int(x/10)
			if not x%11:
				x=int(x/10)
				if not x%7:
					x=int(x/10)
					if not x%5:
						x=int(x/10)
						if not x%3:
							x=int(x/10)
							if not x%2:
								o.append(s)
								print o
	return 1
def permute(table=range(10), permutation=[],
      num_items=10, callback=printer):
    if len(permutation) == num_items or len(table)==0:
        return [callback(permutation)]
    return sum([permute(table[:i]+table[i+1:],
            permutation+[table[i]], num_items, callback) for i in range(len(table))],[])
permute()
