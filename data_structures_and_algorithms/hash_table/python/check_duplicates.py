import unittest

def check_duplicates(input_list):
    my_hash_table = {}
    for item in input_list:
        if my_hash_table.get(item):
            return True
        else:
            my_hash_table[item] = True
    return False


# Unit Tests
class CheckDuplicatesTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(check_duplicates([]), False)

    def test_single(self):
        self.assertEqual(check_duplicates(["Bob"]), False)


    def test_pair_no_dup(self):
        self.assertEqual(check_duplicates(["Bob", "Billy"]), False)

    def test_pair_with_dup(self):
        self.assertEqual(check_duplicates(["Bob", "Bob"]), True)
