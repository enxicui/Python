'''
enter a number named x
if x lees than 0, then erroe
else:
  i in range(1, x+1)
   fact= i*facy
   print(x's factorial is fact
'''
fact=1
x=int(input("please enter a number"))
if x<0:
    print("Error, please enter a number greater than 0")
else:
    for i in range(1, x+1):
        fact *=i
    print("thr factorial of",x, "is", fact)
    
