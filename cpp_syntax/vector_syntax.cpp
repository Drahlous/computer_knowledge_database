#include <iostream>
#include <vector>

using namespace std;

int main() {
    std::vector<int> my_vec;

    // Add items
    my_vec.push_back(1);
    my_vec.push_back(2);
    my_vec.push_back(3);

    // Remove back item (does not return!)
    my_vec.pop_back();

    // Get item at front, back, or index
    my_vec.front();
    my_vec[0] = my_vec.at(0);
    my_vec.back();

    // Size info
    my_vec.size();
    bool is_empty = my_vec.empty();

    // Iteration
    my_vec.begin();
    my_vec.end();

    for (auto it : my_vec) {
        cout << it << ' ';
    }
    cout << endl;

    for (vector<int>::iterator it = my_vec.begin() ; it != my_vec.end(); ++it)
        cout << *it << ' ';
    cout << endl;


    return 0;
}

