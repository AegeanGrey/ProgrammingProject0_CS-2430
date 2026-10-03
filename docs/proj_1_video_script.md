# Introduction

Names and Roles

# Explaining The Programs Structure



## Show Permutation Generator

Permutations of the first $N$ integers are generated using `itertools.permutations(range(N))`. This is done in the `_analyze()` function in `main.py`.

## Show Comparison Counter 

We use the compare most and compare least functions in SortingAlgorithm to track the number of comparisons.

## Algorithm Summaries

30 Seconds Per Algo

### Heapsort

Heapsort treats the array as a max heap. The 'max heapification' process forces each parent to be larger than either of its children.

Until the heap is empty, the algorithm:

1. Places the top element at the beginning of the result array.
2. Heapifies, only affecting parts of the heap that change.

When the unsorted array is empty, the result array contains the elements in sorted order.

### Quicksort

Creates branching permutations of the original array based off a `pivot` and orders the results of each permutation `pivot` from left to right

### Shakersort

Also known as cocktailsort, uses `counter` to keep track of it's position in the array and takes the starting element to compare throughout (while reading from left to right) to sort the highest individual value to the right side of the array, 
and doing the opposite when moving in reverse (going from right to left) to sort the smallest individual value(s)

### Mergesort (Transition to showcase)

Mergesort splits the input array into $N$ subarrays, each with a single element. Since each subarray has a single element, it is sorted.

It then merges adjacent subarrays preserving the sorted order. The merging process is done by pulling from whichever side has the next smallest element. This process of merging adjacent subarrays is repeated until all subarrays have been merged.

At this point, the only remaining subarray contains all the elements in their sorted order.

### Comparison Counting in Mergesort

Mergesort uses the same method for counting comparisons as the other algorithms. It uses one of the `SortingAlgorithm.compare` functions which return the result of the comparison and increments an internal counter. This counter is read back after the sort is finished to determine the total number of comparisons performed. In the case of mergesort, comparisons only happen when merging subarrays.

# Conclusion

Based on our testing and analysis, we conclude that, by measure of comparisons, mergesort is the most efficient algorithm of those tested. Furthermore, we predict that mergesort will scale very well to large values of $N$. From our observations, we can conclude that the data set ***size*** and the initial order will directly affect the best sorting algorithm for the required use case. Finally, we believe that using the `itertools.permutations` python library was a more effective form of streamlining consistency amongst our sorting algorithms and their results.
