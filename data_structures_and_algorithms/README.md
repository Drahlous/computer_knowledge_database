# Data Structures and Algorithms

### Note
A significant portion of the DSA information contained within this repository is adopted from the book [Grokking Algorithms](https://github.com/egonSchiele/grokking_algorithms).
While several of the coding samples in this repo follow the book very closely, others are my own (sometimes hacky) implementations.
If you're looking for strictly accurate implementations, I would encourage that you use caution and remain skeptical of the code provided here.

Otherwise, please join me in exploring a selection of topics across computer science! 

## Common Big O Run times
- `O(log n):` Logarithmic time, binary search

- `O(n):` Linear time, simple search

- `O(n * log n)`: Fast sorting algorithms

- `O(n^2)`: Slow sorting algorithms, bubble sort

- `O(n!)`: Factorial, traveling salesman


## Python Syntax

General
```python
# None serves the same purpose as NULL in other languages
a = None

# Infinity (use like INT_MAX)
float("inf")

```

Lists
```python
my_list = ["a", "b", "c"]

# Get the number of elements in the list
count = my_list.count()

# yields "b"
item = my_list[1]

# yields "1"
index = my_list.index("b")

# Append to the end
my_list.append("d")

# Append another iterable (Note that this has no return value)
my_list.extend(["e", "f", "g"])

# Insert an element at the index, elements after are shifted right
my_list.insert(3, "q")

# Remove an element at an index, shift remaining elements left
my_list.remove(3)

# Remove an element at an index, but also return it
item = my_list.pop(3)
# The index argument is optional, default behavior is the last item [-1]
last = my_list.pop()

# Reverse the list (modify existing list, no return value)
my_list.reverse()

# Sort the List
my_list.sort()

# Create and return a new copy of the list
list_copy = my_list.copy()

```


Hash Tables
```python
# The Dictionary structure is python's hash-table
# It essentially uses JSON syntax
my_table = {}
my_table = dict()
my_table["a"] = "1"
my_table["b"] = { "c": "d" }
```



## PlantUML Diagrams

### Install Pre-requisites:
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
