# Interview Code Book

### 🔰 Beginner Level
- 1️⃣ [Arrays & Hashing](#1️⃣-arrays--hashing)
- 2️⃣ [Strings](#2️⃣-strings)
- 3️⃣ [Sorting](#3️⃣-sorting)
### 🟢 Intermediate Level
- 4️⃣ [Stack](#4️⃣-stack)
- 5️⃣ [Queue & Heap (Priority Queue)](#5️⃣-queue--heap)
- 6️⃣ [Linked Lists](#6️⃣-linked-lists)

### 🚀 Advanced Level
- 7️⃣ Trees & Graphs (DFS, BFS, Dijkstra’s Algorithm)
- 8️⃣ Recursion & Backtracking (Subsets, Permutations, Sudoku Solver)
- 9️⃣ Dynamic Programming (DP) (Knapsack, Memoization, State Transition)
- 🔟 Bit Manipulation (XOR Tricks, Counting Bits, Power of Two)

## 1️⃣ Arrays & Hashing
### Lists
```python
names = ['Badhan', 'Anik', 'Alamin']
ages = [30, 29, 29]
for name, age in zip(names, ages):
    print(name, age)

"""Output
Badhan 30
Anik 29
Alamin 29
"""
```

### Resizable List Part 1

**Description**:
Lists in Python are resizable, meaning you can add elements to them using methods like `append()` or `extend()`.

**Example**:

```python
my_list = [1, 2, 3]
my_list.append(4)        # Adds a single element to the end
print(my_list)           # Output: [1, 2, 3, 4]
```

### Resizable List Part 2

**Description**:
Lists can also be resized by removing elements using methods like `remove()`, `pop()`, or `del`.

**Example**:

```python
my_list = [1, 2, 3, 4]
my_list.pop()            # Removes and returns the last item
print(my_list)           # Output: [1, 2, 3]
my_list.remove(2)        # Removes the first occurrence of the value
print(my_list)           # Output: [1, 3]
```

### List Concat

**Description**:
Lists can be concatenated using the `+` operator or the `extend()` method.

**Example**:

```python
list1 = [1, 2]
list2 = [3, 4]
concatenated_list = list1 + list2  # Using +
print(concatenated_list)           # Output: [1, 2, 3, 4]
list1.extend(list2)                # Using extend()
print(list1)                       # Output: [1, 2, 3, 4]
```

### List Initialization

**Description**:
Lists can be initialized in various ways, including using list literals or comprehensions.

**Example**:

```python
empty_list = []                      # Empty list
list_with_values = [1, 2, 3]         # List with initial values
list_from_range = list(range(5))     # List from range
print(list_from_range)               # Output: [0, 1, 2, 3, 4]
```

### List Clone

**Description**:
Cloning a list can be done using slicing or the `copy()` method.

**Example**:

```python
original_list = [1, 2, 3]
cloned_list = original_list[:]       # Using slicing
print(cloned_list)                   # Output: [1, 2, 3]
another_clone = original_list.copy() # Using copy()
print(another_clone)                 # Output: [1, 2, 3]
```

### List Comprehension

**Description**:
List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause.

**Example**:

```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

### List methods

```python
list.pop(i) # O(n)
list.insert(i, val) # O(n)
```

### 2D or 3D list

**Description**: 2D and 3D List Comprehension. You want to create a `n x m` or `l x n x m` grids. Just follow the dimension in reverse order.

**Example**:
```python
n = 4  # Number of rows
m = 5  # Number of columns
default_value = 0  # Default value for each cell

# Create n x m 2D grid
grid_2d = [[default_value for _ in range(m)] for _ in range(n)]

# Print the 2D grid
for row in grid_2d:
    print(row)
    
"""Output
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
"""

l = 3  # Number of layers
n = 4  # Number of rows
m = 5  # Number of columns
default_value = 0  # Default value for each cell

# Create l x n x m 3D grid
grid_3d = [[[default_value for _ in range(m)] for _ in range(n)] for _ in range(l)]

# Print the 3D grid
for layer in grid_3d:
    print("Layer:")
    for row in layer:
        print(row)

"""Output
Layer:
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
Layer:
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
Layer:
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
"""
```

### Hashmaps and Hashsets
**Description**:  
Hashmaps and Hashsets are data structures that provide efficient storage and retrieval of data using a hash-based mechanism.  
- **Hashmaps** (or dictionaries in Python) store key-value pairs, allowing quick access to values based on their keys.  
- **Hashsets** store unique elements and are optimized for fast membership checks.

**Hashmaps Example**:
```python
# Initialize a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Access Methods
value = my_dict.get('d', 0)  # O(1)
keys = my_dict.keys()        # O(1)
values = my_dict.values()    # O(1)
items = my_dict.items()      # O(1)

# Using a for loop
for key in my_dict:
    print(key)

# Using the dict.keys() method
for key in my_dict.keys():
    print(key)

# Using the dict.values() method
for value in my_dict.values():
    print(value)

# Using the dict.items() method
for key, value in my_dict.items():
    print(key, value)

# Modification Methods
popped_value = my_dict.pop('b', 0)  # O(1)
popped_item = my_dict.popitem()     # O(1), Removes and returns the last inserted item
my_dict.update({'d': 4, 'e': 5})    # O(k), where k is the number of items being added
my_dict.clear()                     # O(n)
copy_dict = my_dict.copy()          # O(n)
value = my_dict.setdefault('z', 30) # O(1)

# Check Key Existence
if 'x' in my_dict:  # O(1)
    print('Key exists')

# Create a dictionary of squares
squares = {x: x*x for x in range(6)}  # O(n)

# defaultdict
from collections import defaultdict

# Create a default dictionary with int as the default factory
# The key will be the default value of int, which is 0.
dict1 = defaultdict(int)

# Create a defaultdict with -1 as the default value
dict2 = defaultdict(lambda: -1)

default_dict = defaultdict(int)  # O(1)
default_dict['a'] += 1           # O(1)

# Counter
from collections import Counter
counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])  # O(n)
print(counter.most_common(2))  # O(k log k), where k is the number of unique elements

# Tuples as Keys
tuple_keys = {(1, 2): 'a', (3, 4): 'b'}  # O(1) for access and insertion
tuple_keys[(5, 6)] = 'c'

from collections import Counter

# Sample counter map
counter_map = Counter({'a': 5, 'b': 1, 'c': 3, 'd': 4})

# Sorting using sorted() function
sorted_items = sorted(counter_map.items(), key=lambda x: x[1], reverse=True)
# This will create a list not map

# Printing sorted items
print(sorted_items) # [('a', 5), ('d', 4), ('c', 3), ('b', 1)]
```
### Time Complexity Table

| **Operation**            | **Time Complexity** |
|---------------------------|---------------------|
| Access (`get`, `keys`, etc.) | `O(1)`                |
| Insert/Update             | `O(1)`                |
| Delete (`pop`, `popitem`) | `O(1)`                |
| Copy                      | `O(n)`                |
| Clear                     | `O(n)`                |
| Comprehension             | `O(n)`                |
| `defaultdict` Access      | `O(1)`                |
| Counter Initialization    | `O(n)`                |
| Counter `most_common`     | `O(k log k)`          |
| Tuple Key Access          | `O(1)`                |

**Hashsets Example**:
```python
# Set
s = {1, 2, 3}

s.clear()  # O(1), Clear the set

s = {1, 2, 3}
s.add(4)  # O(1)
print("After add(4):", s) # {1, 2, 3, 4}

# Remove element (throws KeyError if item is not present)
s.remove(2)  # O(1)
print("After remove(2):", s) # {2, 3, 4}

# Discard element (no error if item is not present)
s.discard(5)  # O(1)
s.remove(3)   # O(1)
print("After discard(5) and remove(3):", s) # {2, 4}

# Pop a random element
popped_item = s.pop()  # O(1), removes random item (since unordered)
print(f"Popped item: {popped_item}")
print("After pop():", s)

# Set Comparisons
A = {1, 2, 3}
B = {3, 4, 5}

# Check if sets are disjoint (no common elements)
print("A.isdisjoint(B):", A.isdisjoint(B))  # False (O(min(len(A), len(B))))

# Check if A is subset of B (A <= B)
print("A.issubset(B):", A.issubset(B))  # False (O(min(len(A), len(B))))

# Check if A is superset of B (A >= B)
print("A.issuperset(B):", A.issuperset(B))  # False (O(min(len(A), len(B))))

# Set Operations
# Difference: Returns elements in A but not in B
print("A.difference(B):", A.difference(B))  # {1, 2} (O(len(A)))

# Update A with difference of B
A.difference_update(B)  # O(len(B))
print("After A.difference_update(B):", A)

# Intersection: Returns elements in both A and B
A = {1, 2, 3}
print("A.intersection(B):", A.intersection(B))  # {3} (O(min(len(A), len(B))))

# Update A with intersection of A and B
A.intersection_update(B)  # O(min(len(A), len(B)))
print("After A.intersection_update(B):", A)

# Symmetric Difference: Returns elements in A or B but not both
A = {1, 2, 3}
print("A.symmetric_difference(B):", A.symmetric_difference(B))  # {1, 2, 4, 5} (O(len(A) + len(B)))

# Update A with symmetric difference of A and B
A.symmetric_difference_update(B)  # O(len(A) + len(B))
print("After A.symmetric_difference_update(B):", A)

# Union Operations
A = {1, 2, 3}
B = {3, 4, 5}

# Union: Returns elements in A or B (without duplicates)
print("A.union(B):", A.union(B))  # {1, 2, 3, 4, 5} (O(len(A) + len(B)))

# Update A with the union of A and B
A.update(B)  # O(len(B))
print("After A.update(B):", A)
```
### Time Complexity Table

| **Operation**                  | **Time Complexity**          |
|--------------------------------|------------------------------|
| `add(item)`                    | `O(1)`                      |
| `remove(item)`                 | `O(1)` (throws `KeyError` if item not found) |
| `discard(item)`                | `O(1)`                      |
| `pop()`                        | `O(1)`                      |
| `isdisjoint(setB)`             | `O(min(len(A), len(B)))`     |
| `issubset(setB)`               | `O(min(len(A), len(B)))`     |
| `issuperset(setB)`             | `O(min(len(A), len(B)))`     |
| `difference(setB)`             | `O(len(A))`                 |
| `difference_update(setB)`      | `O(len(B))`                 |
| `intersection(setB)`           | `O(min(len(A), len(B)))`     |
| `intersection_update(setB)`    | `O(min(len(A), len(B)))`     |
| `symmetric_difference(setB)`   | `O(len(A) + len(B))`         |
| `symmetric_difference_update(setB)` | `O(len(A) + len(B))`   |
| `union(setB)`                  | `O(len(A) + len(B))`         |
| `update(setB)`                 | `O(len(B))`                 |

### 2️⃣ Strings
**Description**:  
In Python, a string is a sequence of characters enclosed within single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). 

> Strings are immutable, meaning their content cannot be changed after creation. Python provides a rich set of methods and operations to manipulate and process strings efficiently.

**Example**:
```python
from collections import Counter

# Example string
s = "hello world"
print("Original string:", s)  # Output: hello world

# 1. Length of the string
print("Length of string:", len(s))  # O(1), Output: 11

# 2. Strip whitespace
s_padded = "   hello world   "
print("Stripped:", s_padded.strip())  # O(n), Output: hello world
print("Left Stripped:", s_padded.lstrip())  # O(n), Output: hello world   
print("Right Stripped:", s_padded.rstrip())  # O(n), Output:    hello world

# 3. Split and join
fruits = "apple,banana,cherry"
fruit_list = fruits.split(",")  # O(n)
print("Split into list:", fruit_list)  # Output: ['apple', 'banana', 'cherry']
print("Joined with ', ':", ", ".join(fruit_list))  # O(n), Output: apple, banana, cherry

# 4. Finding substrings
print("First occurrence of 'o':", s.find("o"))  # O(n), Output: 4
print("Last occurrence of 'o':", s.rfind("o"))  # O(n), Output: 7
print("Index of 'world':", s.index("world"))  # O(n), Output: 6

# 5. Replace substrings
print("Replace 'world' with 'Python':", s.replace("world", "Python"))  # O(n), Output: hello Python

# 6. Count occurrences
print("Count of 'l' in string:", s.count("l"))  # O(n), Output: 3

# 7. Startswith and endswith
print("Starts with 'hello':", s.startswith("hello"))  # O(n), Output: True
print("Ends with 'world':", s.endswith("world"))  # O(n), Output: True

# 8. Check for alpha, digit, alphanumeric, and whitespace
sample = "abc123"
print("Is alpha:", sample.isalpha())  # O(n), Output: False
print("Is digit:", "123".isdigit())  # O(n), Output: True
print("Is alphanumeric:", sample.isalnum())  # O(n), Output: True
print("Is whitespace:", "   ".isspace())  # O(n), Output: True

# 9. Changing case
print("Uppercase:", s.upper())  # O(n), Output: HELLO WORLD
print("Lowercase:", s.lower())  # O(n), Output: hello world
print("Capitalized:", s.capitalize())  # O(n), Output: Hello world
print("Title case:", s.title())  # O(n), Output: Hello World

# 10. ASCII and Unicode conversions
print("ASCII value of 'a':", ord('a'))  # O(1), Output: 97
print("Character for ASCII 97:", chr(97))  # O(1), Output: a

# 11. Checking substring existence
print("'world' in string:", "world" in s)  # O(n), Output: True

# Palindrome check
def is_palindrome(st):
    st = st.lower()
    return st == st[::-1]  # O(n)

print("Is 'Madam' a palindrome?", is_palindrome("Madam"))  # Output: True

# Character frequency count
frequency = Counter(s)  # O(n)
print("Character frequency:", frequency)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)  # O(n log n)

print("Is 'listen' an anagram of 'silent'?", is_anagram("listen", "silent"))  # Output: True

# Removing duplicates
def remove_duplicates(st):
    return "".join(dict.fromkeys(st))  # O(n)

print("Remove duplicates from 'aabbcc':", remove_duplicates("aabbcc"))  # Output: abc
```
### String Operations Time Complexity Table

| **Operation**                     | **Time Complexity** | **Description**                                                                 |
|------------------------------------|---------------------|---------------------------------------------------------------------------------|
| `len(s)`                          | `O(1)`              | Get the length of the string.                                                  |
| `strip()`, `lstrip()`, `rstrip()` | `O(n)`              | Remove leading/trailing whitespace.                                            |
| `split(delimiter)`                | `O(n)`              | Split the string into a list based on the delimiter.                           |
| `join(list)`                      | `O(n)`              | Join a list of strings into a single string.                                   |
| `find(substring)`                 | `O(n)`              | Find the first occurrence of a substring. Returns `-1` if not found.           |
| `rfind(substring)`                | `O(n)`              | Find the last occurrence of a substring. Returns `-1` if not found.            |
| `index(substring)`                | `O(n)`              | Find the first occurrence of a substring. Raises `ValueError` if not found.    |
| `replace(old, new)`               | `O(n)`              | Replace all occurrences of a substring with another substring.                 |
| `count(substring)`                | `O(n)`              | Count the occurrences of a substring in the string.                            |
| `startswith(prefix)`              | `O(n)`              | Check if the string starts with the given prefix.                              |
| `endswith(suffix)`                | `O(n)`              | Check if the string ends with the given suffix.                                |
| `isalpha()`                       | `O(n)`              | Check if all characters in the string are alphabetic.                          |
| `isdigit()`                       | `O(n)`              | Check if all characters in the string are digits.                              |
| `isalnum()`                       | `O(n)`              | Check if all characters in the string are alphanumeric.                        |
| `isspace()`                       | `O(n)`              | Check if all characters in the string are whitespace.                          |
| `upper()`, `lower()`              | `O(n)`              | Convert the string to uppercase or lowercase.                                  |
| `capitalize()`                    | `O(n)`              | Capitalize the first character of the string.                                  |
| `title()`                         | `O(n)`              | Convert the string to title case.                                              |
| `ord(char)`                       | `O(1)`              | Get the ASCII value of a character.                                            |
| `chr(ascii_value)`                | `O(1)`              | Get the character corresponding to an ASCII value.                             |
| `'substring' in string`           | `O(n)`              | Check if a substring exists in the string.                                     |
| `st[::-1]`                        | `O(n)`              | Reverse the string (used for palindrome check).                                |
| `Counter(string)`                 | `O(n)`              | Count the frequency of each character in the string.                           |
| `sorted(string)`                  | `O(n log n)`        | Sort the characters of the string (used for anagram check).                    |
| `dict.fromkeys(string)`           | `O(n)`              | Remove duplicates from the string while preserving order.                      |

## 3️⃣ Sorting

### **Sort Ascending**

By default, the `.sort()` method sorts the elements in *ascending* order *in-place*. The return value of the `.sort()` method is `None`. By default, strings are sorted in **lexicographical order.**

```python
elements = [5, 3, 6, 2, 1]
elements.sort()
print(elements) # [1, 2, 3, 5, 6]

elements = ["grape", "apple", "banana", "orange"]
elements.sort()
print(elements) # ['apple', 'banana', 'grape', 'orange']
```

### **Sort Descending**

```python
def sort(key=None, reverse=False) -> None:
```

1. The `key` parameter allows us to customize the sorting order. 
2. The `reverse` parameter is a boolean value that determines whether the list should be sorted in *descending order*. By default, it is set to `False`.

```python
elements = [5, 3, 6, 2, 1]
elements.sort(None, True)
# elements.sort(True)
print(elements) # [6, 5, 3, 2, 1]
```

### Sort Custom

We can also specify a custom sorting order by using the `key` parameter in the `.sort()` method. The `key` parameter doesn't accept a value, instead, it accepts a *function* that returns a value to be used for sorting.

```python
def get_word_length(word: str) -> int:
    return len(word)
words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]
words.sort(key=get_word_length)
print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']

# Problem link: https://leetcode.com/problems/reorder-data-in-log-files/
# AC, LC:Badhansen
class Solution:
    def sort_by_requirements(self, log: str) -> tuple:
        identifier, content = log.split(" ", 1)
        if content[0].isdigit():
            return (1, "", "")
        else:
            return (0, content, identifier)

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key=self.sort_by_requirements)
        return logs
```

Defining a separate function just to pass it into the `key` parameter of the `.sort()` method can be cumbersome. We can use a *lambda function* to define a function in a single line and pass it directly to the `.sort()` method.

```python
words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]
words.sort(key=lambda word: len(word))
print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
```

The lambda function `lambda word: len(word)` is equivalent to the function `get_word_length` we defined in the previous example. It takes a word as input and returns the length of the word.

---

To turn a `Counter` object (from Python's `collections` module) into a sorted list, you have a couple of options depending on how you want the sorting to work. Here are common ways to convert a `Counter` to a sorted list:

```python
from collections import Counter

