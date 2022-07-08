import sys
sys.path.insert(0, '../code')

import unittest
from q7 import intersection

class ArrFrequencyTestCase(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(intersection([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]), [1, 4, 9]) 
        self.assertEqual(intersection([1, 1, 1], [2, 3, 4]), [])
        self.assertEqual(intersection([1, 2, 3, 4], [2, 3, 3, 4, 1]), [1, 2, 3, 4])
        
if __name__ == "__main__":
    unittest.main()