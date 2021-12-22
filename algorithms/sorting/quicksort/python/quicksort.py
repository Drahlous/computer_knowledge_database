#!/bin/python

### Complexity
# Average Case: O(n logn)
# Worst Case:   O(n^2)

### Base cases
# No elements : Done
# Single element : Done

### Recursive Cases
# Two elements
# left < right : Done
# left > right : Swap elements, Done
# This is accomplished with: pivot = left, right is less than pivot, move right to left, done 

def quicksort(arr):
    ### Base Case
    if len(arr) < 2:
        return arr
    else:
        ### Recursive case
        # Pick pivot arbitrarily for now, we'll make a better choice in a later implementation
        pivot = arr[0]
        lower = [i for i in arr[1:] if i <= pivot]
        higher = [i for i in arr[1:] if i > pivot]
        return quicksort(lower) + [pivot] + quicksort(higher)


print(quicksort([]))
print(quicksort([0]))
print(quicksort([10]))
print(quicksort([10, 15]))
print(quicksort([15, 10]))
print(quicksort([10, 15, 20]))
print(quicksort([20, 15, 10]))
print(quicksort([15, 20, 10]))

