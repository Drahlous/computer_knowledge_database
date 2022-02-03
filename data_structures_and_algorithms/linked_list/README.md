# Linked Lists

## Overview

A Linked List is a set of elements where each node stores the address of the next node.

## Advantages of Linked Lists over Arrays

Imagine you're at lunch with a group of four friends. You'd like to sit together at one table, so you take a small table with four spots.
You sit down and start enjoying your meal, when a fifth friend shows up. Now, everybody has to stand up as a group and look for a bigger table.

This is the same problem we see with adding elements to contiguous arrays. We have to store all of the elements in the same area of memory. If we need more memory, we have to move ALL of the elements to a new segment. This can be very expensive!

This is called `random insertion`, which `Linked Lists` are really `good` at!

### Insertion Complexity

- `Linked List: O(1)`
- `Array:       O(n)`

## Disadvantages of Linked Lists over Arrays

Have you ever visited one of those clickbait "Top Ten Bands of All Time" websites, where each item is a separate webpage?
They start you all the way at number 10 so you have to click the `next` button over and over to who the number one pick is.
You'd really rather jump right to the front and get it over with.

This is called `random access`, and `Linked Lists` are really `bad` at it.

Every time you want to access an item, you have to start at the head and work your way down.

### Reading Complexity

- `Linked List: O(n)`
- `Array:       O(1)`

## Summary

Linked Lists are useful if you're:

- Doing lots of `inserts`

- Don't need to do `random read` often

- Are planning to read every element anyway