# Example Counter object
counter = Counter({'apple': 3, 'banana': 2, 'orange': 5})

# 1. Sort by count (descending order)
sorted_by_count_desc = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print("Sorted by count (descending):", sorted_by_count_desc)

# 2. Sort by count (ascending order)
sorted_by_count_asc = sorted(counter.items(), key=lambda x: x[1])
print("Sorted by count (ascending):", sorted_by_count_asc)

# 3. Sort by key (alphabetical order)
sorted_by_key = sorted(counter.items())
print("Sorted by key:", sorted_by_key)

```

### **Sorted Copy**

There is another way to sort a list in Python, using the `sorted()` function. The `sorted()` function returns a *new list* with the elements sorted in the specified order. The original list remains unchanged.

```python
words = ["kiwi", "pear", "apple", "banana", "cherry", "blueberry"]
sorted_words = sorted(words)
print(sorted_words)# ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear']
```

The `sorted()` function takes the list as the first argument and returns a new list with the elements sorted in ascending order by default.

You can also specify the order using the `reverse` parameter:

```python
numbers = [5, -3, 2, -4, 6, -2, 4]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)# [6, 5, 4, 2, -2, -3, -4]
```

You can also pass a custom function to the `key` parameter to specify the sorting criteria.

```python
numbers = [5, -3, 2, -4, 6, -2, 4]
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers)# [2, -2, -3, 4, -4, 5, 6]
```

For the most part, it's similar to the `sort()` method, but it returns a new list instead of modifying the original list.

### Sorting based on values and order

Sort list using first element in increasing order if the first values are equal sort by second value by descending order.

```python
profits = [1,2,3]
capital = [0,1,1]
pairs = [(profits[i], capital[i]) for i in range(len(profits))] # (profit, capital)
pairs.sort(key=lambda p:(p[1], -p[0]))

