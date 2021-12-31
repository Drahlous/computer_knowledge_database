#include <iostream>
#include <assert.h>

using namespace std;

class Node {
    public:
        Node(int val, Node* next): val{val}, next{next} {}
        int val;
        Node* next;
};

// Return true if we find a cycle
bool check_cycle(Node* head) {
    Node* leader = head;
    Node* follower = head;
    while (leader) {
        leader = leader->next;
        if (!leader) {
            return false;
        } else if (leader == follower) {
            return true;
        } else {
            follower = follower->next;
            leader = leader->next;
        }
    }
    return false;
}

int main() {
    Node head(1, nullptr);
    Node second(2, nullptr);
    Node third(3, nullptr);
    Node fourth(4, nullptr);

    // Create a single-entry list
    head.next = nullptr;
    assert(!check_cycle(&head));

    // Two items, No cycles
    head.next = &second;
    second.next = nullptr;
    assert(!check_cycle(&head));

    // Add a cycle
    head.next = &second;
    second.next = &head;
    assert(check_cycle(&head));

    // Cycle further out
    head.next = &second;
    second.next = &third;
    third.next = &fourth;
    fourth.next = &second;
    assert(check_cycle(&head));

    return 0;
}
