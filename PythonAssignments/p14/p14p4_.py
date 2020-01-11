for number in range (2, 20):
    for i in range(2, number):
        if number % i != 0:
            print(number, "is a prime number")
            break
        else:
            for p in range(2, number):
                if number % p == 0:
                    print(number, 'equals', p, '*', number//p)
            break
print("finished!")
