
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

print(selection_sort([5, 3, 6, 2, 10]))

