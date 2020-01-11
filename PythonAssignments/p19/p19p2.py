'''
function trans(number, base):
    a <- '0123456789ABCDEF'
    number <- number.upper(); outcome <- 0; k=0
    for i in range(len(number)-1, -1, -1):
        outcome += a.find(number[i]) * base ** (k)
        k <- k + 1
    
    return outcome


num <- prompt the user a string
base <- prompt the user an integer
trans(num,base)
'''

def trans(number, base):
    
    #The function is to transfer a 'base' base number to decimal numbver

    a = '0123456789ABCDEF'
    number = number.upper()
    outcome = 0
    k=0
    for i in range(len(number)-1, -1, -1):
        outcome += a.find(number[i]) * base ** (k)
        k = k + 1
    return outcome 

num = input('Please enter a number:\n')
base = int(input('Please enter the base: \n'))
print('The outcome is:',trans(num,base))
