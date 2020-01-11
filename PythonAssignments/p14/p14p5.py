
'''

function fib(n):
    if (n = 0):
        output 'fib(0) == 0'
        return 0
    elif (n = 1):
        output 'fib(1) <- 1'
        return 1
    else:
        print('Calculate the Fibonacci Serise of', n)
        t = fib(n-1)+fib(n-2)
        return t
let the user input a number
while n>=0:
    print("The number of terms from the Fibonacci Serise is:", fib(n))
    n = int(input("please enter a number:"))
print("finished")

'''
def fib(n):
    #calculate the nth of Fibonacci number.
    if n == 0:
        print('Calculate the Fibonacci Serise of', n)
        return 0
    elif n == 1:
        print('Calculate the Fibonacci Serise of', n)
        return 1
    else:
        print('Calculate the Fibonacci Serise of', n)
        t = fib(n-1)+fib(n-2)
        return t
    
n = int(input("please enter a number:"))
while n>=0:
    print("The number of terms from the Fibonacci Serise is:", fib(n))
    n = int(input("please enter a number:"))
    

