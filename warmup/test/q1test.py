import sys
sys.path.insert(0, '../code')

import unittest
from q1 import reverse

class CharArrReverseTestCase(unittest.TestCase):

    def test_char_arr_rev(self):
        self.assertEqual(reverse(['a', 'b', 'c', 'd', 'e']), ['e', 'd', 'c', 'b', 'a'])
        self.assertEqual(reverse(['a', 'b', 'c', 'd']), ['d', 'c', 'b', 'a'])
        self.assertEqual(reverse(['a']), ['a'])
        self.assertEqual(reverse([]), [])
        
if __name__ == "__main__":
    unittest.main()