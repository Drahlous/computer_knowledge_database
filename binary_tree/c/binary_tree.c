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
    } else if (new_node->value == root->value) {
        free(new_node);
        return root;
    } else if (new_node->value < root->value) {
        root->left = insert_node(root->left, new_node);
    } else {
        root->right = insert_node(root->right, new_node);
    }
    return root;
}

struct Node* find_node(struct Node* root, int value_to_find) {
    if (root == NULL) {
        return NULL;

    } else if (value_to_find == root->value) {
        return root;

    } else if (value_to_find < root->value) {
        return find_node(root->left, value_to_find);

    } else {
        return find_node(root->right, value_to_find);
    }
}

struct Node* push_node(struct Node* root, int value) {
    return insert_node(root, create_node(value));
}

void print_subtrees(const struct Node* root, int prefix_count, char prefix_char) {
    if (root != NULL) {
        ++prefix_count;
        for (int i = 0; i < prefix_count; ++i) {
            printf("*");
        }
        printf("%c ", prefix_char);

        printf("%d\n", root->value);
        print_subtrees(root->left, prefix_count, '<');
        print_subtrees(root->right, prefix_count, '>');
    }
}

void print_plantuml_tree(const struct Node* root) {
    printf("@startwbs\n");
    print_subtrees(root, 0, ' ');
    printf("@endwbs\n");
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Provide at least one integer argument\n");
        return 1;
    }

    struct Node* my_tree = NULL;
    my_tree = push_node(my_tree, atoi(argv[1]));

    for(int i = 2; i < argc; ++i) {
        push_node(my_tree, atoi(argv[i]));
    }

    print_plantuml_tree(my_tree);

    return 0;
}


