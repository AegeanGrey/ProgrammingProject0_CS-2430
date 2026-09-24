###################################
# Coding Cadets                   #
# Thaddeus Schelp, Todd Dharni    #
# CS2430                          #
# Programming Project 1           #
# Primary Author: Todd Dharni     #
###################################

"""
    Quicksort divides and conquers
    Selects an element as a pivot and partitions
    the given array around the picked pivot
    by placing the pivot in its correct position in
    the sorted array
"""

# Create a pivot point
# Hoare's Partition
# (consider the first element in a list as the pivot)

# Initialise two pointers (i and j)
# [i targets the start of array]
# [j targets the end of array]

# Move i to the right until an element >= currentPivot
# Move j to the left until an element <= currentPivot

# If i points to an element >= currentPivot and
#    j points to an element <= currentPivot

#    then swap them

#    repeat the process, moving i and j toward
#    each other until they meet or cross

#    when pointers cross, the partition is complete;
#    with elements <= pivot on the left and
#         elements >= pivot on the right

import SortingAlgorithm
import collections

# class for QuickSort to be used in main.py
class QuickSort(SortingAlgorithm.SortingAlgorithm):

    def sort(self, a: collections.abc.MutableSequence[int]) -> collections.abc.Sequence[int]:

        # totalNums = 8
        totalNums = len(a)

        # quickSort function call to pass through the following
        # -----------------------------------------------------
        # array : arrayOfNums
        # start : 0
        #  end  : totalNums - 1 (7)
        self._quickSort(a, 0, totalNums - 1)

        # return the final value for the quick sorted array
        return a

    # quickSort function that will take in a numbered array, start and end point
    # --------------------------------------------------------------------------
    # array: expects an array of nums
    # start: expects an int
    #  end : expects an int
    def _quickSort(self, array, start, end):

        # Base Case
        # ---------
        # if end point is less than start then stop the recursive function
        if end <= start:
            return

        # Location of where we pivot (pivot begins at the end of array)
        pivot = self._partition(array, start, end)

        left = pivot - 1
        right = pivot + 1

        # recursive calls to the quickSort method that utilizes pivot between partitions
        self._quickSort(array, start, left)
        self._quickSort(array, right, end)

    # partition function that will take in a numbered array, start and end point
    # --------------------------------------------------------------------------
    # array : expects an array of nums
    # start : expects an int
    #  end  : expects an int
    def _partition(self, array, start, end):

        # sets the pivot point to the end of the array of the given partition
        pivot = array[end]

        # sets i to the first positioning before the start of the partitioned array
        i = start - 1

        # for loop of j that's in range between start and end + 1 of the range for the partitioned array
        for j in range(start, end + 1):

            # sees if num of index j in array is less than pivot point with self.compare()
            if self.compareLeast(array[j], pivot):

                # if so, increment i by 1
                i += 1

                # update temp to the current index of i in the given array
                temp = array[i]

                # update the indexed value of i in the array to the indexed value of j in the array
                array[i] = array[j]

                # update the indexed value of j in the array to the current temp value
                array[j] = temp

        # continue by incrementing i by 1
        i += 1

        # update the value for temp to the indexed value of i in the given array
        temp = array[i]

        # update the indexed value of i in the array to the indexed value of end in the array
        array[i] = array[end]

        # update the indexed value of end in the array to the current temp value
        array[end] = temp

        # return the current value of i
        return i
