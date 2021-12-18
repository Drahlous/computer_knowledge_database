#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

void push_node(struct Node** head_ref, int value) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->value = value;
    new_node->next = NULL;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }

    struct Node* prev = *head_ref;
    while (prev->next != NULL) {
        prev = prev->next;       
    }

    prev->next = new_node;
}

void delete_list(struct Node** head_ref) {
    struct Node* next = NULL;
    struct Node* curr = *head_ref;
    while (curr != NULL) {
        next = curr->next;

        free(curr);
        curr = next;
    }
    *head_ref = NULL;
}

void print_list(const struct Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->value);
        head = head->next;
    }
    printf("NULL\n");
}

struct Node* reverse_list(struct Node** head_ref) {
    struct Node* prev = NULL;
    struct Node* next = NULL;
    struct Node* curr = *head_ref;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

int main() {
    printf("Testing Linked List Library\n\n");

    struct Node* my_list = NULL;

    printf("pushing nodes...\n");
    push_node(&my_list, 1);
    push_node(&my_list, 15);
    push_node(&my_list, 3);
    print_list(my_list);

    printf("reversing list...\n");
    my_list = reverse_list(&my_list);
    print_list(my_list);

    printf("deleting list...\n");
    delete_list(&my_list);
    print_list(my_list);

    return 0;
}


