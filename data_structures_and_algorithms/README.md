# Data Structures and Algorithms

Note:
A significant portion of the DSA information contained within this repository is adopted from the book [Grokking Algorithms](https://github.com/egonSchiele/grokking_algorithms).
While several of the coding samples in this repo follow the book very closely, others are my own (sometimes hacky) implementations.

## Table of Contents

1. [Selection Sort](./sorting/selection_sort/README.md)

2. [Recursion](./recursion/README.md)

3. [Quicksort](./sorting/quicksort/README.md)

4. [Hash Tables](./hash_table/README.md)

5. [Breadth First Search](./graphs/breadth_first_search/README.md)

6. [Dijkstra's Algorithm](./graphs/dijkstra/README.md)

7. [Greedy Algorithms](./greedy_algorithms/README.md)

8. [Dynamic Programming](./dynamic_programming/README.md)

## Common Big O Run times

- `O(log n):` Logarithmic time, binary search

- `O(n):` Linear time, simple search

- `O(n * log n)`: Fast sorting algorithms

- `O(n^2)`: Slow sorting algorithms, bubble sort

- `O(n!)`: Factorial, traveling salesman

## PlantUML Diagrams

### Install Pre-requisites

```bash
# Install Java
sudo apt install default-jre

# Install Graphvis
sudo apt install graphviz

# Download PlantUML jar to ~/.local/bin/plantuml.jar
curl -L -o ~/.local/bin/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

# Check that PlantUML is installed correctly
java -jar ~/.local/bin/plantuml.jar

# Install feh to view output PNG
sudo apt install feh

# Alternative: Use water-uml to render a live view
sudo npm i -g water-plant-uml

```

### Generate Diagrams from puml file

```bash
# Render a PUML file into a PNG
java -jar ~/.local/bin/plantuml.jar exampleDiagram.puml

# View the PNG
feh exampleDiagram.png

# Live View:
water-uml live exampleDiagram.puml
```
