'''
psuedocode

sum = 0   data initialization

for x from 1 to 10000
    if (x mod 3 == 0) and  (x mod 5 == 0)
        sum = sum + x

print the outcome sum
'''

sum=0

for x in range(1,10000):
    if x%3==0 or x%5==0:
        sum=sum+x
print(sum)
