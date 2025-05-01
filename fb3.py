"""
fizzbuzz using for loop
will use for loop that loop from 1 through 100
1- if number divisible by 3 then print fizz
2- if the number ivisible by 5 then print buzz
3- if the number divisible by 3 and 5 then print fizzbuzz
"""
for number in range (1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: fizzbuzz")
    elif number % 3 == 0:
        print(f"{number}: fizz")
    elif number % 5 == 0:
        print(f"{number}: buzz")
    else:
        print(number)



