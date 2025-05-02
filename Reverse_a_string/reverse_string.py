# Here different ways to reverse a list a string or integers.

#reverse a list:

my_list = ["apple", "banana", "date", 2] 
#reverse using list slicing:
print(my_list[::-1])
#reverse using reverse() methode.
my_list.reverse()
print(my_list)

my_numbers = [1, 2, 3, 4]
print(my_numbers)
print("reverse using list slicing: ")
print(my_numbers[::-1])
print("reverse using reverse() methode: ")
my_numbers.reverse()
print(my_numbers)

#reverse using foor loop
print("reverse list using For loop: ")
my_numbers1 = [10, 20, 30, 40]
reversed_list =[]
for number in my_numbers1:
    reversed_list.insert(0, number)
print(reversed_list)

"""
How It Works
Initialization:
my_list contains [1, 2, 3, 4, 5]
reversed_list starts as an empty list []
Loop Through Original List:
The for loop goes through each item in my_list in order (1, then 2, then 3, etc.)
Inserting Items at Position 0:
insert(0, item) places each new item at the beginning (index 0) of reversed_list
This pushes previous items to the right
Step-by-Step Building of reversed_list:
1st iteration: reversed_list becomes [1]
2nd iteration: [2, 1] (2 is inserted at position 0)
3rd iteration: [3, 2, 1]
4th iteration: [4, 3, 2, 1]
5th iteration: [5, 4, 3, 2, 1]
Key Concept
By always inserting new items at the front of reversed_list, we effectively build the list in reverse order compared to the original.
"""
