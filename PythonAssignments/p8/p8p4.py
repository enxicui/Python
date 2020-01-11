'''
sum1 equal to 0
sum2 equal to 0sum3=0
sum4 equal to 0
sum5 equal to 0
sum6 equal to 0
sum7 equal to 0
while True:
    number=int(input('Please enter a number', ))
    if number==0:
        print('this number is equal to 0')
#count the times
        sum1 +=1
    if number>0 and number<=20:
        print('this number is greater than 0 and less than or equal to 20')
        sum2 +=1
    if number>20 and number<=40:
        print('this number is greater than 20 and less than or equal to 40')
        sum3 +=1
    if number>40 and number<=60:
        print('this number is greater than 40 and less than or equal to 60')
        sum4 +=1
    if number>60 and number<=80:
        print('this number is greater than 60 and less than or equal to 80')
        sum5 +=1
    if number>80 and number<=100:
        print('this number is greater than 80 and less than or equal to 100')
        sum6 +=1
    if number>100:
        print('this number is greater than 100')
        sum7 +=1
    if number<0:
        print('the count equal 0 is', sum1)
        print('the count between 0 and 20 is', sum2)
        print('the count between 20 and 40 is', sum3)
        print('the count between 40 and 60 is', sum4)
        print('the count between 60 and 80 is', sum5)
        print('the count between 80 and 100 is', sum6)
        print('the count greater than is,', sum7)
        break
'''
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
while True:
    number=int(input('Please enter a number', ))
    if number==0:
        print('this number is equal to 0')
        sum1 +=1
    if number>0 and number<=20:
        print('this number is greater than 0 and less than or equal to 20')
        sum2 +=1
    if number>20 and number<=40:
        print('this number is greater than 20 and less than or equal to 40')
        sum3 +=1
    if number>40 and number<=60:
        print('this number is greater than 40 and less than or equal to 60')
        sum4 +=1
    if number>60 and number<=80:
        print('this number is greater than 60 and less than or equal to 80')
        sum5 +=1
    if number>80 and number<=100:
        print('this number is greater than 80 and less than or equal to 100')
        sum6 +=1
    if number>100:
        print('this number is greater than 100')
        sum7 +=1
    if number<0:
        print('the count equal 0 is', sum1)
        print('the count between 0 and 20 is', sum2)
        print('the count between 20 and 40 is', sum3)
        print('the count between 40 and 60 is', sum4)
        print('the count between 60 and 80 is', sum5)
        print('the count between 80 and 100 is', sum6)
        print('the count greater than is,', sum7)
        break
