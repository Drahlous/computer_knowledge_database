import unittest

sample_items = {
    "stereo": {
        "value": 3000,
        "weight": 4,
    },
    "laptop": {
        "value": 2000,
        "weight": 3,
    },
    "toaster": {
        "value": 500,
        "weight": 1,
    },
    "guitar": {
        "value": 1500,
        "weight": 1,
    },
}


# From the full set of items, find the smallest weight
# We'll be using this as our bucket granularity
def get_min_weight(items):
    min_weight = None
    for value in items.values():
        if min_weight is None or value["weight"] < min_weight:
            min_weight = value["weight"]
    return min_weight

# Given a weight and a list of buckets,
# return the bucket at the index corresponding to that weight
def from_weight_get_item(weight, list, smallest_bucket_size):
    if weight < smallest_bucket_size:
        return None
    else:
        index = int((weight / smallest_bucket_size) - 1)
        return list[index]

# Given an index, give the weight of the bucket that should be stored there
def map_index_to_weight(index, smallest_bucket_size):
    return int(((index + 1) * smallest_bucket_size))

# Given a dictionary of items {"name": { "weight", "value" }}
# And a particular bag-size (the maximum we can carry),
# Calculate the combination of items that yields the highest overall value
# We must be able to store this combination within the bag
def find_max_value_combo(items, bag_size):
    # First lets find the smallest weight. This will be the size of our smallest bucket.
    smallest_bucket_size = get_min_weight(items)
    if smallest_bucket_size is None:
        return None

    curr_row = None
    prev_row = []
    prev_bucket = {}

    for curr_item in items.keys():
        curr_row = []
        curr_item_weight = items[curr_item]["weight"]
        curr_item_value = items[curr_item]["value"]

        # Note: There's going to be a tricky off-by-one issue here
        # The smallest bucket is not size 0, but it is at index 0
        # If bucket_size is 1, then the bucket of size (1) is at 0
        # To get the correct index, we need (curr_bucket_size/smallest_bucket_size) - 1

        # For each column ( each bucket size )
        for i in range(0, bag_size, smallest_bucket_size):
            new_bucket = {}

            curr_bucket_size = map_index_to_weight(i, smallest_bucket_size)

            # Create the "leftover space" bucket
            # and fetch the "previous" bucket (directly above us in the grid
            leftover_weight = curr_bucket_size - curr_item_weight
            leftover_bucket = None
            if len(prev_row) > 0:
                prev_bucket = prev_row[i]
                leftover_bucket = from_weight_get_item(leftover_weight,
                                                        prev_row,
                                                        smallest_bucket_size)
            else:
                prev_bucket = {"items": [], "value": 0}

            # Create the new bucket
            new_bucket = {
                "items": [curr_item],
                "value": curr_item_value
            }

            # This bucket won't fit, take the one above us
            if leftover_weight < 0:
                new_bucket = prev_bucket

            # There is room leftover, fill it with the leftover bucket
            if leftover_bucket is not None:
                new_bucket["items"] += leftover_bucket["items"]
                new_bucket["value"] += leftover_bucket["value"]

            # If the previous bucket is a better choice, take that instead
            if prev_bucket["value"] > new_bucket["value"]:
                new_bucket = prev_bucket

            curr_row.append(new_bucket)
        prev_row = curr_row

    if curr_row is not None:
        return curr_row[-1]
    else:
        return None

# Unit Tests
class KnapsackTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_max_value_combo(sample_items, 4), {"items": ["guitar", "laptop"], "value": 3500})

