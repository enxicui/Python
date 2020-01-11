 #to check whether a tring is a palindromes
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring
    def isPal(s):
        print ('isPal function called with argument', s)
        if len(s) <= 1:
            return True
        else:
            result = s[0] == s[-1] and isPal(s[1:-1])
            print ('About to return result', result, 'from isPal with argument', s)
            return result
        return isPal(toChars(s))
str = input('Enter a string (enpty string to exit): ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    break
print('Finished!')

                
