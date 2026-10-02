# Introduction

Names and Roles

# Explaining The Programs Structure



## Show Permutation Generator

Permutations of the first $N$ integers are generated using `itertools.permutations(range(N))`. This is done in the `_analyze()` function in `main.py`.

## Show Comparison Counter 

Explain functionality and implementation or where it's applied 

## Algorithm Summaries

30 Seconds Per Algo

### Heapsort

Heapsort treats the array as a heap where each element $i$'s children are located at $2i+1$ and $2i+2$.

The algorithm begins by building a max heap. This 'max heapification' process forces each parent to be larger than either of its children.

Until the heap is empty:


1. Place the top element at the beginning of the result array.
2. Heapify, only affecting parts of the heap that change.

When the unsorted array is empty, the result array contains the elements in sorted order.

### Quicksort



### Shakersort



### Mergesort (Transition to showcase)

Mergesort splits the input array into $N$ subarrays, each with a single element. Since each subarray has a single element, it is sorted.

It then merges adjacent subarrays preserving the sorted order. The merging process is done by pulling from whichever side has the next smallest element. This process of merging adjacent subarrays is repeated until all subarrays have been merged.

At this point, the only remaining subarray contains all the elements in their sorted order.

### Comparison Counting in Mergesort

Mergesort uses the same method for counting comparisons as the other algorithms. It uses one of the `SortingAlgorithm.compare*()` which return the result of the comparison and increment an internal counter. This counter is read back after the sort is finished to determine the total number of comparisons performed. In the case of mergesort, comparisons only happen when merging subarrays.

# Conclusion

Based on our testing and analysis, we conclude that, by measure of comparisons, mergesort is the most efficient algorithm of those tested. Furthermore, we predict that mergesort will scale very well to large values of $N$.
