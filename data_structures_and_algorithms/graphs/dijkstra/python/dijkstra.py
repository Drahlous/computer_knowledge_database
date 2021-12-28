#!/bin/python3
import unittest

"""
Sample Graph:


      ---> (A) --- 1
   6 --     ^    ----
    --      |        v
(start)    3|      (end)
    --      |        ^
   2 --     |    ----
      ---> (B) --- 5

The shortest route in this graph is 6 units long:

    start --> B --> A --> end
           2  +  3  +  1  = 6

"""

sample_graph = dict()
sample_graph["start"] = { "a": 6, "b": 2 }
sample_graph["a"] = { "end": 1 }
sample_graph["b"] = { "a": 3, "end": 5 }
sample_graph["end"] = {}

### Table Breakdown

### Initial
#   node    cost    processed   parent
#   ---     ---     ---         ---
#   start   0       False       None
#   A       None    False       None
#   B       None    False       None
#   end     None    False       None

### Processed Start
#   node    cost    processed   parent
#   ---     ---     ---         ---
#   start   0       True        None
#   A       6       False       Start
#   B       2       False       Start
#   end     None    False       None

### Processed B
#   node    cost    processed   parent
#   ---     ---     ---         ---
#   start   0       True        None
#   A       5       False       B
#   B       2       True        Start
#   end     7       False       B

### Processed A
#   node    cost    processed   parent
#   ---     ---     ---         ---
#   start   0       True        None
#   A       5       True        B
#   B       2       True        Start
#   end     6       False       A

# Then build the path backwards from "end" by checking "parent"
# end -> A -> B -> start

# Reverse the list to get the final path
# start -> B -> A -> end






# Update the table with the new costs of neighbor nodes
# Mark this node as processed
def update_table(parent, graph, table):
    for key in graph[parent].keys():
        old_cost = table[key]["cost"]

        if old_cost is None:
            print( key + " old cost: None")
        else:
            print( key + " old cost: " +  str(old_cost))

        # New Cost = (cost_to_parent) + (cost_from_parent_to_node)
        new_cost = table[parent]["cost"] + graph[parent][key]
        print( key + " new cost: " + str(new_cost)) 

        if table[key]["cost"] is None or new_cost < table[key]["cost"]:

            print( key + " updated cost:  " + str(new_cost)) 
            table[key]["cost"] = new_cost
            table[key]["parent"] = parent

    table[parent]["processed"] = True

# Find the next cheapest node
def get_next_cheapest(table):
    cheapest_node = None
    for key in table.keys():
        if not table[key]["processed"]:
            if cheapest_node is None or table[key]["cost"] < table[cheapest_node]["cost"]:
                cheapest_node = key
    return cheapest_node

def get_final_path(table, end):
    final_path = []
    node = end
    while node is not None:
        final_path.append(node)
        node = table[node]["parent"]
    return final_path

def dijkstra(graph, start, end):
    # Initialize the table
    # Table entries contain nodes, costs, a flag for marking processed nodes, and the parent node
    table = dict()
    for key in graph.keys():
        table[key] = {"cost": None, "processed": False, "parent": None }

    table[start]["cost"] = 0
    table[end]["processed"] = True

    current_node = start

    while current_node is not None:
        print("current_node: " + current_node)
        print(table)
        update_table(current_node, graph, table)
        current_node = get_next_cheapest(table)

    path = get_final_path(table, end)
    print(path)

# Unit Tests
class DijkstraTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(dijkstra(sample_graph, "start", "end"), None)


