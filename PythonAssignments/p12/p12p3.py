'''
def squ(num)
epsilon = 0.01
step = epsilon ** 2

number = float(input(’Enter the number for which you wish
                       to calculate the square root:  ’))
root = 0.0
while abs(number - root ** 2) >= epsilon and root <= number:
    root += step
if abs(number - root ** 2) < epsilon:
    print(’The approximate square root of’, number, ’is’, root)
    return root
    prompts the user for a floating-point number
if num>=0:
    print squ
else:
    print(’Failed to find a square root of’, number)

'''
def squ(num):
    epsilon = 0.01
    step = epsilon**2
    
    root=0.0s
    while abs(num-root**2)>= epsilon and root<=num:
        root +=step
    if abs(num-root**2)<epsilon:
        print("THe approximate square root of", num, "is", root)
    return root

num=float(input("enter the number for which you wish to calculate the square root:"))
if num>=0:
    epsilon=0.01
    print(squ(num))
else:
    print("Error. You should input a non-negative number.")
