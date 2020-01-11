'''
give f(n) a definition
    if n == 1:
        return 2
    elif n > 1:
        return n+f(n-1)
prompt the user input a number
for i in range (1, n+1)
    print( f(i)
'''
def f(n):
    #Take n as input and calculate nth value and print it and return 
    if n == 1:
        return 2
    elif n > 1:
        return n + f(n-1)
   
while True:
    n = int(input("Please enter a positive number:" ))
    if n>=1:
        for i in range (1, n+1):
            print( f(i),end=" ")
        print()
    if n<1:
        print("finished")
        break
        
        
    
    
 
