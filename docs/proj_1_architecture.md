```mermaid
classDiagram
    SortingAlgorithm --|> MergeSort
    SortingAlgorithm --|> HeapSort
    SortingAlgorithm --|> QuickSort
    SortingAlgorithm --|> ShakerSort
    
    class SortingAlgorithm{
        - comaparison_count int
        + compareLeast(int a, int b) bool
        + compareMost(int a, int b) bool
        + sort(MutableSequence~int~ a)* Sequence~int}~
    }

    class MergeSort {
        - merge (Iterable int~ l, Iterable~List~Int~~ r) Iterable~int~
    }
    
    class HeapSort{
        - heapify (MutableSequence~int~ a, int node, int unsorted_size)
        
    }
    
    class QuickSort{
        - quickSort(~int~ array, int start, int end)
        - partition(~int~ array, int start, int end)
    }
    
    class ShakerSort{
        - shakerSort(~int~ array, int start, int end)
        - 
    }
```
