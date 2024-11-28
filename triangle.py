def area(a, h):
    '''Принимает числа a, h - основание и высоту треугольника, возвращает площадь треугольника'''
    if a < 0 or h < 0:
        return 0
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает числа a, b, c - стороны треугольника, возвращает периметр треугольника'''
    if a < 0 or b < 0 or c < 0:
        return 0
    elif a >= b + c or b >= a + c or c >= a + c:
        return 0
    return a + b + c
