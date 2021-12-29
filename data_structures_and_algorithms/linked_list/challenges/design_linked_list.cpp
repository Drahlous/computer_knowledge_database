class MyLinkedList {
    public:
        MyLinkedList(): head{nullptr}, tail{nullptr}, length{0} {}

        int get(int index) {
            Node* node = get_node_at(index);
            return node ? node->val : -1;
        }

        void addAtHead(int val) {
            create_node(val, head);
        }

        void addAtTail(int val) {
            create_node(val, tail);
        }

        void addAtIndex(int index, int val) {
            if (index < 0 || index > length)
                return;

            if (index == 0)
                addAtHead(val);
            else if (index == length)
                addAtTail(val);
            else 
                create_node(val, get_node_at(index - 1));
        }

        //  0    1    2
        //  a -> b -> c
        void deleteAtIndex(int index) {
            Node* victim = get_node_at(index);
            Node* prev = get_node_at(index - 1);

            if (index < 0 || index > (length - 1)) {
                return;
            }

            // If we're deleting the head, update it
            if (index == 0)
                head = head->next;

            // If we're deleting the tail, update it
            if (index == (length - 1)) {
                tail = prev;
            }

            if (prev)
                prev->next = victim->next;


            delete victim;
            --length;
        }

    private:
        class Node {
            public:
                Node(int val, Node* next) : val{val}, next{next} {}
                int val;
                Node* next;
        };
        Node* head;
        Node* tail;
        int length;

        Node* get_node_at(int index) {
            Node* curr_node = head;
            int i = 0;

            if (index < 0)
                return nullptr;
            else if (index > (length - 1))
                return nullptr;

            while (curr_node) {
                if (i == index)
                    return curr_node;
                ++i;
                curr_node = curr_node->next;
            }

            return curr_node;
        }

        Node* create_node(int val, Node* prev) {
            Node* new_node = new Node(val, nullptr);

            if (prev) {
                new_node->next = prev->next;
                prev->next = new_node;
            }
            else
                head = new_node;


            if (!new_node->next)
                tail = new_node;

            ++length;
            return new_node;
        }
};

