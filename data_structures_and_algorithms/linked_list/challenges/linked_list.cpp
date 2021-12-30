#include "linked_list.h"
#include <iostream>

void MyLinkedList::print_list() {
    Node* curr_node = this->head;
    while (curr_node) {
        std::cout << curr_node->val << " -> ";
        curr_node = curr_node->next;
    }
    std::cout << std::endl;
}

int MyLinkedList::get(int index) {
    Node* node = get_node_at(index);
    return node ? node->val : -1;
}

void MyLinkedList::addAtHead(int val) {
    create_node(val, nullptr);
}

void MyLinkedList::addAtTail(int val) {
    create_node(val, tail);
}

void MyLinkedList::addAtIndex(int index, int val) {
    if (index < 0 || index > length)
        return;
    create_node(val, get_node_at(index - 1));
}

void MyLinkedList::deleteAtIndex(int index) {
    Node* victim = get_node_at(index);
    Node* prev = get_node_at(index - 1);

    if (index < 0 || index > (length - 1)) {
        return;
    }

    // If we're deleting the head, update it
    if (index == 0) {
        head = head->next;
    }

    // If we're deleting the tail, update it
    if (index == (length - 1)) {
        tail = prev;
    }

    if (prev) {
        prev->next = victim->next;
    }

    delete victim;
    --length;
}

MyLinkedList::Node* MyLinkedList::get_node_at(int index) {
    Node* curr_node = head;
    int i = 0;

    if (index < 0 || index > (length - 1)) {
        return nullptr;
    }

    while (curr_node && i < index) {
        ++i;
        curr_node = curr_node->next;
    }

    return curr_node;
}

MyLinkedList::Node* MyLinkedList::create_node(int val, Node* prev) {
    Node* new_node = new Node(val);

    // If there is no previous, this is the new head
    if (!prev) {
        new_node->next = head;
        head = new_node;
    }
    else {
        new_node->next = prev->next;
        prev->next = new_node;
    }

    // If there is no next, this is the new tail
    if (!new_node->next) {
        tail = new_node;
    }

    ++length;
    return new_node;
}

int main() {

    MyLinkedList* my_list = new MyLinkedList();
    my_list->addAtHead(7);
    my_list->print_list();

    my_list->addAtTail(7);
    my_list->print_list();

    my_list->addAtHead(9);
    my_list->print_list();

    my_list->addAtTail(8);
    my_list->print_list();

    my_list->addAtHead(6);
    my_list->print_list();

    my_list->addAtHead(0);
    my_list->print_list();

    std::cout << "Getting index 5: " << my_list->get(5) << std::endl;

    my_list->addAtHead(0);
    my_list->print_list();

    std::cout << "Getting index 2: " << my_list->get(2) << std::endl;

    my_list->print_list();
    
    return 0;
}
