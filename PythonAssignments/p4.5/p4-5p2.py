import math


while True:
    length=float(input('enter your length:'))
    if length >= 0:
        radius=length/2
        area=length**2
        volume=length**3
        area_circle=math.pi*radius**2
        volume_sphere=4/3*math.pi*radius**3
        volume_cylinder=math.pi*radius**2*length
        print('area=',length**2)
        print('volume=',length**3)
        print('area of a circle=',math.pi*radius**2)
        print('volume of a sphere=',4/3*math.pi*radius**3)
        print('volume of a cylinder=',math.pi*radius**2*length)
    else:
        print('Length must be >= 0. Please try again.') 
        break
    
