#ifndef LINKED_LIST_H
#define LINKED_LIST_H

struct Node {
    int value;
    struct Node* next;
};

void push_node(struct Node** head_ref, int value);
void delete_list(struct Node** head_ref);
void print_list(const struct Node* head);
struct Node* reverse_list(struct Node** head_ref);

#endif /* LINKED_LIST_H */
