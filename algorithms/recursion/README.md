# Recursion

## Overview
Imagine that you find yourself crouching around the dusty attic at your grandmas, when you find an old locked chest.
You ask where the key is, and she points to a cardboard box in the corner. You open the box to find a set of smaller boxes.

If you want to find the key in this nested set of boxes, you might use a recursive algorithm.
1. Look through the box
2. If you find a box, open it and go back to step 1
3. If you find a key, youre done!

Loops can perform better, but recursion can be more readable in some cases (or the only option!)

### Base Case
The `Base Case` tells you when youre finished and can stop recursing 

### Recursive Case
The `Recursive Case` is the part that you keep jumping back into until you end up with the base case


### The Stack Datastructure
A `Stack` allows you to do two actions:
- `Push` a new item to the top
- `Pop` the top item off the stack


## Notes
- Recursion is when functions call themselves

- Every recursive function has a `base case` and a `recursive case`

- A `Stack` can `push` and `pop`

- Functions are added on top of the `callstack`, which can get very large, take a lot of memory, and overflow

