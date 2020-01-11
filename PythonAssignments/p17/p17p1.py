'''
give a definition of divisors(n):
	if n==1:
		divisors = (1,)
		return divisors
	else:
		divisors = (1,)
		for i between 2, and n//2 + 1):
			if n % i == 0:
				divisors += (i,)
		return divisors


enter a number
if n<=0:
	print("number should be greater than 0")
else:
	 divisors = divisors(n)
	 divisors += (n,)
	 print('The divisors of', n, 'is',divisors)
'''

def divisors(n):
	if n==1:
		divisors = (1,)
		return divisors
	else:
		divisors = (1,)
		for i in range(2, n//2 + 1):
			if n % i == 0:
				divisors += (i,)
		return divisors


n = int(input('please enter a number:'))
if n<=0:
	print("number should be greater than 0")
else:
	 divisors = divisors(n)
	 divisors += (n,)
	 print('The divisors of', n, 'is',divisors)

