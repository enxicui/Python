while True:
    amount=float(input('please enter your amount', ))
    tax_larger=amount * 0.6 * 0.135
    tax_smaller=amount * 0.4 * 0.23
    total =amount + tax_larger + tax_smaller
    if amount >= 0:
        print('total amount=',total)
    else:
        print('Amount of income must be >= 0. Please try again.')
        break
