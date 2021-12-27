#!/bin/python

# Based on:
# https://realpython.com/introduction-to-python-generators/


### Generators
#
# Generators are a special type of function,
# they return a Lazy Iterator, which you can loop over like a List.
#
# Lazy Iterators are different from lists in that they do not store their contents in memory
#

### Example 1: Reading Files

# Say we want to read each line in a file.
# We might open the file, read it, and split the buffer at newline characters
from os import wait


def get_lines_naive(filename):

    # open() returns a generator object that you can iterate through lazily
    file = open(filename)

    # However, the split() function insists on loading everything into memory at once to populate the array.
    # This will lead to a MEMORY ERROR
    lines = file.read().split("\n")
    return lines

# To avoid the memory errors, we'll want to use the Generator-Yield paradigm
def get_lines(filename):
    # Create the lazy iterator
    for row in open(filename):
        # Return a generator object instead of holding the line in memory
        yield row



# Recap:
# Yield results in a generator object
# return results in reading only the first line


### Example 2: Infinite Sequence

# We know that we can use range() to generate a finite sequence
def get_finite_sequence(lower, upper):
    # Create a range
    a = range(lower, upper)
    # Return as a List
    return list(a)

# But if we want to generate an infinite sequence, we'll need a generator
def generate_infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Uncomment the following lines to see it working
#for i in generate_infinite_sequence():
#    print(i, end=" ")

# You can also use next() directly on the generator object to get numbers one-at-a-time
gen = generate_infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))



### Understanding Generators
#
# Generators look and act like normal functions, but they use `yield` instead of `return`
#
# `yield` indicates that the value is returned, but unlike return we don't exit the function afterwards
#
# Instead, the STATE of the function is persistent.
# Next time we call next() on the iterator, we jump back into the function at the next line after the `yield`
# It might look something like this:

# def generate_infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# gen = generate_infinite_sequence() 
# we jump into the function,
# create num = 0,
# step into the while loop,
# hit `yield num` and return, but the function remembers where we're at, the next line is num += 1

# Now we call next(gen), causing us to jump back into the function and evaluate until the next `yield`
# increment num `num += 1`
# jump back to the while loop
# yield `num` again

# The concept is very similar to the usage of yield() in the context of parallel programming,
# where you might use `yield` to throw context back to the other thread, then get context again later


### Creating Generators
# You can create generators without binding them to a variable
# This avoids storing the entire object in memory, so you don't take a huge penalty

# Square Brackets: Builds a list from the generator object
nums_squared_lc = [num**2 for num in range(5)]
print(nums_squared_lc)

# Parenthesis: Just return the generator object as is
nums_squared_gc = (num**2 for num in range(5))
print(nums_squared_gc)

