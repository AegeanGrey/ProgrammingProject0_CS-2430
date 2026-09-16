import MergeSort

import itertools

if __name__ == "__main__":
    for i in (4,):
        for perm in itertools.permutations(range(i)):
            merge: MergeSort.MergeSort = MergeSort.MergeSort()
            result = merge.sort(perm)
            print(merge._comparison_count, perm, result)