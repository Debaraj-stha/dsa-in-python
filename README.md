# Data Structures in Python

This repository contains implementations of various data structures in Python, along with sample code and explanations for each. The goal is to provide a comprehensive reference for understanding and utilizing these data structures in Python programming.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data Structures](#data-structures)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Trees](#trees)
    - [Graphs](#graphs)
    - [Hash Tables](#hash-tables)
    - [Heaps](#heaps)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

This repository provides Python implementations of common data structures. Each data structure is implemented in a separate file with detailed comments and example usage. The aim is to help developers understand the inner workings of these data structures and how to implement them in Python.
I have also included some designand analysis  of algorithms like searching and sorting.

## Installation

To use the data structures in this repository, you can simply clone the repository to your local machine:

```bash
git clone https://github.com/Debaraj-stha/dsa-in-python.git
```

Navigate to the project directory:

```bash
cd dsa
```

## Usage

Each data structure is contained in its own file. To use a data structure, you can import the relevant class into your Python script. For example, to use the `LinkedList` class:

```python
from linked_list import LinkedList

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.display()
```

Refer to the individual files for more detailed usage examples.

## Data Structures

### Arrays

Arrays are a fundamental data structure consisting of a collection of elements, each identified by an index.

File: `arrays.py`

### Linked Lists

Linked lists are a linear data structure where each element is a separate object, with each element (node) pointing to the next element in the sequence.

File: `linked_list.py`

### Stacks

Stacks are a linear data structure that follows the Last In First Out (LIFO) principle. The most recently added element is the first one to be removed.

File: `stack.py`

### Queues

Queues are a linear data structure that follows the First In First Out (FIFO) principle. The first element added is the first one to be removed.

File: `queue.py`

### Trees

Trees are a hierarchical data structure with a root node and child nodes, represented as a set of linked nodes.

File: `tree.py`

### Graphs

Graphs are a collection of nodes connected by edges. They can be used to represent various real-world structures.

File: `graph.py`

### Hash Tables

Hash tables are a data structure that implements an associative array, a structure that can map keys to values efficiently.

File: `hash_table.py`

### Heaps

Heaps are a specialized tree-based data structure that satisfies the heap property. In a max heap, for any given node I, the value of I is greater than or equal to the values of its children.

File: `heap.py`

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bug fix.
3. Make your changes.
4. Submit a pull request with a description of your changes.

Please ensure your code follows the existing style and conventions used in the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code and use these data structures in your projects. If you have any questions or suggestions, please open an issue or submit a pull request. Happy coding!