# C++ Syntax Reference

## Container Common
```cpp
my_container.front();
my_container.back();

my_container.size();
my_container.empty();

my_container.begin();
my_container.end();

my_container.erase(i);
```

## Vector
```cpp
#include <vector>

vector<int> my_vec;

my_vec.push_back(1);
my_vec.pop_back();

my_vec[0];
my_vec.at(0);

for (auto it : my_vec) {}

// Iterators
my_vec.begin();
my_vec.end();

for (vector<int>::iterator it = my_vec.begin() ; it != my_vec.end(); ++it)
        cout << *it << ' ';

```


## Deque
```cpp
#include <deque>

deque<int> my_deque;

my_deque.push_front(1);
my_deque.push_back(2);

my_deque.pop_front();
my_deque.pop_back();

my_deque.front();
my_deque.back();

```

## Set (Unordered Set)
```cpp
#include <unordered_set>

unordered_set<string> my_set = {"red", "green", "blue"};

auto item = my_set.find("green");

if (item == my_set.end()) {
    cout << "not found";
} else {
    string result  = *item;
}

```

## Hash Table (Unordered Map)
```cpp
#include <unordered_map>

unordered_map<string, int> my_hashmap = {
    {"first", 1},
    {"second", 2} };
my_hashmap["third"] = 3;

auto item = my_hashmap.find("first");

if (item == my_map.end()) {
    cout << "not found";
} else {
    int first = item->first;
    int second = item->second;
}
```

## Binary Search Tree (Map)
```cpp
#include <map>

map<char,int> my_map;

my_map.emplace('a', 100);
for (auto& x: my_map)
    cout << x.first << x.second;
```


