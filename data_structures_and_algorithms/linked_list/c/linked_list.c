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

void delete_item(struct Node** head_ref, int value_to_delete) {
    struct Node* next = NULL;
    struct Node* curr = *head_ref;

    struct Node* prev = NULL;
    while (curr != NULL) {
        if (curr->value == value_to_delete) {
            prev->next = curr->next;
            free(curr);
            break;
        } else {
            next = curr->next;
            prev = curr;
            curr = next;
        }
    }
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

void print_list_puml(const struct Node* head) {
    printf("@startuml\n");
    printf("skinparam componentStyle rectangle\n");
    printf("left to right direction\n");

    while (head != NULL) {
        printf("[%d] --> ", head->value);
        if (head->next != NULL) {
            printf("[%d]\n", head->next->value);
        } 
        head = head->next;
    }
    printf("[null]\n");
    printf("@enduml\n\n");
}

int main() {
    printf("\" Testing Linked List Library\n\n");

    struct Node* my_list = NULL;

    printf("\" pushing nodes...\n");
    push_node(&my_list, 1);
    push_node(&my_list, 15);
    push_node(&my_list, 3);
    print_list_puml(my_list);

    printf("\" reversing list...\n");
    my_list = reverse_list(&my_list);
    print_list_puml(my_list);

    int item_to_delete = 15;
    printf("\" deleting item %d...\n", item_to_delete);
    delete_item(&my_list, item_to_delete);
    print_list_puml(my_list);

    int item_to_add = 15;
    printf("\" adding item %d...\n", item_to_add);
    push_node(&my_list, 15);
    print_list_puml(my_list);

    item_to_delete = 15;
    printf("\" deleting item %d...\n", item_to_delete);
    delete_item(&my_list, item_to_delete);
    print_list_puml(my_list);

    item_to_delete = 200;
    printf("\" deleting non-existent item %d...\n", item_to_delete);
    delete_item(&my_list, item_to_delete);
    print_list_puml(my_list);

    printf("\" deleting list...\n");
    delete_list(&my_list);
    print_list_puml(my_list);
    return 0;
}


