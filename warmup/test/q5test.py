import sys
sys.path.insert(0, '../code')

import unittest
from q5 import get5thPowSum

class FifthPowSumTestCase(unittest.TestCase):

    def test_5th_pow_sum(self):
        self.assertEqual(get5thPowSum(), 443839) 
        
if __name__ == "__main__":
    unittest.main()