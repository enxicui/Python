'''
input a integer nunber x
i=0
    if x is greater than or equal to 0
        while i<=x:
            for i in range(1, x+1)
                if and check if i**2=x
                The number's sqaure root is i
                break
    if i**2>x or i**2<x:
            print('This number is not a perfect square')
if x<0
    exit the peogram




'''
x= int(input("please input a number for you to calculate the square root:"))
i=0
if x>=0:
    for i in range(1, x+1):
        if i**2==x:
            print("The number's sqaure root is:",i)
            break
    if i**2>x or i**2<x:
            print('This number is not a perfect square')
if x<0:
    print('Finished!')
