#include <stdio.h>
#include <stdlib.h>
#include "binary_tree.h"


struct Node* create_node(int value) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->value = value;
    new_node->left  = NULL;
    new_node->right = NULL;

    return new_node;
}

struct Node* insert_node(struct Node* root, struct Node* new_node) {
    if (root == NULL) {
        return new_node;
    } else if (new_node->value < root->value) {
        root->left = insert_node(root->left, new_node);
    } else {
        root->right = insert_node(root->right, new_node);
    }
    return root;
}

struct Node* push_node(struct Node* root, int value) {
    return insert_node(root, create_node(value));
}

void print_tree_dfs(const struct Node* root) {
    if (root != NULL) {
        printf("%d -> ", root->value);
        print_tree_dfs(root->left);
        print_tree_dfs(root->right);
    }
}

int main() {
    printf("Testing Binary Tree Library\n\n");
    struct Node* my_tree = NULL;
    my_tree = push_node(my_tree, 10);
    push_node(my_tree, 15);
    push_node(my_tree, 5);
    print_tree_dfs(my_tree);


    return 0;
}


