#!/bin/python
import unittest
from collections import deque

def person_is_seller(name):
    # For now, represent sellers with a "_m" at the end of their name
    return (name[-2] == '_' and name[-1] == 'm')

# Perform a Breadth-First-Search through "graph",
# Starting from the entry at "name"
# Returns the name of the nearest mango-seller or None if no such path exists
def search(name, graph):
    if name == '':
        return None

    # Create the list of people to search
    search_queue = deque()

    # Add the list of your neighbors to the search-queue
    if graph.get(name):
        search_queue += graph[name]

    # Keep track of which people we've already searched
    searched = []

    # While the search queue is not empty
    while search_queue:
        person = search_queue.popleft()
        # Only search people we've never seen
        if not person in searched:
            if person_is_seller(person):
                return person
            else:
                # Add this persons neighbor's to the queue
                search_queue += graph[person]
                searched.append(person)
    return None


# Unit Tests
class BreadthFirstSearchTest(unittest.TestCase):
    def test_empty(self):
        graph = {}
        self.assertEqual(search("", graph), None)

    def test_cyclic(self):
        graph = {}
        graph["you"] = ["peggy"]
        graph["peggy"] = ["you"]
        self.assertEqual(search("you", graph), None)

    def test_cyclic_triple(self):
        graph = {}
        graph["you"] = ["peggy"]
        graph["peggy"] = ["jim"]
        graph["jim"] = ["you", "frank"]
        graph["frank"] = ["you", "gary_m"]
        graph["gary_m"] = []
        self.assertEqual(search("you", graph), "gary_m")

    def test_second_degree(self):
        # There are directed edges from you to alice, bob, and claire
        graph = {}
        graph["you"] = ["alice", "bob", "claire"]


        # We can add second-degree connections like this
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny_m"]

        # These entries have no connections
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny_m"] = []
        self.assertEqual(search("you", graph), "jonny_m")