print(pairs)
# [(1, 0), (3, 1), (2, 1)]
```

### **Time and Space Complexity**

The time complexity of the `.sort()` method is `𝑂(𝑛𝑙𝑜𝑔𝑛)`, where `n` is the number of elements in the list. The space complexity is `𝑂(𝑛)`, where `n` is the number of elements in the list.

***Note*:** Python uses the [Timsort](https://en.wikipedia.org/wiki/Timsort) algorithm for sorting lists. Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort.

### Merge Sort

```python
# Problem Link: https://leetcode.com/problems/sort-an-array/
# AC, LC: Badhansen

class Solution:
    def mergeSort(self, nums, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m + 1, r)
            self.merge(nums, l, m, r)
    def merge(self, nums, l, m, r):
        i = l
        j = m + 1
        res = []
        while i <= m and j <= r:
            if nums[i] <= nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
        while i <= m:
            res.append(nums[i])
            i += 1
        while j <= r:
            res.append(nums[j])
            j += 1
        index = 0
        for k in range(l, r + 1):
            nums[k] = res[index]
            index += 1
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
```

## 4️⃣ Stack
**Description**:
A stack is a collection of elements that follows the Last In, First Out (LIFO) principle. The `push` operation adds an element to the top of the stack, while the `pop` operation removes the top element.

**Example**:
```python
stack = []

