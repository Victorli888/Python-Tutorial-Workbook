"Uses this test suite to test HR_Kangaroo Solution"
import unittest

from HR_Kangaroo import kangaroo


class Jump(unittest.TestCase):

    def test_Yes_1(self):
        result = kangaroo(0, 3, 4, 2)
        self.assertEqual(result, "YES")

    def test_No_1(self):
        result = kangaroo(0, 2, 5, 3)
        self.assertEqual(result, "NO")


suite = unittest.TestLoader().loadTestsFromTestCase(Jump)
unittest.TextTestRunner(verbosity=2).run(suite)
