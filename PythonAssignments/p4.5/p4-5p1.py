euro_CNY_conversion = 8.10

while True:
    euro_amount = float(input('enter the amount of euro',))
    if euro_amount >= 0:   
        print('amount in euro:',euro_CNY_conversion*euro_amount)
    else:
        print('amount must be >= 0. Please try again.')
        break
