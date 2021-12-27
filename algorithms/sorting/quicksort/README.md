# Quicksort

## Overview
- Quicksort uses `Divide and Conquer` to recursively sort an array of elements

- Pick a `pivot`, put smaller elements on the left, larger elements on the right (this is called `partitioning`)

- Recursively sort the two smaller sub-arrays

- Average case `O(n log n)`, worst case `O(n^2)`


### Base Cases
These arrays are really easy to sort:
- `[]` : Empty Array, already sorted
- `[5]` : Single Element, already sorted

Two elements are a tiny bit harder, but still easy:
- `[3, 7]` : left < right, already sorted
- `[7, 3]` : left > right, just swap the elements


### Recursive Cases
1. Pick an element to be the `Pivot`
2. Move elements `less than` the pivot to the `left` sub-array
2. Move elements `greater than` the pivot to the `right` sub-array
4. Recursively call quicksort on the sub-arrays, return to step (1)




## Quicksort Complexity
Quicksort is a little strange, the `complexity` depends on which `pivot` we choose.
We get the best performance when we pick the pivot completely randomly every time.

- Average Case: `O(n logn)`

- Worst Case: `O(n^2)`



## Notes

- `Quicksort` is actually faster than `Merge Sort`, even though they have the same complexity `O(n logn)`

