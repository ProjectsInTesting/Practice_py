#reverse a number 1,2,3,4
# will use a list

#1 using list slicing

my_numbers = [1, 2, 3, 4]
print(my_numbers[::-1])

#2 usnig reverse methide()

my_num = [1, 2, 3, 4]
my_num.reverse()
print(my_num)

# reverse using for loop

my_n = [1, 2, 3]
rev_n = []
for number in my_n :
    rev_n.insert(0, number)
    print(rev_n)



