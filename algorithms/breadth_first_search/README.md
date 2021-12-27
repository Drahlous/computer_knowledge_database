# Breadth First Search (BFS)

### Topics Covered

- `Graphs`: Data structure used to map networks and relationships (Directed vs Undirected)

- `Breadth First Search`: Algorithm used on graphs, can answer questions like `whats the shortest X?`

- `Topological Sort`: A type of sorting algorithm that exposes `dependencies` between nodes


### BFS Usecase Examples
BFS is good at finding shortest-paths:

- Write a checkers AI to calculate the fewest moves to victory

- Write a spellchecker (fewest number of edits to translate a misspelled word into a real one, e.g. Readed is one-off from Reader)

- Find the nearest doctor to you within your insurance network


## Introduction to Graphs
A `Graph` models a set of `objects (nodes)` along with the `connections (edges)` between them.


## BFS Overview
`Breadth first search` is an algorithm used to search through graph data structures.
They allow you to answer two types of questions:

- Is there a path from A to B?

- What is the shortest path from A to B?

Say for example that you're a mango farmer, and you're looking through facebook to find a mango seller.
How would you check whether you're connected to a mango seller?


The search is simple:
1. Make a list of friends to search
2. Go to each person on the list, check if they sell mangos


But what if none of your friends are mango sellers? Then you need to check `friends-of-friends`.
3. Each time you add someone to the list of people to check, add all of their friends to the list too!

Adding step (3) makes this `Breadth First Search`, and it will eventually cover the entire network.


So we've answered the first question: `Is there a path from A to B?`
But how do we answer the second question: `What is the shortest path from A to B?`


The nice thing is that BFS already works this way!
As long as we `check items in the same order that they're added to the list`, we'll automatically find the shortest path first.
This will automatically search all first-degree connections before any second-degree connections;
It will search all second-degree connections before any third-degree connections, and so on...


But how do we ensure that we only check items in the same order that they're added to the list?
We need a new data structure, called a `Queue`...

## Queues
Queues work the same way that you're used to in real life;
although you might call them `lines`, as in: `waiting in the lunch line`

Queues are similar to Stacks, with one key difference:
- `Queues` are FIFO (First in, First out)
- `Stacks` are LIFO (Last in, First out)

Like Stacks, Queues are also `bad at Random Access`

Queues support two operations:
- `Enqueue` (push to front)
- `Dequeue` (pop from back)


