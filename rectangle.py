def area(a, b):
    '''Принимает числа a, b - стороны прямоугольника, возвращает площадь прямоугольника'''
    if a < 0 or b < 0:
        return 0
    return a * b


def perimeter(a, b):
    '''Принимает числа a, b - стороны прямоугольника, возвращает периметр прямоугольника'''
    if a < 0 or b < 0:
        return 0
    return (a + b) * 2
