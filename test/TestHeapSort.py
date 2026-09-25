################################################
# Coding Cadets                                #
# Thaddeus Schelp, Todd Dharni, Brayden Graham #
# CS2430                                       #
# Programming Project 1                        #
# Primary Author: Thaddeus Schelp              #
################################################

import unittest

import HeapSort
import Constants


class TestHeapSort(unittest.TestCase):
    def test_already_sorted(self):
        merge: HeapSort.HeapSort = HeapSort.HeapSort()
        self.assertEqual(merge.sort(Constants.TEST_CASE_ALREADY_SORTED), Constants.SOLUTION)
        self.assertGreater(merge._comparison_count, 0)

    def test_reverse_sorted(self):
        merge: HeapSort.HeapSort = HeapSort.HeapSort()
        self.assertEqual(merge.sort(Constants.TEST_CASE_REVERSE_SORTED), Constants.SOLUTION)
        self.assertGreater(merge._comparison_count, 0)

    def test_normal_case(self):
        merge: HeapSort.HeapSort = HeapSort.HeapSort()
        self.assertEqual(merge.sort(Constants.TEST_CASE_NORMAL), Constants.SOLUTION)
        self.assertGreater(merge._comparison_count, 0)


if __name__ == "__main__":
    unittest.main()
