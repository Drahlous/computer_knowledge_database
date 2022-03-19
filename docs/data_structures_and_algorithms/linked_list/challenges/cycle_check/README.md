# Challenge: Linked List Cycle Test


Given the `head` of a linked list, determine if the list contains a cycle.
A cycle means there's a way to leave from a point, and return to that same point later.

Return `true` if there's a cycle, `false` otherwise.

### Problem Solving

A simple solution is to keep track of every node that we've seen.
We could add each node to a hash-table as we pass through.
Then, every time we hit a node, we could see if we have already stored it in the hash-table.

However, this solution uses `O(n)` extra memory.
Is there a way to do it in `O(1)` memory?

If we send out two pointers that move at *different speeds*, then they will eventually catch up to one-another.
One pointer is a `leader`, and another is the `follower`. 
The leader will move faster than the follower.

If we hit a `nullptr`, we're at the end and there's no cycle.
If we see that `leader` and `follower` are the same, we *must have hit a cycle*.



## Part 2: Return the node where the cycle *begins*

We're going to creep the `head` node forward, and try to detect it with the other pointers that we know are already in the cycle.
We can send the `leader` around the cycle repeatedly, watching for `follower`. When we hit `follower`, we move `head` forward.


