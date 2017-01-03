import math

def area(base, height):
    return base * height / 2

def perimeter(side1, side2, side3):
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    return perimeter(side1, side2, side3) / 2

def area_hero (side1, side2, side3):
    ''' (number, number, number) -> float

    Return the area of a triangle with sides of length
    side1, side2, and side 3.

    >>> area_hero (3, 4, 5)
    6.0
    '''
    
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area

                     
    
