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

### Queues
Queues work the same way that you're used to in real life;
although you might call them `lines`, as in: `waiting in the lunch line`

Queues are similar to Stacks, with one key difference:
- `Queues` are FIFO (First in, First out)
- `Stacks` are LIFO (Last in, First out)

Like Stacks, Queues are also `bad at Random Access`

Queues support two operations:
- `Enqueue` (push to front)
- `Dequeue` (pop from back)



## Implementing a Graph in code
To implement a Graph, we need two things:
- `Nodes`
- `Edges` (Connections between the nodes)

So we need a data structure that lets us model the relationships between objects...
Do we already know anything that can do this for us?

`Hash Tables`!


In python, we can implement a graph with a `dictionary (hash_table)`.
For each entry, the `key` will represent a particular node.
The `value` will be a list of other nodes, meaning that there is an edge from this node to each node in the list.
This is called an `adjacency list`


```python
# There are directed edges from you to alice, bob, and claire
graph = {}
graph["you"] = ["alice", "bob", "claire"]


# We can add second-degree connections like this
graph["bob"] = ["anuj", "peggy"]
```

Note that the order within the adjacency list doesn't matter.




## Implementing the Breadth First Search Algorithm
Remember that the implementation will work like this:

1. Keep a `Queue` containing the people to check

2. `Pop` a person off the queue

3. Check whether this person is the target

4.a if this is the target, then we're done! return true

4.b. if this is not the target, add all of their `neighbors` to the `queue`

5. Loop back to step 1

6. if the queue is empty, no route exists. return false


Python supports `Queues` with the `Deque (Double Ended Queue)`
```python
from collections import deque

def search():
    # Create the list of people to search
    search_queue = deque()

    # Add the list of your neighbors to the search-queue
    search_queue += graph["you"]

    # While the search queue is not empty
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a seller!")
            return True
        else:
            search_queue += graph[person]

```

But what happens when two people have the same friend?
In this example, both bob and alice are friends with peggy, so we'll end up checking her twice!
```python
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
```

To prevent this, *we'll need to keep track of which people we've already checked*.

If we don't track the already-checked people, we might end up in an infinite loop. This could happen if the graph has a *cyclic dependency*:


```python
graph["you"] = ["peggy"]
graph["peggy"] = ["you"]
```

- We would add you're neighbors (peggy) before checking you.
- We'd move on to checking peggy, first adding her neighbors (you)
- Jumping back to you, we'd add your neighbors (peggy) again...



Accounting for the duplication prevention, we get:
```python

# Perform a Breadth-First-Search through "graph",
# Starting from the entry at "name"
# Returns the name of the nearest mango-seller or None if no such path exists
def search(name, graph):

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
```

## Complexity of Breadth First Search `O(V + E)`
If you search the entire network then you'll follow every edge, so we're at least `O(E)` where `E = number_of_edges`.
Further, you'll need to add each node (vertex) to queue at some point. That's individually constant, but we do it `V = number_of_vertices` times, for `O(V)`.

Combined, we get `O(V + E)` where `V is the number of Vertices`, `E is the number of edges`.


## Breadth First Search Recap
- BFS tells you if there's a path from A to B

- If a path exists, BFS find the shortest path

- A `directed graph` has arrows, the `direction` of the arrows represents the dependency direction.

- An `undirected graph` has no arrows, and the relationships go `both ways`

- `Queues are FIFO (First in, First out)`

- `Stacks are LIFO (Last in, First out)`

- You must check people in the `order` that they're added to the `search_queue`, otherwise you don't get the shortest path.

- You must keep a list of the people you've already checked to prevent `duplicates`, otherwise you risk `infinite loops`.

