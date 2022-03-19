#!/bin/python


# Recursively calculate the sum of all items in the list starting at "head"
def sum_list(head):
    if head == None:
        return 0
    else:
        return head.value + sum_list(head.next)

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

a = Node(2, None)
b = Node(3, a)
print(sum_list(b))

c = Node(0, b)
print(sum_list(c))

d = Node(10, c)
print(sum_list(d))

