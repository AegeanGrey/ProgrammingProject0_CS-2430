################################################
# Coding Cadets                                #
# Thaddeus Schelp, Todd Dharni, Brayden Graham #
# CS2430                                       #
# Programming Project 1                        #
# Primary Author: Thaddeus Schelp              #
################################################
import collections

import SortingAlgorithm

class HeapSort(SortingAlgorithm.SortingAlgorithm):
    """
    A class that implements the heapsort algorithm.
    """

    def _heapify(self, a: collections.abc.MutableSequence[int], node: int, unsorted_size: int) -> None:
        """
        Heapifies a subsection of the Sequence.

        :param a: The partially sorted or unsorted Sequence.
        :param node: The node to start the heapification at.
        :param unsorted_size: The size of the unsorted subsection within the a parameter.
        :return: None
        """
        # Go until we hit the bottom of the tree.
        while node < unsorted_size:
            largest: int = node
            left: int = node * 2 + 1
            right: int = left + 1
            # Set largest to the index of the largest value of node, and its left and right children
            if left < unsorted_size and self.compareLeast(a[largest], a[left]):
                largest = left
            if right < unsorted_size and self.compareLeast(a[largest], a[right]):
                largest = right
            # End case: We have
            if largest == node: break
            a[node], a[largest] = a[largest], a[node]
            node = largest


    def sort(self, a: collections.abc.MutableSequence[int]) -> collections.abc.Sequence[int]:
        # Fully heapify all portions of a.
        for i in range(len(a) // 2 - 1, -1, -1):
            self._heapify(a, i, len(a))

        # Progressively heapify the array, selecting the largest element and placing it into the sorted portion of a.
        unsorted_size: int = len(a)
        while unsorted_size > 0:
            self._heapify(a, 0, unsorted_size)
            unsorted_size -= 1
            a[unsorted_size], a[0] = a[0], a[unsorted_size]

        return a
