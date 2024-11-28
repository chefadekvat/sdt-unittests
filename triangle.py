import unittest

def area(a, h):
    '''Принимает числа a, h - основание и высоту треугольника, возвращает площадь треугольника'''
    if a < 0 or h <= 0:
        return 0
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает числа a, b, c - стороны треугольника, возвращает периметр треугольника'''
    if a < 0 or b < 0 or c < 0:
        return 0
    elif a >= b + c or b >= a + c or c >= a + b:
        return 0
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_extreme(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(1000000, 2000000), 1000000000000)

    def test_perimeter_extreme(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(1000000, 1000000, 1000000), 3000000)
    
    def test_area_invalid(self):
        self.assertEqual(area(-1, 2), 0)
        self.assertEqual(area(1, -2), 0)
        self.assertEqual(area(1, -22), 0)
        self.assertEqual(area(-1, 3), 0)
        self.assertEqual(area(-1, -3), 0)
        self.assertEqual(area(1, 0), 0)
        self.assertEqual(area(1123423423, 0), 0)

    def test_perimeter_invalid(self):
        self.assertEqual(perimeter(-1, 2, 3), 0)
        self.assertEqual(perimeter(1, -2, 3), 0)
        self.assertEqual(perimeter(1, 2, -3), 0)
        self.assertEqual(perimeter(-1, -2, 3), 0)
        self.assertEqual(perimeter(-1, 2, -3), 0)
        self.assertEqual(perimeter(1, 2, 3), 0)