import unittest
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

class CircleTestCase(unittest.TestCase):
    def test_area_extreme(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), math.pi)
        self.assertEqual(area(10), 100 * math.pi)
        self.assertEqual(area(32), 1024 * math.pi)
        self.assertEqual(area(238433), math.pi * (238433 ** 2))

    def test_perimeter_extreme(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 2 * math.pi)
        self.assertEqual(perimeter(10), 20 * math.pi)
        self.assertEqual(perimeter(30), 60 * math.pi)
        self.assertEqual(perimeter(2349823442398), 2 * math.pi * 2349823442398)

    def test_area_invalid(self):
        self.assertEqual(area(-1), 0)
        self.assertEqual(area(-10), 0)
        self.assertEqual(area(-321), 0)
        self.assertEqual(area(-123), 0)

    def test_perimeter_invalid(self):
        self.assertEqual(perimeter(-1), 0)
        self.assertEqual(perimeter(-10), 0)
        self.assertEqual(perimeter(-321), 0)
        self.assertEqual(perimeter(-123), 0)