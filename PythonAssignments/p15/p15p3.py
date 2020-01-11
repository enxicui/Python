'''


give f(n) a definition
    if n == 0:
        return 13
    elif n == 1:
        return 8
    elif n > 1:
        return f(n-2) + 13 * f(n-1)

while True:
   prompt the user input a number
    if n >= 0:
        for i in range (0, n+1):
            print("f(n) is :", f(i), end=" ")
            print()
    elif n < 0:
        print("finished!")
        break
        
'''

def f(n):
    #Take n as input and calculate nth value and print it and return 
    if n == 0:
        return 13
    elif n == 1:
        return 8
    elif n > 1:
        return f(n-2) + 13 * f(n-1)

while True:
    n = int(input("please enter a number:"))
    if n >= 0:
        for i in range (0, n+1):
            print("f(n) is :", f(i), end=" ")
            print()
    elif n < 0:
        print("finished!")
        break
        
