#fizzbuzz using For loop

# 1 create a for loop that loops through 1 through 100.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: Fizzbuzz")
    elif number % 3 == 0:
        print(f"{number}: fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(number)

        

        # we can add the number next to the fizzbuzz word by using the f string.

#        for number in range(1, 101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("Fizzbuzz")
#    elif number % 3 == 0:
#        print("fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)


