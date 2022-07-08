import sys
sys.path.insert(0, '../code')

import unittest
from q4 import roundOff

MIN_VALUE = -sys.maxsize - 1
MAX_VALUE = sys.maxsize

class ArrFrequencyTestCase(unittest.TestCase):

    def test_arr_frequency(self):
        self.assertEqual(roundOff(5.1), 5) 
        self.assertEqual(roundOff(4.5), 5)
        self.assertEqual(roundOff(3.6), 4)
        self.assertEqual(roundOff(9.9), 10)
       
        
if __name__ == "__main__":
    unittest.main()