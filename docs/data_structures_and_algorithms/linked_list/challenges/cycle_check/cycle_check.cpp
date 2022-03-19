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

Node* get_cycle_start(Node* head) {
    if (!head) {
        return nullptr;
    }
    Node* follower = head;
    Node* leader = head->next;

    while (leader != follower) {
        if (!leader || !leader->next) {
            return nullptr;
        }
        follower = follower->next;
        leader = leader->next->next;
    }

    // At this point, leader == follower, they both point to a node in the cycle
    
    // We're going to leave the follower pointer in place
    // and repeatedly loop through the cycle with the leader pointer
    //
    // After each cycle, we'll creep the head node one step deeper into the list
    // Every time we move the leader, we'll see if we've bumped into the head
    //
    // This should detect the head on the cycle that it first enters the loop
    while (head != leader) {
        leader = leader->next;
        if (leader == follower) {
            head = head->next;
        }
    }
    return head;
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
    assert(&head == get_cycle_start(&head));

    // Cycle further out
    head.next = &second;
    second.next = &third;
    third.next = &fourth;
    fourth.next = &second;
    assert(check_cycle(&head));
    assert(&second == get_cycle_start(&head));

    return 0;
}
