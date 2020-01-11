'''
function f(n):
    if n==1:
        output 
        return 2
    elif:
        output 
        return 2 * f(n-1)

n = input a number
while (n >= 1):
    output 'The outcome is:',f(n)
    n <- input a number
endwhile
 Program Exit!s
'''
def f(n):
    #Calculate the f(n) the question requests
    if n == 1:
        p = 2
        print("the number of", n, "is", p)
        return p
    elif n > 1:
        t = 2 * f(n-1)
        print("the number of", n, "is", t)
        return t
n = int(input("please enter a number: "))
while n >= 1:
    print(f(n))
    n = int(input("please enter a number: "))
   
print("Finished!")
