# List is a collection of ellement. 
# lists are:
#           - Mutable: i can change, add or remove elements.
#           - ordered: items maintain their defined ordered
#           - Indexable: means elements can be accessed via their position (index)
#           - Heterogeneouse: can contain different data types e.g: itegers, strings, other lists.
#            my_list = [1, 2, 3, "Hello", 5.5]


What is a list in python

In Python, a list is a built-in data structure used to store an ordered collection of items. Lists are:

Mutable: You can change, add, or remove elements after creation.

Ordered: Items maintain their defined order (unless explicitly changed).

Indexable: Elements can be accessed via their position (index).

Heterogeneous: Can contain different data types (e.g., integers, strings, other lists).

Basic Syntax
python
my_list = [1, 2, 3, "hello", 5.5]
Key Features
Creation:

python
empty_list = []
numbers = [1, 2, 3]
mixed = [10, "apple", True, [1, 2]]
Accessing Elements (0-based indexing):

python
print(numbers[0])  # Output: 1
print(mixed[-1])    # Output: [1, 2] (negative index starts from the end)
Slicing (Extract sub-lists):

python
print(numbers[1:3])  # Output: [2, 3] (excludes index 3)
Modifying Lists:

python
numbers[0] = 99      # Change an element
numbers.append(4)    # Add to end
numbers.insert(1, 5) # Insert at index 1
numbers.remove(2)    # Remove first occurrence of 2
Common Methods:

append(x): Add x to the end.

extend(iterable): Add multiple items.

pop([i]): Remove and return item at index i (default last).

sort(): Sort the list in place.

reverse(): Reverse the list in place.

len(list): Get the length.

List Comprehensions (Concise creation):

python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
Example
python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1])       # Output: "banana"
print(len(fruits))     # Output: 4
Use Cases
Storing and manipulating ordered data.

Iterating over collections (e.g., for item in list).

As stacks (append(), pop()) or queues (with collections.deque).

Lists are one of Python’s most versatile and widely used data structures! 🚀

*****************************************************************************

Python Lists: A Comprehensive Guide with Examples
Lists in Python are ordered, mutable collections that can hold a variety of object types. They are one of Python's most versatile and commonly used data structures.

Creating Lists
python
# Empty list
empty_list = []
empty_list = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']
mixed = [1, 'hello', 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
Basic List Operations
Accessing Elements
python
fruits = ['apple', 'banana', 'cherry', 'date']

# Indexing (0-based)
print(fruits[0])    # 'apple'
print(fruits[2])    # 'cherry'
print(fruits[-1])   # 'date' (last element)

# Slicing
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[2:])   # ['cherry', 'date']
print(fruits[::-1]) # ['date', 'cherry', 'banana', 'apple'] (reverse)
Modifying Lists
python
# Changing elements
fruits[1] = 'blueberry'
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# Adding elements
fruits.append('elderberry')  # Add to end
fruits.insert(1, 'apricot')  # Insert at specific position
print(fruits)  # ['apple', 'apricot', 'blueberry', 'cherry', 'date', 'elderberry']

# Combining lists
more_fruits = ['fig', 'grape']
fruits.extend(more_fruits)  # Or fruits += more_fruits
print(fruits)  # ['apple', 'apricot', 'blueberry', 'cherry', 'date', 'elderberry', 'fig', 'grape']
Removing Elements
python
# Remove by value
fruits.remove('blueberry')

# Remove by index
popped = fruits.pop(2)  # Removes and returns 'cherry'
popped_last = fruits.pop()  # Removes and returns last element ('grape')

# Clear the list
fruits.clear()  # fruits is now []
List Methods
python
nums = [5, 2, 8, 1, 9, 3]

# Sorting
nums.sort()  # [1, 2, 3, 5, 8, 9]
nums.sort(reverse=True)  # [9, 8, 5, 3, 2, 1]
sorted_nums = sorted(nums)  # Returns new sorted list

# Reversing
nums.reverse()  # Reverses in place

# Searching
print(nums.index(5))  # Returns index of first occurrence
print(8 in nums)      # True if 8 is in the list

# Counting
print(nums.count(5))  # Count occurrences of 5

# Length
print(len(nums))      # Number of elements
List Comprehensions
A concise way to create lists:

python
# Squares of numbers
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
Copying Lists
python
original = [1, 2, 3]

# Shallow copy (different object, same references)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Deep copy (for nested lists)
import copy
deep_copy = copy.deepcopy(original)
Advanced Operations
python
# Zip lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
zipped = list(zip(names, scores))  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2, 3, 4, 5]

# Enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
    # 0 a
    # 1 b
    # 2 c

# Map and filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))  # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x%2 == 0, nums))  # [2, 4]
Lists are incredibly versatile and form the backbone of many Python programs. They can be used as stacks (LIFO) with append() and pop(), or as queues (FIFO) with append() and pop(0) (though collections.deque is more efficient for queues).

