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
        + sort(MutableSequence~int~ a)* Sequence~int}~ None
    }

    class MergeSort {
        - merge (Iterable~List~int~~ l, Iterable~List~int~~ r) Iterable~List~int~~
    }
    
    class HeapSort{
        - heapify (MutableSequence~List~int~~ a, int node, int unsorted_size) None
        
    }
    
    class QuickSort{
        - quickSort(~List~int~~ array, int start, int end) None
        - partition(~List~int~~ array, int start, int end) int
    }
    
    class ShakerSort{
        - shakerSort(~List~int~~ array) None
    }
```
