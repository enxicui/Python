
'''
Psuedocode

    if input number equal to the stored password print You have successfully logged in.
    else
        let the user input his password again
        if password is correct then print you have successfully logged in
        else
            let the user input his password again
            if password is correct then print you have successfully logged in
            else print you have been denied access.
'''

count=0
while count<3:
    password='098765'
    x=(input('Please enter your password',))
    if(x==password):
        print('You have successfully logged in.')
        break
    else:
        count +=1
        '''print('Please try again')'''
if count>=3:
    print('You have been denied access.')
