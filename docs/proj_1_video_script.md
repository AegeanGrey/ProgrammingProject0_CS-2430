# Mergesort

Mergesort splits the input array into $N$ subarrays, each with a single element. Since each subarray has a single element, it is sorted.

It then merges adjacent subarrays preserving the sorted order. The merging process is done by pulling from whichever side has the next smallest element. This process of merging adjacent subarrays is repeated until all subarrays have been merged.

At this point, the only remaining subarray contains all the elements in their sorted order.

# Heapsort

Heapsort treats the array as a heap where each element $i$'s children are located at $2i+1$ and $2i+2$.

The first step it takes is to convert the heap into a max heap in which the largest element is at the top of the heap. This 'heapification' process exchanges each parent with the larger of its children if that child is also larger than the parent. This starts at the bottom of the heap and works its way up, pushing the largest values to the top.

These next steps are repeated until the unsorted array is empty: First, the largest element is removed from the heap and placed at the beginning of the result array. Then the new head is heapified as described above. If any swap was performed, then the new child is also heapified until we reach the bottom of the tree or no more swaps happen.

When the unsorted array is empty, the result array contains the elements in sorted order.
