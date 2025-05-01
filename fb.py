#fizzbuzz 


# FizzBuzz checker that keeps running until you type “q”
while True:                                          # 1
    user_input = input("Enter a number (or q to quit): ")  # 2

    if user_input.upper() == "q":                    # 3
        print("Good-bye!")                           # 4
        break                                        # 5

    if not user_input.isdigit():                     # 6
        print("→ Please enter a positive whole number.")   # 7
        continue                                     # 8

    num = int(user_input)                            # 9

    if num % 3 == 0 and num % 5 == 0:                # 10
        print("FizzBuzz")                            # 11
    elif num % 3 == 0:                               # 12
        print("Fizz")                                # 13
    elif num % 5 == 0:                               # 14
        print("Buzz")                                # 15
    else:                                            # 16
        print(num)                                   # 17
