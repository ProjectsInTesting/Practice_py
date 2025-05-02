# Lists => collection of elements 
# Mutable: You can change, add, or remove elements after creation.
# Ordered: Items maintain their defined order (unless explicitly changed).
# Indexable: Elements can be accessed via their position (index).
# Heterogeneous: Can contain different data types (e.g., integers, strings, other lists).
# print(my_list[-1]) # [-1] get the last index int he list




# Access list
"""
fruit = ["banana", "apple", "botato", "20"]
print(fruit[:2])    # ['banana', 'apple']
print(fruit[-1])    # 20
print(fruit[:])     # ['banana', 'apple', 'botato', '20']
print(fruit[:1])    # ['banana']
print(fruit[1:3])   # ['apple', 'botato']
print(fruit[1:])    # ['apple', 'botato', '20']
print(fruit[0:])    # ['banana', 'apple', 'botato', '20']
print(fruit[::-1])  # ['20', 'botato', 'apple', 'banana']
"""


#########

# Update (change) item in a list:
"""
my_list1 = [1, 2, 3, 4]
my_list1[1] = 100
print(my_list1)
"""


########

# reverse a list
     #1 using slicing
"""
my_fruit = ["apple", "banana", "orange", "watermealon"]
print("reverse using list slicing: ")
print(my_fruit[::-1])
"""
     #2 using reverse() methode
"""
print("reverse a list using reverse() methode: ")
my_fruit.reverse()
print(my_fruit)
"""

     # using For loop
"""print("revers a list using For loop: ") => The print(reversed_list) inside the 
loop shows the list after each insertion
"""
"""
my_fruit = ["banana", "Apple", "orange"]
reversed_list = []
for item in my_fruit:
    reversed_list.insert(0, item)
    print(reversed_list)
"""

# remove item from a list
"""
my_list = [1, 2, 3, 4]
my_list.remove(1) # using remove > remove item by value
print(my_list)

del my_list[2]  # use del > delete by index
print(my_list)
"""

# remove duplicate from list






