
'''
function base(decimal ,base) :
    list = "0123456789ABCDEF"
    other_base = ""
    while decimal != 0 :
        other_base = list[decimal % base] + other_base
        decimal    = decimal // base
    return other_bases

n = int(input("please enter a number: "))
b = int(input("please enter a base: "))
print("the number of", n, "in base", b, "is", base(n, b))

'''
def base(decimal ,base) :
    list = "0123456789ABCDEF"
    other_base = ""
    while decimal != 0 :
        other_base = list[decimal % base] + other_base
        decimal    = decimal // base
    return other_base




n = int(input("please enter a number: "))
b = int(input("please enter a base: "))
print("the number of", n, "in base", b, "is", base(n, b))
