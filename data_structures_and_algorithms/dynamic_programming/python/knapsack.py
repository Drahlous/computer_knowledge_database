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


def get_min_weight(items):
    min_weight = None
    for value in items.values():
        if min_weight is None or value["weight"] < min_weight:
            min_weight = value["weight"]
    return min_weight


def find_max_value_combo(items, bag_size):
    ### Setup the grid

    # First lets find the smallest weight. This will be the size of our smallest bucket.
    bucket_size = get_min_weight(items)
    if bucket_size is None:
        return None

    prev_row = []
    prev_bucket = {}

    for curr_item in items.keys():
        print("\n\nChecking item " + curr_item)

        print("previous row:")
        print(prev_row)


        curr_row = []
        curr_item_weight = items[curr_item]["weight"]
        curr_item_value = items[curr_item]["value"]

        # For each column ( each bucket size )
        for i in range(0, bag_size, bucket_size):
            curr_bucket_size = i + bucket_size
            new_bucket = {}
            print("filling bucket: " + str(curr_bucket_size))
            if len(prev_row) > 0:
                prev_bucket = prev_row[i]

                new_bucket = {
                        "items": [curr_item, prev_row[i - curr_item_weight]["items"]],
                        "value": curr_item_value + prev_row[i - curr_item_weight]["value"],
                    }
            else: 
                prev_bucket = {"items": None, "value": 0}
                new_bucket = {
                        "items": curr_item,
                        "value": curr_item_value
                    }

            # This item can't fit, take previous best
            if curr_item_weight > curr_bucket_size or prev_bucket["value"] > new_bucket["value"]:
                new_bucket = prev_bucket
        
            curr_row.append(new_bucket)

        prev_row = curr_row
        print("new_row: ")
        print(curr_row)
# Unit Tests
class KnapsackTest(unittest.TestCase):
    def test_basic(self):
        find_max_value_combo(sample_items, 4)


