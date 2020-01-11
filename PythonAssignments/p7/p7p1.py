'''
presudocode
input a year
if(the year>=0)then
if(the year mod 4=0 and the year mod 100!=0
or the year mod 400=0 )
print(this is leap year)
else( the year is not a leap year)
else tell users this year must be >=0


'''

year=int(input('PLease input your year:'))

if (year >=0):
    if (year % 4==0 and year % 100!=0 or year % 400==0):
        print('The year is a leap year')
    else:
        print('The year is not a leap year')
else:
    print('The year must over 0')
    
