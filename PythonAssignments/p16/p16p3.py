'''
function totalfactors(x):
    fac = 0
    for i between 1, x
        if x % i == 0:
            fac +=i:
    return fac

n == input a number
for i in range(1, x+1):
    if totalfactors(j) == j:
        print(j)
    endif
else finished
'''
#find the factors of number x 
def totalfactors(x):
    fac=0
    for i in range(1, x):
        if x % i == 0:
            fac +=i
            
    return fac


x = int(input("please enter a number:"))

for j in range(1, x+1):
    if totalfactors(j) == j:
        print('The perfect number is: ', j)

else:
    print("finished!")
    
    
