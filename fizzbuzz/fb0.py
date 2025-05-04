#fizzbuzz using while loop with user entry

#user enter a number
# if number divisible by 3 print "fizz"
# if number divisible by 5 print "buzz"
# if number divisible by 3 and 5 print Fizzbuzz
# otherwise print the number

while True:

    number = int (input("Please enter a number: "))
    if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")  #
    elif number % 3 == 0:
            print("Fizz")
    elif number % 5 == 0:
            print("Buzz")
    else:
            print(number)



""" explaining the code:
# create a variable called number which will be an integer and will ask a user to enter and integer number
# so we will need to use if statement 
# if number moduler (divisable) by 3 = 0 then print fizz
# if number moduler (divisible) by 5 == 0 then print buzz
# if number moduler (divisible) by 3 = 0 and number (divisible) by 5 = 0 then print fizzbuzz
# otherwise print the number.
"""

