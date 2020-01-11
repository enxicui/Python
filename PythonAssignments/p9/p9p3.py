

'''
pseudocode

Prompt the user for an integer as x
if x==0:
    fa==1
elif:
    fa==1
elif x<0:
    fac = 1
for every integer between 1 and x
    fa = fa * i
print(fa)

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
    for i in range(1, x+1):
        fa=fa*i
print('factorial of', x, 'is', fa)

