#include <deque>

using namespace std;

int main() {
    deque<int> my_deque;

    my_deque.push_front(1);
    my_deque.push_back(2);

    // These do not return!
    my_deque.pop_front();
    my_deque.pop_back();

    my_deque.front();
    my_deque.back();

    return 0;
}
