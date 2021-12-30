# Challenge: Design a Linked List

Design a singly linked list such that each node has a `val` and `next` attribute.

Implement the `MyLinkedList` class:

- `int get(int index)` get the value of the node at index. If the index is invalid, return `-1`

- `void addAtHead(int val)` add a node with value `val` before the first element. The new node becomes the head of the list.

- `void addAtTail(int val)` append a node with value `val` at the end of the list.

- `void addAtIndex(int index, int val)` insert a node with value `val` at the specified `index`. If `index` equals the length of the list, append to the end. If the index is invalid, do not insert the node.

- `void deleteAtIndex(int index)` delete the node at the specified `index`. If `index` is invalid, do nothing.

## Constraints:
- 0 <= index, val <= 1000
- at most 200 calls

"MyLinkedList",
7 "addAtHead",
7 "addAtTail",
9 "addAtHead",
8 "addAtTail",
6 "addAtHead",
0 "addAtHead",
5 "get",        => 8
0 "addAtHead",
2 "get",        => 6
5 "get",        => 7
4 "addAtTail"
