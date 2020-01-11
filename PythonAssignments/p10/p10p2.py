'''
input a integer nunber x
i=0
    if x is greater than or equal to 0
        while i<=x:
            for i in range(1, x+1)
                if and check if i**3=x
                    The number's scube root is i
                    break
    if i**3>x or i**3<x:
            print('This number is not a perfect square')
    if x<0
        for i in range (x-1,0):
            if i**3==x:
                print("The number's cube root is:", i)
                break
        if i**3>x or i**3<x:
            print("The number is not a perfect cube")
                
    if x==0:
       this program should exits


'''
while True:
    x= int(input("please input a number for you to calculate the cube root:"))
    i=0
    if x>0:
        for i in range(0, x+1):
            if i**3==x:
                print("The number's cube root is:",i)
                break
        if i**3>x or i**3<x:
            print('This number is not a perfect cube')

    if x<0:
        for i in range(x-1, 0):
            if i**3==x:
                print("The number's cube root is:", i)
                break
        if i**3>x or i**3<x:
            print("The number is not a perfect cube")
                
    if x==0:
        print("finished!")
        break


   
