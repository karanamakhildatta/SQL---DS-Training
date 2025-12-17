DATA STRUCTRURES AND ALGORITHMS - DAY 1

# Day 1: Introduction to Data Structures and Algorithms

## 1.1 What are Data Structures and Algorithms?

Data Structures are ways to organize and store data in a computer so that it can be accessed and modified efficiently. Algorithms are step-by-step procedures or formulas for solving problems or performing tasks.

## 1.2 Common Data Structures

Here are some common data structures:

- **Array**: A collection of elements identified by index or key.
- **Linked List**: A linear collection of elements where each element points to the next.
- **Stack**: A collection of elements that follows the Last In First Out (LIFO) principle.
- **Queue**: A collection of elements that follows the First In First Out (FIFO)
  principle.
- **Hash Table**: A data structure that maps keys to values for efficient lookup.

## 1.3 Basic Algorithms

Here are some basic algorithms:

- **Sorting Algorithms**: Methods to arrange data in a particular order (e.g., Bubble Sort, Merge Sort).
- **Searching Algorithms**: Methods to find specific data within a structure (e.g., Linear
  Search, Binary Search).

ARRAYS & STRINGS

## 2.1 What is an Array?

An array is a collection of elements, each identified by an index or key. Arrays are used to store multiple values in a single variable, making it easier to manage and manipulate data.
Key Terms:

- Fixed Size: The size of an array is determined at the time of its creation in most of the programming languages and cannot be changed.
- Zero Indexing: It start with index 0, meaning the first element is accessed with index 0, the second with index 1, and so on.
- Random Access: Elements in an array can be accessed directly using their index, allowing for efficient retrieval and modification.
- Contiguous Memory: Arrays store elements in contiguous memory locations, which helps in efficient access and cache performance.
  **Visual Representation:**

```
Index:    0     1     2     3     4
        +-----+-----+-----+-----+-----+
Array:  |  10 |  20 |  30 |  40 |  50 |
        +-----+-----+-----+-----+-----+
Address: 100   104   108   112   116  (assuming 4 bytes per integer)
```

## 2.2 Array Operations in Code

Here are some common operations performed on arrays using Python:

```python
# Creating an array
arr = [10, 20, 30, 40, 50]
# Accessing elements
first_element = arr[0]  # 10
second_element = arr[1]  # 20
# Modifying elements
arr[2] = 35  # arr is now [10, 20, 35, 40, 50]
# Adding elements (not typical for fixed-size arrays, but possible in dynamic arrays/lists)
arr.append(60)  # arr is now [10, 20, 35, 40, 50, 60]
# Removing elements
arr.remove(20)  # arr is now [10, 35, 40,
# 50, 60]
```

## 2.3 Array Traversal

Array traversal refers to the process of accessing each element in an array sequentially. This is often done using loops.

Problem 1:
Write a python code to forward traverse an array and print each element.

Problem 2:
Write a python code to backward traverse an array and print each element.

### 2.4 Time & Space Complexity (Big O Notation)

Big O notation describes how the runtime or space requirements of an algorithm grow as the input size increases.

**Common Time Complexities (from fastest to slowest):**

| Notation   | Name         | Example                          |
| ---------- | ------------ | -------------------------------- |
| O(1)       | Constant     | Accessing array element by index |
| O(log n)   | Logarithmic  | Binary search                    |
| O(n)       | Linear       | Linear search, array traversal   |
| O(n log n) | Linearithmic | Merge sort, quick sort           |
| O(n²)      | Quadratic    | Nested loops, bubble sort        |
| O(2ⁿ)      | Exponential  | Recursive fibonacci (naive)      |

**Visual Growth Comparison:**

```
n = 10:
O(1)      → 1
O(log n)  → 3.3
O(n)      → 10
O(n log n)→ 33
O(n²)     → 100
O(2ⁿ)     → 1024

n = 100:
O(1)      → 1
O(log n)  → 6.6
O(n)      → 100
O(n log n)→ 664
O(n²)     → 10,000
O(2ⁿ)     → 1.27 × 10³⁰ (impossibly large!)
```

```python
# O(1) - Constant Time
def getFirstElement(arr):
# O(n) - Linear Time
def find_sum(arr):
# O(n²) - Quadratic Time
def print_pairs(arr):

# Space Complexity:

# O(1) Space - Uses fixed extra space
def find_max(arr):

def double_array(arr):

```

## 2.5 Array Operations Complexity

| Operation             | Time Complexity | Explanation                   |
| --------------------- | --------------- | ----------------------------- |
| Access by index       | O(1)            | Direct memory calculation     |
| Search (unsorted)     | O(n)            | Must check each element       |
| Search (sorted)       | O(log n)        | Binary search                 |
| Insert at end         | O(1)            | Direct placement              |
| Insert at beginning   | O(n)            | Shift all elements            |
| Insert at middle      | O(n)            | Shift elements after position |
| Delete from end       | O(1)            | Direct removal                |
| Delete from beginning | O(n)            | Shift all elements            |

## 2.6 Basic Array Patterns

Maximum/Minimum Element:

```python
def find_max(arr):
```

Counting Elements:

```python
def count_occurrences(arr, target):
```

Reversing an Array (In-Place):

```python
def reverse_array(arr):
```

Linear Search:

```python
def linear_search(arr, target):
```

Two Pointers:

```python
def remove_duplicates(arr):
def merge_sorted_arrays(arr1, arr2):
def move_zeros_to_end(arr):
def sorted_squares(arr):
```

Array Traversal:

```python
def plus_one(arr):
```

Searching:

```python
def binary_search(arr, target):
def linear_search(arr, target):
```

Hashing:

```python
def two_sum(arr, target):
```
