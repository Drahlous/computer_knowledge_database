#!/bin/python
import unittest

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


# Unit Tests
class QuicksortTest(unittest.TestCase):
    def test_quicksort_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_quicksort_zero(self):
        self.assertEqual(quicksort([0]), [0])

    def test_quicksort_single(self):
        self.assertEqual(quicksort([10]), [10])
    def test_quicksort_two_sorted(self):
        self.assertEqual(quicksort([10, 15]), [10, 15])

    def test_quicksort_two_unsorted(self):
        self.assertEqual(quicksort([15, 10]), [10, 15])

    def test_quicksort_three_sorted(self):
        self.assertEqual(quicksort([10, 15, 20]), [10, 15, 20])

    def test_quicksort_three_reversed(self):
        self.assertEqual(quicksort([20, 15, 10]), [10, 15, 20])

    def test_quicksort_three_left_shift(self):
        self.assertEqual(quicksort([15, 20, 10]), [10, 15, 20])

