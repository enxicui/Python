
'''
function findDivisors(num1, num2)
    initialise divisors
    for i from 1 to minmum(num1, num2) do
        if num1 mod i == 0 and num2 mod i == 0 then
            add i to divisors
        return divisors
'''
def finddivisors(num1, num2):
    #Finds the common divisors of num1 and num2
    divisors = ()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

num1 = int(input("please enter a number:"))
num2 = int(input("please enter another number:"))

if num1 <= 0 and num2 <= 0:
    print("this number should  grater than 0")
    
# First of all, get the common divisors and print them out
else:
    divisors= finddivisors(num1, num2)
    print('The common divisors of', num1, 'and', num2, 'are:', divisors)
# Now sum them and print the total
    total = 0
    for d in divisors:
        total += d
    print('Sum of the common divisors is:', total)
print('Finished!')
