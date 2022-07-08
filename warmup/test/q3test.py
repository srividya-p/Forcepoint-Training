import sys
sys.path.insert(0, '../code')

import unittest
from q3 import firstSecondMax

MIN_VALUE = -sys.maxsize - 1
MAX_VALUE = sys.maxsize

class ArrFrequencyTestCase(unittest.TestCase):

    def test_arr_frequency(self):
        self.assertEqual(firstSecondMax([3, 2, 4, 5, 1]), [5, 4])
        self.assertEqual(firstSecondMax([8, 8, 8, 8, 8, 8]), [8, None])
        self.assertEqual(firstSecondMax([-2, -3, -2, -1, -1, 0, 0]), [0, -1])
        self.assertEqual(firstSecondMax([MIN_VALUE, MIN_VALUE, MAX_VALUE]), [MAX_VALUE, MIN_VALUE])
             
if __name__ == "__main__":
    unittest.main()