#ifndef BINARY_TREE_H
#define BINARY_TREE_H

struct Node {
    int value;
    struct Node* left;
    struct Node* right;
};

struct Node* push_node(struct Node*, int);
void delete_tree(struct Node*);
void print_tree(const struct Node*);
struct Node* invert_tree(struct Node*);

#endif /* BINARY_TREE_H */
