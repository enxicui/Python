'''
def fib(x)
fib1 = 0
fib2 = 1
i=2
if x == 1:
     print("Series is", ',', fib1, ',', fib2, sep = "")
else:
    print("Series is", fib1, ', ', fib2, sep = "", end = "")
    a,b=fib1, fib2
    while i < x:
        a, b= b, a+b
        print(",", b, end="")
        i +=1
    print()
prompt the user for an integer x
if x<0 : 
   print("Error, the number should be a non-negative integer")
elif x==0:
   print("Series of is 0")
else:
   fib(x)


'''
#1
def fib(x):
    fib1 = 0
    fib2 = 1
    i = 2
    if x == 1:
        print("Series is", ',', fib1, ',', fib2, sep = "")
    else:
        print("Series is", fib1, ', ', fib2, sep = "", end = "")
        a,b=fib1, fib2
        while i < x:
            a, b= b, a+b
            print(",", b, end="")
            i +=1
    print()
        

#2
x=int(input("plwase enter a non-negative integer"))
if x<0 : 
   print("Error, the number should be a non-negative integer")
elif x==0:
   print("Series of is 0")
else:
   fib(x)

