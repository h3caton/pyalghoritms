import unittest
from merge_sort import (
    Sort
)

class TetsSort(unittest.TestCase):

    def test_init1(self):
        data_in = [11,2,3,7,6,4,8,9,12]
        data_out = [2,3,4,6,7,8,9,11,12]
        self.assertEqual(Sort.sort(array=data_in), data_out)

    def test_init2(self):
        data_in = [2,3,4,6,7,8,9,11,12]
        data_out = [2,3,4,6,7,8,9,11,12]
        self.assertEqual(Sort.sort(array=data_in), data_out)

    def test_init3(self):
        data_in = [1,2,3]
        data_out = [1,2,3]
        self.assertEqual(Sort.sort(array=data_in), data_out)


if __name__ == '__main__':
    unittest.main()
