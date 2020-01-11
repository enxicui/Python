'''
pseudocode
for number between 2 to 20:
    for i in between 2 to number::
        if number % i = 0:
            output number, 'equals', i, '*', number//i
            break
        endif
    else:
        print(number, 'is a prime number')
    end for
endfor
output 'Finished!'
'''
# 
# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers

for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')
print('Finished!')
