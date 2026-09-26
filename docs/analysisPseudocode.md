In the below pseudocode:
- Each sorting_algorithm is expected to inherit from `SortingAlgorithm` as shown in the classDiagram.md file.
- The permutations are generated using Python's builtin `itertools.permutations`.

```pseudo
for each sorting_algorithm:
  let comparisons be an empty array
  for each sample_size:
    // Generate comparison counts
    for each permutation of [1..sample_size]:
      sorting_algorithm.sort(permutation)
      comparisons.push(comparison_count)
    end
    
    // Gather best and worst indices
    sort indices into the comparisons array by their associated comparison_count
    let best be the first 10 indices
    let worst be the last 10 indices
    
    // Display everything
    display sorting_algorithm.name
    display average(comparisons)
    for each index of the best indices:
      display permutations[index]
      display comparisons[index]
    end
    for each index of the worst indices:
      display permutations[index]
      display comparisons[index]
    end
  end
end
```