import SortingAlgorithm

import collections

class MergeSort(SortingAlgorithm.SortingAlgorithm):
    """
    A class that implements the mergesort algorithm.
    """

    def _merge(self, l: collections.abc.Iterable[int], r: collections.abc.Iterable[int]) -> collections.abc.Iterable[int]:
        """
        Merges two sorted iterables.

        :param l: The left iterable.
        :param r: The right iterable.
        :return: A merge of the left and right iterables, with elements maintaining their sorted order.
        """
        l_iter: collections.abc.Iterator[int] = iter(l or [])
        r_iter: collections.abc.Iterator[int] = iter(r or [])
        l_next: int|None = next(l_iter, None)
        r_next: int|None = next(r_iter, None)

        # Forward elements from both iterables until one is exhausted.
        while l_next is not None and r_next is not None:
            # Choose to forward elements from either the left or right iterable depending on which is smaller.
            if self.compare(l_next, r_next):
                yield l_next
                l_next = next(l_iter, None)
            else:
                yield r_next
                r_next = next(r_iter, None)
        # Forward all remaining elements from the iterable that we have not exhausted.
        if l_next is None:
            while r_next is not None:
                yield r_next
                r_next = next(r_iter, None)
        elif r_next is None:
            while l_next is not None:
                yield l_next
                l_next = next(l_iter, None)

    def sort(self, a: collections.abc.MutableSequence[int]) -> collections.abc.Sequence[int]:
        # Transform the sequence into the format in which it will be processed: a two-dimensional, jagged list.
        a: list[collections.abc.Iterable[int]] = [[number] for number in a]
        # Sort the two-dimensional iterable. We are done when only one iterable is left.
        while len(a) > 1:
            # Pad the list to a multiple of 2 so that we can grab pairs.
            # If this ends up being the odd one out, then it is discarded anyway
            a.append([])
            # Merge every pair of elements
            a = [self._merge(l, r) for l, r in zip(a[::2], a[1::2])]
        # Unpack and return the result
        return list(a[0])