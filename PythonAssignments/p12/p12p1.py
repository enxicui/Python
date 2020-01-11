'''
give x a function
    factorial=1
    for i in range(1, x+1):
        fac=fac*i
    return fac
give a number x
if x==0:
    print fac
elif x<0:
    error
else:
    print the fac
 

'''
#1
def fac(x):
    fac=1
    for i in range(1, x+1):
        fac *=i
    return fac
#2
x=int(input("Please enter a non-negative number"))
if x < 0:
    print("Error, the number should be a non-negative number")
else:
    print("The factorial of", x, "is", fac(x))

