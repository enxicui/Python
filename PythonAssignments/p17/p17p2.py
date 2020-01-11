'''
give a funtion common(num1, num2):
	num = min(num1, num2)
	if num1 == 1 or num2 == 1:
		return (1,)
	else:	
		divisor=(1,)
		for i between 2 and num//2 + 1):
			if num1 % i ==0 and num2 % i ==0:
				divisor += (i,)
	
	if max(num1, num2)%num == 0:
		divisor +=(num,)
	return divisor

num1 = int(input("please enter a number : "))
num2 = int(input("please enter another number : "))
outcome = common(num1, num2)

print(outcome)

'''

def common(num1, num2):
	num = min(num1, num2)
	if num1 == 1 or num2 == 1:
		return (1,)
	else:	
		divisor=(1,)
		for i in range(2, num//2 + 1):
			if num1 % i ==0 and num2 % i ==0:
				divisor += (i,)
	
	if max(num1, num2)%num == 0:
		divisor +=(num,)
	return divisor

num1 = int(input("please enter a number : "))
num2 = int(input("please enter another number : "))
outcome = common(num1, num2)

print(outcome)


