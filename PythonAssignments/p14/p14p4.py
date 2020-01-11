'''


for number in range(2, 20):
    prime = True;
    for i in range(2, number):
        if number % i = 0:
            output number, 'equals', i, '*', number//i
            flag = False;
        endif
    endfor
    if (prime):
        output number, 'is a prime number'
    endif
endfor
output 'Finished!'

'''
for number in range (2, 20):
    #prime is to mark whether a number is a prime number
    prime = True;
    for i in range(2, number):
        if number % i== 0:
            print(number, 'equals', i, '*', number//i)
            # if current number is not prime number, then mark flag false
            prime = False;
    if prime:
        print(number, "is a prime number")               
        print()
   
        #print('Finished!')
