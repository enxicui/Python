'''
give f(n) a definition
    if n == 1:
        return 1
    elif n > 1:
        return f(n-1) + 2 ** (n-1)
while True:
    prompt the user enter a number n.
    if n>=1:
        for i in range(1, n+1):
            printf(i)
        print()
    if n<1:
        print("finished")
        break     
        
'''

def f(n):
    #Take n as input and calculate nth value and print it and return 
    if n == 1:
        return 1
    elif n > 1:
        return f(n-1) + 2 ** (n-1)


while True:
    n = int(input("Please enter a number: ",))
    if n>=1:
        for i in range(1, n+1):
            print("f(n) is:", f(i), end=" ")
            print()
    if n<1:
        print("finished")
        break
        
        
        

