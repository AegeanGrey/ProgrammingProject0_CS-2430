################################################
# Coding Cadets                                #
# Thaddeus Schelp, Todd Dharni, Brayden Graham #
# CS2430                                       #
# Programming Project 1                        #
# Primary Author: Thaddeus Schelp              #
################################################
import HeapSort
import MergeSort
import QuickSort
import ShakerSort
import SortingAlgorithm

import itertools
import sys

def _analyze(sample_set: tuple[int], algorithm: type):
    for i in range(len(sample_set)):
        result_i: list[int] = []
        for perm in itertools.permutations(range(sample_set[i])):
            algo: SortingAlgorithm.SortingAlgorithm = algorithm()
            algo.sort([*perm])
            result_i.append(algo._comparison_count)

        indices: list[int] = sorted(range(len(result_i)), key=lambda k: result_i[k])
        average: float = sum(result_i) / len(result_i)
        best: list[int] = sorted(indices[:10], key=lambda k: result_i[k])
        worst: list[int] = sorted(indices[-10:], key=lambda k: result_i[k])
        permutations: tuple[tuple[int]] = tuple(itertools.permutations(range(sample_set[i])))
        length: int = len(str(permutations[0]))
        print(f"Permutations of {sample_set[i]} elements")
        print(f"\t    Total number of cases : {len(result_i)}")
        print(f"\t   Average compare counts : {average:.2f}")
        print(f"\t     Worst compare counts : {" | ".join(" "*(length - len(str(j))) + str(j) for j in (result_i[j] for j in worst))}")
        print(f"\t              Worst cases : {" | ".join(" "*(length - len(str(permutations[j]))) + str(permutations[j]) for j in worst)}")
        print(f"\t      Best compare counts : {" | ".join(" "*(length - len(str(j))) + str(j) for j in (result_i[j] for j in best))}")
        print(f"\t               Best cases : {" | ".join(" "*(length - len(str(permutations[j]))) + str(permutations[j]) for j in best)}")


def main():
    if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
        print("""    python3 main.py sample_set [algorithms*]

    sample_set:
        Comma separated list of integers. For each integer in the CSV list an array of that size is made and every permutation of elements in that array is sorted by every listed algorithm.

    algorithms:
        --mergesort  includes tests for the mergesort algorithm
        --heapsort   includes tests for the heapsort algorithm
        --quicksort  includes tests for the quicksort algorithm
        --shakersort includes tests for the shakersort algorithm""")
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
           arg != "--heapsort" and \
           arg != "--quicksort" and \
           arg != "--shakersort":
            print(f"Invalid argument: '{arg}'", file=sys.stderr)
            invalid_argument = True
    # if all arguments are valid, test each sorting algorithm against the sample set
    if not invalid_argument:
        for arg in sys.argv[2:]:
            if arg == "--mergesort":
                print("==================== Merge Sort ====================")
                _analyze(sample_set, MergeSort.MergeSort)
            elif arg == "--heapsort":
                print("==================== Heap Sort ====================")
                _analyze(sample_set, HeapSort.HeapSort)
            elif arg == "--quicksort":
                print("==================== Quick Sort ====================")
                _analyze(sample_set, QuickSort.QuickSort)
            elif arg == "--shakersort":
                print("==================== Shaker Sort ====================")
                _analyze(sample_set, ShakerSort.ShakerSort)


if __name__ == "__main__":
    main()