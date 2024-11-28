import math

def area(r):
    '''Принимает число r - радиус круга, возвращает площадь круга'''
    if r < 0:
        return 0
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r - радиус круга, возвращает периметр круга'''
    if r < 0:
        return 0
    return 2 * math.pi * r

