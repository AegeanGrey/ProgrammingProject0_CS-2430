################################################
# Coding Cadets                                #
# Thaddeus Schelp, Todd Dharni, Brayden Graham #
# CS2430                                       #
# Programming Project 1                        #
# Primary Author: Thaddeus Schelp              #
################################################
import HeapSort
import MergeSort
import SortingAlgorithm

import itertools
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
        print("""    python3 main.py sample_set [algorithms*]

    sample_set:
        Comma separated list of integers. For each integer in the CSV list an array of that size is made and every permutation of elements in that array is sorted by every listed algorithm.

    Algorithms:
        --mergesort  runs the mergesort algorithm
        --heapsort   runs the heapsort algorithm""")
        exit()
    # validate arguments
    invalid_argument: bool = False
    try:
        # build the sample set
        sample_set: tuple[int] = tuple(int(num) for num in sys.argv[1].split(','))
    except ValueError:
        print("First argument is invalid. Expected comma separated integers.", file=sys.stderr)
        invalid_argument = True
    # ensure only implemented sorting algorithms were requested
    for arg in sys.argv[2:]:
        if arg != "--mergesort" and \
           arg != "--heapsort":
            print(f"Invalid argument: '{arg}'", file=sys.stderr)
            invalid_argument = True
    # if all arguments are valid, test each sorting algorithm against the sample set
    if not invalid_argument:
        for arg in sys.argv[2:]:
            if arg == "--mergesort":
                print("==================== Merge Sort ====================")
                for i in sample_set:
                    for perm in itertools.permutations(range(i)):
                        algo: SortingAlgorithm.SortingAlgorithm = MergeSort.MergeSort()
                        result = algo.sort([*perm])
                        print(algo._comparison_count, perm, result)
            elif arg == "--heapsort":
                print("==================== Heap Sort ====================")
                for i in sample_set:
                    for perm in itertools.permutations(range(i)):
                        algo: SortingAlgorithm.SortingAlgorithm = HeapSort.HeapSort()
                        result = algo.sort([*perm])
                        print(algo._comparison_count, perm, result)
