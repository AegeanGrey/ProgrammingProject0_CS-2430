################################################
# Coding Cadets                                #
# Thaddeus Schelp, Todd Dharni, Brayden Graham #
# CS2430                                       #
# Programming Project 1                        #
# Primary Author: Todd Dharni                  #
################################################

import SortingAlgorithm
import collections

class ShakerSort(SortingAlgorithm.SortingAlgorithm):

    """
        sort is the highest function call to pass in the array (a) to plug into
        the shakerSort algorithm which is based off of Shaker / Cocktail Sort.
    """
    def sort(self, a: collections.abc.MutableSequence[int]) -> collections.abc.Sequence[int]:

        # calls the private shakerSort function while passing in the array
        self._shakerSort(a)

        # return the final value for the shaker sorted array
        return a

    """
        shakerSort will take in a given array and navigate from right to left
        sorting one value at a time. It will move the largest given value to
        the right side and then take the smallest given value to the left side
        of the array. 
    """
    def _shakerSort(self, array):

        lengthOfArray = len(array)

        # Counter is used to compare a number to the left or right of itself
        counter = 0

        # Tells when the counter should move from left to right (otherwise right to left)
        forward = True

        # Establishes limits or "walls" the counter should not move past
        left_wall = counter - 1
        right_wall = lengthOfArray

        # checks if left_wall is less than or equal to right_wall
        while left_wall <= right_wall:

            # if we're reading the array from left to right -->
            if forward:

                # compares if the array value to the right is less than
                # the array value to the left ------------- a[0] > a[1]
                if self.compareMost(array[counter], array[counter + 1]):

                    # then swap the places of each value with their current index
                    array[counter], array[counter + 1] = array[counter + 1], array[counter]

                # increment counter --- (moves the reading from left to right)
                counter = counter + 1

                if counter >= lengthOfArray - 1:

                    # Set forward to false so the next run is for reading backwards
                    forward = False

                    # decrement right_wall boundary reference of the array
                    right_wall = right_wall - 1

                    # update counter to begin comparing at the position of the right_wall
                    counter = right_wall

            # if we're reading the array from right to left <--
            elif not forward:

                # compares if the array value to the left is less than the
                # array value to the right : a[leftElement] < a[right_wall]
                if self.compareLeast(array[counter], array[counter - 1]):

                    # then swap the places of each value with their current index
                    array[counter - 1], array[counter] = array[counter], array[counter - 1]

                # decrement counter --- (moves the reading from right to left)
                counter = counter - 1

                # checks for forward pass-off
                if counter <= left_wall:

                    # Set forward to true so the next run is for reading forward
                    forward = True

                    # increment left_wall boundary reference of the array
                    left_wall = left_wall + 1

                    # update counter to begin comparing at the position of the left_wall
                    counter = left_wall
