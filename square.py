import unittest

def area(a):
    '''Принимает число a - сторону квадрата, возвращает площадь квадрата'''
    if a < 0:
        return 0
    return a * a


def perimeter(a):
    '''Принимает число a - сторону квадрата, возвращает периметр квадрата'''
    if a < 0:
        return 0
    return 4 * a

class SquareTestCase(unittest.TestCase):   
    def test_area_extreme(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(1000000), 1000000000000)

    def test_area_invalid(self):
        self.assertEqual(area(-1), 0)
        self.assertEqual(area(-32), 0)
        self.assertEqual(area(-123), 0)
        self.assertEqual(area(-43), 0)
        self.assertEqual(area(-100), 0)

    def test_perimeter_extreme(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(1000000), 4000000)

    def test_perimeter_invalid(self):
        self.assertEqual(perimeter(-1), 0)
        self.assertEqual(perimeter(-32), 0)
        self.assertEqual(perimeter(-123), 0)
        self.assertEqual(perimeter(-43), 0)
        self.assertEqual(perimeter(-100), 0)