# Push elements onto the stack
stack.append(1) # O(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: [1, 2, 3]

# Pop elements from the stack
top_element = stack.pop() # O(1)
# Check the element
value = stack[-1] # O(1)
print(value) # Output: 3
print(top_element)  # Output: 3
print(stack)        # Output: [1, 2]
```
## 5️⃣ Queue & Heap
### Queue
**Description**:
A queue is a collection of elements that follows the First In, First Out (FIFO) principle. The `enqueue` operation adds an element to the end of the queue, while the `dequeue` operation removes the element from the front of the queue.

**Example**:
```python
from collections import deque

queue = deque()

# Enqueue elements
queue.append(1) # O(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

# Dequeue elements
front_element = queue.popleft() # O(1)
print(front_element)  # Output: 1
print(queue)          # Output: deque([2, 3])
```

### Double Ended Queue (Deque)
**Description:**
A deque (double-ended queue) allows you to add or remove elements from both ends (front and back). This provides more flexibility than a regular queue or stack.

**Example**:
```python
from collections import deque

deque_obj = deque()

# Add elements to both ends
deque_obj.append(1)        # O(1), Add to the right
deque_obj.appendleft(2)    # O(1), Add to the left

print(deque_obj)  # Output: deque([2, 1])

# Remove elements from both ends
right_element = deque_obj.pop() # O(1)
left_element = deque_obj.popleft() # O(1)

