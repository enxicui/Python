
'''
Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""
    '''
#to check whether a tring is a palindromes
def isPalindrome(s):
    """Checks whether the string s is a palindrome """
    def toChars(s):
        """Converts a string to lowercase and removes non-letters """
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring
    def isPal(s):
        """Checks whether the string s is a palindrome"""
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
str = input('Enter a string (enpty string to exit): ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    break
print('Finished!')
