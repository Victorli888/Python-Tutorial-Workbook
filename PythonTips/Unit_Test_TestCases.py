import unittest

from Unit_Test_Tutorial import calculator
"""
Every function that starts with test will run automatically
"""


class NameTestCase(unittest.TestCase):
    # IMPORTANT NOTE: each test case needs to start with test_xxxxx  test_ signals that this is a test case
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


suite = unittest.TestLoader().loadTestsFromTestCase(NameTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
