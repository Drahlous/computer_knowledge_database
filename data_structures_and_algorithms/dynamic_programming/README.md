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


### The Knapsack DP Solution

First, we'll setup the `grid`.
Each `column` represents the solution to the subproblem where `bag-size` is that column number.
Each row is a potential item to steal.

We have a `bag` of `size 4`, so our right-most column will have the value `4lbs`.
The smallest item weighs `1lbs`, this will be the size of our smallest bucket & the increments between buckets.


| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |


Now we can add the rows, one for each item:


| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| Stereo | | | | |
| Laptop | | | | |
| Guitar | | | | |
| Toaster | | | | |


First we'll solve the stereo row:

The stereo won't fit in any of the bags with weights 1 through 3, and we don't know anything better to put in there yet.
It will fit in the 4lb slot though, so we'll mark that one.

| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| Stereo | 0 | 0 | 0 | 3000 {S} |
| Laptop | | | | |
| Guitar | | | | |
| Toaster | | | | |



Now we can solve the `Laptop Row`. It won't fit in the 1lb or 2lb colums. It will fit in the 3lb slot, and we haven't seen a better deal yet, so we'll mark it there.
When we get to the 4lb slot, we can choose to take the previous best (`the cell directly above us, a $3000 stereo`).
Or we can craft a solution with the current item, the `Laptop, which is 3lbs`. 
If we took the laptop, we'd have 1lb of free space leftover that we could fill. We haven't filled any cells in the 1lb column yet, so we can't get any more value than the laptop alone. The stereo is better than the laptop alone, so we'll take that.



| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| Stereo | 0 | 0 | 0 | 3000 {S} |
| Laptop | 0 | 0 | 2000 {L}| 3000 {S} |
| Guitar | | | | |
| Toaster | | | | |



Next we can do the `Guitar Row`.
This one fits in the 1lb and 2lb slots, so we'll take it.
When we get to the 3lb slot, we compare our potential value with the row above us:
We know that we can fill a 3lb slot with a $2000 laptop, or we could grab the guitar to have 2lbs left over.

What's the best thing we can fit in a 2lb slot? The 2lb slot in the row above us tells us that we don't have any valuable choices.
So we'll take the $2000 laptop.
However, the 4lb slot leaves us with 3lbs leftover, so we can add the contents of the 3lb slot from the row above:

$2000 Laptop + $1500 Guitar = $3500

That's better than our other choice for this slot, the $3000 Stereo.

| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| Stereo | 0 | 0 | 0 | 3000 {S} |
| Laptop | 0 | 0 | 2000 {L}| 3000 {S} |
| Guitar | 1500 {G} | 1500 {G} | 2000 {L} | 3500 {L,G} |
| Toaster | | | | |


Finally, the toaster only beats the guitar by itself in the 2lb slot.

| | 1lb | 2lb | 3lb | 4lb |
| --- | --- | --- | --- | --- |
| Stereo | 0 | 0 | 0 | 3000 {S} |
| Laptop | 0 | 0 | 2000 {L}| 3000 {S} |
| Guitar | 1500 {G} | 1500 {G} | 2000 {L} | 3500 {L,G} |
| Toaster | 1500 {G} | 2000 {T,G} | 2000 {L} | 3500 {L,G} |


So our final answer is the contents of the 4lb slot in our last row!
We'll take the Laptop and Guitar for a total of $3500.


### DP Questions and Clarifications

#### What if we add another item, do we have to re-calculate everything?
No, we only need to save the very last row.


#### What if you add an item that's smaller than the smallest bucket?
You need to redistribute the bucket sizes and re-calculate everything.


#### Can you steal fractions of an item?
Not with Dynamic Programming, but you wouldn't want to anyways. If you can take fractions, just use a Greedy Solution instead!


#### Can you have items that depend on eachother? (e.g. buy one get one half off)
No, the problem must be divided into `discrete subproblems`. They cannot be interdependent.


## Key Points
- Dynamic Programming is good when you're trying to `optimize` given a `constraint`

- Every solution will involve creating a `grid`. Your goal is to optimize the `values in the cells`.

- There is `no one-size-fits-all formula`. Instead this is a strategy you can use to think about optimization problems.

