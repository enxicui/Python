
'''
pseudocode

Prompt the user for an integer as x
if x==0:
    fa==1
elif:
    fa==1
elif x<0:
    fac = 1
else:
    fa=1
    i=1
    while i<=x:
        fa *=1
        i +=1
        fa = fa * i
print(fa)

'''
''' 
x=int(input("input a number"))
fact=1
i=1
if x==0 or x==1:
    print("the factorial of x is ", 1)
elif x>1:
    while i<=x:
        fact *=i
        i +=1
    print(fact)
        '''
x=int(input('please enter a number:'))
fa=0
if x==0:
    fa==1
elif x==1:
    fa==1
elif x<0:
    print('sorry, the number must greater than 0')
else:
    fa=1
    i=1
    while i<=x:
        fa *=i
        i +=1
    print('factorial of', x, 'is', fa)


    

    
