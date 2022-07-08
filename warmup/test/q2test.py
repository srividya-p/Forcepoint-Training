import sys
sys.path.insert(0, '../code')

import unittest
from q2 import numberOfOccurences

class ArrFrequencyTestCase(unittest.TestCase):

    def test_arr_frequency(self):
        self.assertEqual(numberOfOccurences([3, 2, 1, 3, 2, 4, 5]), {3: 2, 2: 2, 1: 1, 4: 1, 5: 1})
        self.assertEqual(numberOfOccurences([1, 1, 1, 1, 1, 100, 100, 2, 2]), {1: 5, 100: 2, 2: 2})
        self.assertEqual(numberOfOccurences([2]), {2: 1})
        self.assertEqual(numberOfOccurences([0, 0, 0, 0, 0, 0, 0]), {0: 7})
         
if __name__ == "__main__":
    unittest.main()