
'''
pseudocode

pseudocode

Prompt the user for an integer as n
while x>=0 do
    sum_ = 0
    for every integer between 1 and n
        sum_ += i
    print(sum_)
    break

'''

x = int(input("Please input your number:"))

while(x>=0):
    sum_=0
    for i in range(1, x+1):
        sum_ +=i
    print(sum_)
    x = int(input("Please input your number:"))



   


    

    

