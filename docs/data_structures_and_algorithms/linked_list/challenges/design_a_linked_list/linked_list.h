#ifndef LINKED_LIST_H
#define LINKED_LIST_H
class MyLinkedList {
    public:
        MyLinkedList(): head{nullptr}, tail{nullptr}, length{0} {}

        int get(int index);
        void addAtHead(int val);
        void addAtTail(int val);
        void addAtIndex(int index, int val);
        void deleteAtIndex(int index);

        void print_list();

    private:
        class Node {
            public:
                Node(int val) : val{val}, next{nullptr} {}

                int val;
                Node* next;
        };

        Node* get_node_at(int index);
        Node* create_node(int val, Node* prev);


        Node* head;
        Node* tail;
        int length;
};
#endif /* LINKED_LIST_H */
