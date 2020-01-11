'''
  {  while true
  number= input number;
          
		if x mod 2 == 0 and x >o
			print(x is divisble by 2)
		if x mod 3 == 0 and x>0
			print(x is divisble by 3)
		if x mod 5 == 0 and x>0
			print(x is divisble by 5)
		if x mod 7 == 0 and x>0
			print(x is divisble by 7)
		 break

		if x <0
		print"finished"
		break
	}
'''
number=int(input('Please enter a number', ))

while number>=0:
    
    if number%2==0 and number>=0:
        print('this number is divisible by 2')
    if number%3==0 and number>=0:
        print('this number is divisible by 3')
    if number%5==0 and number>=0:
        print('this number is divisible by 5')
    if number%7==0 and number>=0:
        print('this number is divisible by 7')
    number=int(input('Please enter a number', ))
    
