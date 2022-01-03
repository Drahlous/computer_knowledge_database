#include <iostream>
#include <unordered_map>
#include <string>
#include <utility>
#include <limits>
#include <list>

using namespace std;

class TableEntry {
    public:
        TableEntry() {}
        TableEntry(string name, int cost, bool isProcessed, string parent): name(name), cost(cost), isProcessed(isProcessed), parent(parent) {}
        string name;
        int cost;
        bool isProcessed;
        string parent;
};

using my_graph_t = unordered_map<string,unordered_map<string,int>>;
using my_table_t = unordered_map<string, TableEntry>;

// Table:
// | NodeName | Cost | isProcessed? | Parent Node |


void print_table(unordered_map<string, TableEntry> &node_table) {
    cout << "\n\n";
    for (auto entry : node_table) {
        cout <<
            entry.first                                     << " | " <<
            entry.second.cost                               << " | " <<
            (entry.second.isProcessed ? "True" : "False")   << " | " << 
            entry.second.parent                             << endl; 
    }
    cout << "\n\n";
}


void process_node(string current_node, my_graph_t &graph, my_table_t &node_table) {

    cout << "Processing node: " << current_node << endl;
    // Update neighbors
    for (auto &neighbor : graph[current_node]) {

        // If this neighbor isn't present in the table, it's the first time we've seen it
        if (node_table.find(neighbor.first) == node_table.end()) {
            cout << "first time seeing " << neighbor.first << endl;
            node_table.emplace(neighbor.first, TableEntry(neighbor.first, numeric_limits<int>::max(), false, current_node));
        }

        int new_cost = node_table[current_node].cost + graph[current_node][neighbor.first];
        int old_cost = node_table[neighbor.first].cost;

        if (new_cost < old_cost) {
            node_table[neighbor.first].cost = new_cost;
            node_table[neighbor.first].parent = current_node;
        }
    }

    // Mark this node as processed
    node_table[current_node].isProcessed = true;
}

string get_next_cheapest(my_table_t &table) {
    TableEntry *current_cheapest = nullptr;

    for (auto &row : table) {

        // Find a node that:
        // - hasn't been processed
        // - cheaper than the current best
        if (row.second.isProcessed) {
            continue;
        } else if (!current_cheapest || (row.second.cost < current_cheapest->cost)) {
            current_cheapest = &row.second;
        }
    }

    if (current_cheapest) {
        return current_cheapest->name;
    } else {
        return "";
    }
}

// Build the final path backwards by repeatedly jumping to parent
void get_final_path(my_table_t &table, string start, string end) {
    list<string> final_path;
    string current_node = end;
    while (current_node != "") {
        final_path.push_front(current_node);
        current_node = table[current_node].parent;
    }
    for (auto item: final_path) {
        cout << item << endl;
    }
}

// Find the cheapest path from start to end
int dijkstra(my_graph_t &graph, string start, string end) {

    // Create the node-cost table
    my_table_t table;
    table.emplace(start, TableEntry(start, 0, false, ""));
    print_table(table);

    string current_node = get_next_cheapest(table);
    while (current_node != "" && current_node != end) {

        // Process the current node
        process_node(current_node, graph, table);
        print_table(table);

        // Get the next-cheapest node
        current_node = get_next_cheapest(table);
        print_table(table);
    }
    
    // We've found a path, now unfurl it
    if (current_node == end) {
        get_final_path(table, start, end);
    }

    return 0;
}


int main() {
    cout << "Hello World!" << endl;

    unordered_map<string, unordered_map<string,int>>sample_graph({
        {"start", {
            {"a", 6},
            {"b", 2}
        }},

        {"a", {
            {"end", 1}
        }},

        {"b", {
            {"a", 3},
            {"end", 5}
        }},

        {"end", {
        }}
    });

    dijkstra(sample_graph, "start", "end");

    return 0;
}
