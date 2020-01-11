'''
Psuedocode

  if input number equal to the stored password print You have successfully logged in.
    else
        let the user input his password again
        if password is correct then print three [times
        if the three times are all correct then you have successfully logged in
        else print you have been denied access.

'''

count=0
password = '11'

x=(input('Please enter your password'))
if x==password:
    print('You have successfully logged in.')
else:
    #give x a null value to recount x 
    x='' 
    while count<3:
        y=input('Enter the passwod for three times:')
        count +=1
        x += y

if x == password*3:
    print('You have successfully logged in.')
    
    
elif x!=password:
    print('You have been denied accedd')

    

    
    
