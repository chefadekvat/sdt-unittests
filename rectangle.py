import unittest

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

class RectangleTestCase(unittest.TestCase):
    def test_area_extreme(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(32, 45), 1440)
        self.assertEqual(area(238433, 12312), 2935587096)
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(1, 1), 1)
        self.assertEqual(area(1, 0), 0)
        self.assertEqual(area(0, 1), 0)

    def test_perimeter_extreme(self):
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(30, 30), 120)
        self.assertEqual(perimeter(1, 1), 4)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(1, 0), 2)
        self.assertEqual(perimeter(2349823442398, 345834579889), 5391316044574)

    def test_area_invalid(self):
        self.assertEqual(area(-1, 2), 0)
        self.assertEqual(area(0, -30), 0)
        self.assertEqual(area(-30, -30), 0)
        self.assertEqual(area(2, -2), 0)
        self.assertEqual(area(3, -1), 0)
        self.assertEqual(area(-1, -1), 0)
    
    def test_perimeter_invalid(self):
        self.assertEqual(perimeter(-1, 2), 0)
        self.assertEqual(perimeter(0, -30), 0)
        self.assertEqual(perimeter(-30, -30), 0)
        self.assertEqual(perimeter(2, -2), 0)
        self.assertEqual(perimeter(3, -1), 0)
        self.assertEqual(perimeter(-1, -1), 0)