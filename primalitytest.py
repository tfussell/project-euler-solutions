from math import sqrt,floor
import psyco

psyco.full()

def isPrime(n):
	if n==1:return 0
	elif n<4:return 1
	elif not n%2:return 0
	elif n<9:return 1
	elif not n%3:return 0
	else:
		r=floor(sqrt(n))
		f=5
		while f<=r:
			if not n%f or not n%(f+2):return 0
			f+=6
		return 1
