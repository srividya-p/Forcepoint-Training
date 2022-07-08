import sys
sys.path.insert(0, '../code')

import unittest
from q5 import get5thPowSum

class ArrFrequencyTestCase(unittest.TestCase):

    def test_arr_frequency(self):
        self.assertEqual(get5thPowSum(), 443839) 
        
if __name__ == "__main__":
    unittest.main()