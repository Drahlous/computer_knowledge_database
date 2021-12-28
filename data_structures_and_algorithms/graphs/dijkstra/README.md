# Dijkstra's Algorithm

Dijkstra's algorithm is run on `weighted` graphs to find the `shortest path`.
It only works on `Acyclic Graphs` with `No Negative Edges`.

## Overview 
- Keep a table with all of the nodes in the graph, keep track of the 'cheapest' cost to get to each node.

- Recursively find the `current cheapest` node, update the costs of its neighbors if the path from this node is cheaper.

- Mark this node as processed, do not process it again.

- Repeat for every node in the graph.


| Node | Cost | Processed? | Parent |
| --- | --- | --- | --- |
| A | 2 | True | Start |
| B | 3 | False | Start |
| C | NULL | False | NULL |





