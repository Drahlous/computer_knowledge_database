# Dijkstra's Algorithm

Dijkstra's algorithm is run on `weighted` graphs to find the `shortest path`.
It only works on `Acyclic Graphs` with `No Negative Edges`.

## Overview

- Keep a table of all of the nodes in the graph

- In the table, keep track of the 'cheapest' cost to get to each node

- At each step use the `current cheapest` node, see if this node allows us to get to its neighbors for cheaper than any other paths seen so far

| Node | Cost | Processed? | Parent |
| --- | --- | --- | --- |
| A | 2 | True | Start |
| B | 3 | False | Start |
| C | NULL | False | NULL |

## Dijkstra's Algorithm Steps

1. Pick a `current_node`, this will be the cheapest node stored in our table so far.

2. We need to update the cost for this node's neighbors.
    - We should compare the `neighbor's` current total cost (in the table) to the theoretical cost they would have if we used a path from `current_node` (`total_cost_to_current_node` + `cost_of_edge_from_current_to_neighbor`)
    - If this new cost is cheaper, update the neighbor's cost and mark it's parent as `current_node`

3. Mark the `current_node` as processed, do not process it again.

4. Repeat until every node in the graph is marked `processed`.

## Dijkstra's Algorithm vs Breadth First Search

- `Breadth First Search` finds the shortest path in terms of the `number of edges` in the path. BFS ignores the weights.

- `Dijkstra's Algorithm` finds the shortest path in terms of the `total combined weight` of the edges in the path.

## Graph Terminology

- A `Weighted graph` has a number assigned to each edge. This number represents the `cost` of using that edge.
- An `Unweighted graph` has no numbers on the edges. Each edge has the same cost.

- A `Cycle` is a path in a graph that allows you to `start at a node`, `travel around`, and `end up where you started`.

## The Key Idea of Dijkstra's Algorithm

At each step, when you find the `cheapest` node, the `cost` currently stored for that node is the lowest that it can possibly ever be.
It is `mathematically impossible` that you'll find a shorter path to this node later on.

This is why `Dijkstra's Algorithm` breaks down when you have `Negative-Weight edges within a cycle`.
In these cases, use something like `Bellman-Ford` instead.

You might be tempted to think that you can get rid of the negative-weight problem by adding a positive offset to all edges.
The problem is that, although an offset affects all `edges` equally, it *does not* affect all `paths` equally.
Paths of different segment lengths will be changed by differing amounts.

```text
Length : 2
     2
A   -->     B

Length : *3*
     3
A   -->     B 


Length : 2
     1           1
A   -->     B   -->     C

Length : *4*
     2           2
A   -->     B   -->     C
```