print(right_element)  # Output: 1
print(left_element)   # Output: 2
print(deque_obj)      # Output: deque([])

# Create a deque
dq = deque([10, 20, 30, 40, 50])

# Access the first element
first_element = dq[0]  # O(1)
print("First element:", first_element)

# Access the last element
last_element = dq[-1]  # O(1)
print("Last element:", last_element)

# Insert at a specific position (e.g., index 2)
dq.insert(2, 25)  # O(n)
print("After insert:", dq)

# Access an element by index (not the ends)
middle_element = dq[2]  # O(n)
print("Element at index 2:", middle_element)

# Iterate through all elements
for elem in dq:  # O(n)
    print(elem, end=" ")
```
**Time Complexity**:

- `append` (add to the right): `O(1)`
- `appendleft` (add to the left): `O(1)`
- `pop` (remove from the right): `O(1)`
- `popleft` (remove from the left): `O(1)`

In python we can traverse stacks, queues, and deques in Python:

- **Stack Traversal**:
    - Stacks follow the Last In, First Out (LIFO) principle.
    - Traversing a stack involves iterating over the elements, typically implemented as a list.
    - Time Complexity: `O(n)`
- **Queue Traversal**:
    - Queues follow the First In, First Out (FIFO) principle.
    - Traversing a queue involves iterating over the elements, often implemented using `collections.deque`.
    - Time Complexity: `O(n)`
- **Deque Traversal**:
    - Deques (double-ended queues) allow elements to be added or removed from both ends.
    - Traversing a deque involves iterating over the elements, also implemented using `collections.deque`.
    - Time Complexity: `O(n)`

### Heaps or Priority Queues
**Description:**
A Priority Queue is a data structure where elements are dequeued based on priority. Python implements it using the `heapq` module, which provides a min-heap by default.

**Example**:
```python
import heapq  # Min-Heap by default

