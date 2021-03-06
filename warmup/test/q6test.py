import sys
sys.path.insert(0, '../code')

import unittest
from q6 import mostFrequent

class MostFrequentNumTestCase(unittest.TestCase):

    def test_most_frequent(self):
        self.assertEqual(mostFrequent([1, 2, 3, 3, 3, 4, 2, 5, 1]), 3) 
        self.assertEqual(mostFrequent([1, 1, 1, 1, 1, 1]), 1)
        self.assertTrue(mostFrequent([2, 2, 2, 3, 3, 3]) == 2  or mostFrequent([2, 2, 2, 3, 3, 3]) == 3) 
        
if __name__ == "__main__":
    unittest.main()