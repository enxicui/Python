'''
psuedocode

if (year is not exactly divisible by 4) then (it is a common year)
else
if (year is not exactly divisible by 100) then (it is a leap year)
else
if (year is not exactly divisible by 400) then (it is a common year)
else (it is a leap year)
'''
year = int(input('please input a year'))

if year % 4 != 0:
    print('it is a common year')
else:
    if year % 100 != 0:
        print('it is a leap year')
    else:
        if year % 400 !=0:
            print('it is a common year')
        else:
            print('it is a leap year')
