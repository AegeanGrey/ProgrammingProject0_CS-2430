import abc
import collections

class SortingAlgorithm(abc.ABC):
    """
    An abstract class for sorting algorithms.
    """
    def __init__(self):
        self._comparison_count: int = 0

    def compare(self, a: int, b: int) -> bool:
        """
        Compares a and b and keeps track of the total number of compares.

        :param a: the left argument
        :param b: the right argument
        :return: true if a is less than b otherwise.
        """
        self._comparison_count += 1
        return a < b

    @abc.abstractmethod
    def sort(self, a: collections.abc.Sequence[int]) -> collections.abc.Sequence[int]:
        """
        Sorts the a Sequence.

        This function may overwrite a.

        :param a: the Sequence to sort
        :return: a sorted Sequence
        """
        pass