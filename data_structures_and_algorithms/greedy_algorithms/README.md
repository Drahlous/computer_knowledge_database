# Greedy Algorithms

The `Greedy Strategy` provides a very fast and simple solution to `optimization` problems.
The concept is straightforward: At every step in the algorithm, take the current-best choice.

Greedy algorithms find `local` optimizations, and don't always give the `globally optimal` best solution.
Despite this they're often good enough, and they're `extremely fast`.


## Common Problems that can be Approximated with a Greedy Solution
The greedy strategy can provide a `good-enough` answer to lots of `optimization` problems.
They don't always provide the most optimal solution, but they can get close.

- Scheduling problems (fit the most events in a given timeframe)

- The Knapsack problem (fit the highest-value items in a bag of limited size)

- Set covering problems (from a group of sets, find the smallest subset that covers every item)

- NP-Complete problems (the optimal solution can only be found be checking every possible combination)


## The Set Datastructure
A set contains a group of items with no duplicates.

- Like a list without duplicates

- Like a hash-table with just keys (not key-value pairs)

```python
first_set = set(["A", "B", "C"])
second_set = set(["C", "D", "E"])
```

A `Set Intersection` is the overlap between two sets
```python
# Contains ["C"]
my_intersection = first_set & second_set
```

A `Union` is the combination of all items in both sets
```python
# Contains ["A", "B", "C", "D", "E"]
my_union = first_set + second_set
```

A `Difference` removes the intersection of the sets
```python
# Contains ["A", "B"]
my_difference = first_set - second_set
```

## Common Traits of NP-Complete problems

- The problem involves computing "All Possible Combinations"

- You're looking to create a sequence of items, but it's not obvious that the finished sequence is the correct answer.
    (e.g. Sorting is a sequence, but not NP-Complete. It's obvious that there is only one correct answer)
