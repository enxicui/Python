'''


psuedocode

prompt the user for an integer
initialise a=0, b=1, i=2
if (n is less than or equal to 0):
    print error;
     elif x==1
         print0
elif x==2
    print0,1
else:
    while (i less than or equal to x-1)
	    n = a + b
	    a = b
	    b = n,
            print ns
			increase i byonei	
    '''
x = int(input("please enter a number that you want to calculate:"))
a= 0
b= 1
i= 2

if x <= 0:
    print("error, please enter a positive number")
elif x==1:
    print("series is:", 0)
elif x==2:
    print("series is:", 0, 1)
else:
    print(0, 1, end=" ")
    while i<=x-1:
        n=a+b
        a=b
        b=n
        print(n, end=" ")
        i +=1
        
        
        
   
   
    
