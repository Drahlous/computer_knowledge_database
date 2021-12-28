# Hash Tables


## Overview
`Hash Tables` allow you to do very quick lookup (random access) for unordered datasets.
They go by several other names:
- `Maps` / `Hash Maps` (C/C++)
- `Dictionaries` (Python)
- `Associative Arrays` (Bash)


## Hash Functions
Hash functions are mathematical operations that take `strings` as input, and provide `numbers` as output.
- Insert a unique `string` and get a unique `number`
- Output is consistently linked to input (the function gives the same output every time)
- Different inputs shouldnt map to the same output (`collision`)

A `hash table` simply uses a `hash function` to map `strings` into positions of an `array`.


## Usecases
- Need fast lookup for unordered (non-sequential) data

- Preventing duplicate entries

- Use as a cache (remember recently used data)

- Model relationships between one object and another



## Hash Collisions
We said that hash functions always map different `keys` to different `slots`.
In reality, it's really hard to make a hash function where every input gives a different output.

### Dealing with Collisions
The simplest way to deal with a collision is to replace the entry at a location with a linked list.
Each overlapping entry would be contained in the list.

Doing this too much can severly decrease the performance of the table, since you end up with a linked list, right?



## Hash Table Performance

| | Average | Worst |
| --- | --- | --- |
| Search | `O(1)` | `O(n)` |
| Insert | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |


To improve performance, we need to limit collisions: 
- Keep a low `Load Factor`
- Use a good `Hash Function` (it should spread items around very evenly)

### Load Factor

Load factor: `(number_of_filled_slots / total_number_of_slots)`

It's generally a good idea to keep the load factor under `0.7`

When you have to increase the size of the array, you should `double the size`.
This will `ammortize` the resizing complexity

