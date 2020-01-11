'''
Psuedocode
1. let the user input the first, second and the third number
2. set maxium equal to minus  infinity
3. if none of three number are odd  then print None of them is odd!
    else
    if x is odd and a is greater than record maxium then let maxium eqaul = a
    if y is odd and b is greater than record maxium then let maxium eqaul = b
    if z is odd and a is greater than record maxium then let maxium eqaul = c
    Then the maxium has recorded the max odd number, just print it out.
'''

x=int(input('Please enter the first numbel.r'))
y=int(input('Please enter the second number'))
z=int(input('Please enter the third number'))
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('None of the three number is odd')
number_largest = 0
if x % 2!=0:
    number_largest =x
if y % 2!=0:
    if y>number_largest:
        number_largest=y
if z % 2!=0:
    if z>number_largest:
        number_largest=z
        print('The largest number is:', number_largest)
        

                