# Initialize an empty list to act as a heap
heap = []

# Push elements onto the heap
heapq.heappush(heap, 10)  # O(log n)
heapq.heappush(heap, 5)   # O(log n)
heapq.heappush(heap, 15)  # O(log n)
heapq.heappush(heap, 3)   # O(log n)

print("Heap after pushing elements:", heap)  
# Output: Heap after pushing elements: [3, 5, 15, 10]

# Pop the smallest element from the heap
smallest = heapq.heappop(heap)  # O(log n)
print("Smallest element:", smallest)  
# Output: Smallest element: 3

print("Heap after popping the smallest element:", heap)  
# Output: Heap after popping the smallest element: [5, 10, 15]

# Convert a list into a heap
nums = [5, 7, 9, 1, 3]
heapq.heapify(nums)  # O(n)
print("Heapified list:", nums)  
# Output: Heapified list: [1, 3, 9, 7, 5]

# Push an element into the heap
heapq.heappush(nums, 4)  # O(log n)
print("Heap after pushing 4:", nums)  
# Output: Heap after pushing 4: [1, 3, 4, 7, 5, 9]

# Pop the smallest element from the heap
value = heapq.heappop(nums)  # O(log n)
print("Popped smallest element:", value)  
# Output: Popped smallest element: 1

