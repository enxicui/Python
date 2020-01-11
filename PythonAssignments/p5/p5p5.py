x=input ('Please enter towns or cities')
if (x=='Dublin' or x=='Kilkenny'):
    print(x+' is in Leinster')
elif(x=='Belfast' or x=='Derry' or x=='Lisburn'):
    print(x +' is in Ulster')
elif(x=='Cork' or x=='Limerick' or x=='Waterford'):
    print(x +' is in Munster')
elif(x=='Galway' or x=='Sligo'):
    print(x +' is in Connacht')
else:
    print("Sorry, I didn't recognise that name")
