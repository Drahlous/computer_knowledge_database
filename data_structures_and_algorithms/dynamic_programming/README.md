# Dynamic Programming

Dynamic Programming is used for `optimization problems` that involve a `constraint`.

Dynamic Programming is a technique for solving hard problems, it's not a one-size-fits-all algorithm.
It only works on problems that can be broken into `discrete sub-problems`.


## Overview
Every Dynamic Programming algorithm uses a `grid` to keep track of the results of the subproblem.

- Break a large problem into smaller subproblems (sort of like recursion)

- Store the results from each of the subproblems in the `grid`

- Build the final solution up by re-using the already-computed results of the subproblems



## The Knapsack Problem

You are a thief. You can only steal the things you can fit in your bag.
You see these items that you might steal:

| Item | Value | Weight|
| --- | --- | --- |
| Stereo | $3000 | 4 lbs |
| Laptop | $2000 | 3 lbs |
| Guitar | $1500 | 1 lbs |
| Toaster | $500 | 1 lbs |


You want to steal as much `value` as you can, but your bag only carries `4 lbs`!
What should we take?

So you can steal the Stereo for $3000, but that takes up all of your 4 lb bag space.

You could take the Laptop for $2000, which uses 3 lbs of your bag space.
That leaves us with *1 lb of leftover space*.
In that *leftover space* we could take the toaster or the guitar.
It's obvious to us that we'd take the guitar, it's more valuable.

This is the part that we should focus on:
What question are we really answering here?
>In that *leftover space* we could take the toaster or the guitar.
>It's obvious to us that we'd take the guitar, it's more valuable.

We can rephrase this question as *What is the maximum value we can put in 1 lb of leftover space?*

But what if we had *2 lbs of leftover space*? We can't just multiply the 1 lb answer by 2, there is only one guitar that we can steal!
So there is probably a different answer for all of the *leftover space* options: 1lb, 2lb, 3lb.

Then, when we're deciding whether to take the next item, we have the *current max* for each of those bucket sizes.
If we have leftover space, we have a pre-computed *maximum value* that we can fit in that space!

