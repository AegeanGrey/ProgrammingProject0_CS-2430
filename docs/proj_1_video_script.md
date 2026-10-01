# Mergesort

Mergesort splits the input array into $N$ subarrays, each with a single element. Since each subarray has a single element, it is sorted.

It then merges adjacent subarrays preserving the sorted order. The merging process is done by pulling from whichever side has the next smallest element. This process of merging adjacent subarrays is repeated until all subarrays have been merged.

At this point, the only remaining subarray contains all the elements in their sorted order.

# Heapsort

Heapsort treats the array as a heap where each element $i$'s children are located at $2i+1$ and $2i+2$.

The algorithm begins by building a max heap. This 'max heapification' process forces each parent to be larger than either of its children.

Until the heap is empty:

1. Place the top element at the beginning of the result array.
2. Heapify, only affecting parts of the heap that change.

When the unsorted array is empty, the result array contains the elements in sorted order.

# Permutation Generator

Permutations of the first $N$ integers are generated using `itertools.permutations(range(N))`. This is done in the `_analyze()` function in `main.py`.

# Comparison Counting in Mergesort

Mergesort uses the same method for counting comparisons as the other algorithms. It uses one of the `SortingAlgorithm.compare*()` which return the result of the comparison and increment an internal counter. This counter is read back after the sort is finished to determine the total number of comparisons performed. In the case of mergesort, comparisons only happen when merging subarrays.