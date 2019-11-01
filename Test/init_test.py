"""This is a test file for __init__"""

import unittest
import Lambdata_rileydata as lr

class BasicMathTests(unittest.TestCase):
    """This is a test fot the incrment_1 function"""
    def test_incrment(self):
        self.assertEqual(lr.incrment_1(lr.TEST_VAR), 3)

    """This is a test fot the incrment_1 function"""
    def test_2x(self):
        self.assertEqual(lr.mult2(lr.TEST_VAR), 18)

if __name__ == '__main__':
    unittest.main()

