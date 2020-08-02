import unittest

from Unit_Test_Tutorial import calculator
"""
Every function that starts with test will run automatically
"""


class NameTestCase(unittest.TestCase):

    def test_m1(self):
        result = calculator(5, "*", 5)
        self.assertEqual(result, 25)

    def test_m2(self):
        result = calculator(23, "*", 0)
        self.assertEqual(result, 0)

    def test_d2(self):
        result = calculator(10, "/", 0)
        self.assertEqual(result, "Can't Divide by Zero.")

    def test_d1(self):
        result = calculator(10, "/", 10)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
else:
    print("test has been loaded")
