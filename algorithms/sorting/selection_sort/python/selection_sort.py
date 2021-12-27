import unittest


def find_smallest_idx(input_array):
    smallest = input_array[0]
    smallest_index = 0

    for i in range(1, len(input_array)):
        if input_array[i] < smallest:
            smallest = input_array[i];
            smallest_index = i

    return smallest_index


def selection_sort(input_array):
    new_array = []
    for i in range(len(input_array)):
        smallest_idx = find_smallest_idx(input_array)
        # Pop the smallest item from the old array, push it onto the new one
        new_array.append(input_array.pop(smallest_idx))
    return new_array



# Unit Tests
class SelectionSortTest(unittest.TestCase):

    def test_selection_sort_empty(self):
        self.assertEqual(selection_sort([]), [])

    def test_selection_sort_single(self):
        self.assertEqual(selection_sort([5]), [5])

    def test_selection_sort_basic(self):
        self.assertEqual(selection_sort([5, 3, 6, 2, 10]), [2, 3, 5, 6, 10])

    def test_selection_sort_with_negatives(self):
        self.assertEqual(selection_sort([1, 0, -2, 2, -1]), [-2, -1, 0, 1, 2])