print("Heap after popping the smallest element:", nums)  
# Output: Heap after popping the smallest element: [3, 5, 4, 7, 9]
```
### Custom Heaps
**Description:**
Suppose I have a pairs of integers which represent (cost, profit) of an item.
By default it is min heap so it will heapify based on first value then second value then third value.

**Example**:
```python
import heapq

# Initialize the list of tuples
elements = [(3, 300), (3, 140), (3, 140), (3, 10), (5, 55), (5, 50), (10, 200), (10, 100)]

# Convert the list to a heap
heapq.heapify(elements)

print("Heapified list:")
while elements:
    val = heapq.heappop(elements)
    print(val)
    
'''
Heapified list:
(3, 10)
(3, 140)
(3, 140)
(3, 300)
(5, 50)
(5, 55)
(10, 100)
(10, 200)
'''
```
> **Now I want to create a heap: Low cost with high profit.**

**Example**:
```python
import heapq

elements = [(3, 300), (3, 140), (3, 140), (3, 10), (5, 55), (5, 50), (10, 200), (10, 100)]
heap = []
for cost, profit in elements:
	heapq.heappush(heap, (cost, -profit))
	
print("Heapified list:")
while heap:
    cost, profit = heapq.heappop(heap)
    print(cost, -profit)
    
'''
Heapified list:
3 300
3 140
3 140
3 10
5 55
5 50
10 200
10 100
'''
```

> **Now I want to create a heap: High cost with high profit.**

**Example**
```python
import heapq

