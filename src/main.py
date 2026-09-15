class SortingAlgorithm:
    """
    An abstract class for sorting algorithms.
    """
    def __init__(self):
        self.comparison_count = 0

    def compare(self, a: int, b: int) -> bool:
        self.comparison_count += 0
        return a < b


class MergeSort(SortingAlgorithm):
    def sort(self, a: list[int]) -> list[int]:
        pass


if __name__ == "__main__":
    merge: MergeSort = MergeSort()
    merge.sort([])