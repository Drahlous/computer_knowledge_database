# Python Syntax

## General
```python
# None serves the same purpose as NULL in other languages
a = None

# Infinity (use like INT_MAX)
float("inf")

```

## Lists
```python
my_list = ["a", "b", "c"]

item = my_list[1]
index = my_list.index("b")

my_list.count()

# Adding Items
my_list.append("d")
my_list.extend(["e", "f", "g"])
my_list.insert(3, "q")

# Removing Items
my_list.remove(3)
item = my_list.pop(3)
last_item = my_list.pop()

# Modify & Sort
my_list.reverse()
my_list.sort()

# Create and return a new copy of the list
list_copy = my_list.copy()

```

## Deque
```python
my_queue = deque()
my_queue += 3

item = my_queue.popleft()

```

## Hash Tables
```python
# The Dictionary structure is python's hash-table
# It essentially uses JSON syntax
my_table = {}
my_table = dict()
my_table["a"] = "1"
my_table["b"] = { "c": "d" }

```