elements = [(3, 300), (3, 140), (3, 140), (3, 10), (5, 55), (5, 50), (10, 200), (10, 100)]
heap = []
for cost, profit in elements:
	heapq.heappush(heap, (-cost, -profit))
	
print("Heapified list:")
while heap:
    cost, profit = heapq.heappop(heap)
    print(-cost, -profit)
    
'''
Heapified list:
10 200
10 100
5 55
5 50
3 300
3 140
3 140
3 10
'''
```
## 6️⃣ Linked Lists 
### Singly Linked List
**Description:**
A linked list is a linear collection of elements, where each element points to the next element in the sequence. Each element, often called a "node," contains two key pieces of information:

* The data value
* A reference (or link) to the next node in the sequence

**Example**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """Add element to the end of the list with O(1) time complexity"""
        new_node = Node(data)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Add to the end
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
    
    def appendleft(self, data):
        """Add element to the beginning of the list with O(1) time complexity"""
        new_node = Node(data)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # Add to the beginning
            new_node.next = self.head
            self.head = new_node
            
        self.size += 1
    
    def display(self):
        """Display all elements in the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def get_size(self):
        """Return the number of elements in the list"""
        return self.size
```
### Doubly Linked List
**Description**
A doubly linked list is a type of linked data structure in which each node contains three components:

* Data: The actual value or information being stored
* Next pointer: A reference to the next node in the sequence
* Previous pointer: A reference to the previous node in the sequence

**Example**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # Add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            new_node.prev = self.tail  # Link the new node back to the current tail
            self.tail = new_node  # Update the tail reference
        self.size += 1
    
    # Add a node at the beginning of the list
    def appendleft(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head.prev = new_node  # Link the current head back to the new node
            self.head = new_node  # Update the head reference
        self.size += 1
    
    # Delete the first node (from the head)
    def delete_from_head(self):
        if self.head is None:  # If the list is empty
            return None
        
        current_data = self.head.data  # Store the value of the head
        
        # If only one node exists
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Move the head pointer forward
            self.head.prev = None  # Remove reference to the deleted node
        
        self.size -= 1
        return current_data
    
    # Delete the last node (from the tail)
    def delete_from_tail(self):
        if self.tail is None:  # If the list is empty
            return None
        
        current_data = self.tail.data  # Store the value of the tail
        
        # If only one node exists
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # Move the tail pointer backward
            self.tail.next = None  # Remove reference to the deleted node
        
        self.size -= 1
        return current_data
    
    # Get the current size of the list
    def get_size(self):
        return self.size
    
    # Check if the list is empty
    def is_empty(self):
        return self.head is None
    
    # Display the list in forward order
    def display(self):
        if self.is_empty():
            print("Empty list")
            return
            
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")
```