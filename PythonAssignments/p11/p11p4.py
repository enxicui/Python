'''
give x a function
    factorial=1
    for i in range(1, x+1):
        fac=fac*i
    return fac
give a number x
c=1
if x==0:
    print c
elif x>0:
    print the formula
 
'''
def fac_pro(x):
    fac=1
    for i in range(1, x+1):
        fac*=i
    return fac

x=int(input("Give a number: "))
c=1
if x==0:
    print("The number of catalan number is: ",c)
elif x>0:
    print(fac_pro(2*x)/(fac_pro(x+1)*fac_pro(x)))
