#fizzbuzz 


# FizzBuzz checker that keeps running until you type “q”
while True:                                          # 1
    user_input = input("Enter a number (or q to quit): ")  # 2

    if user_input.lower() == "q":                    # 3
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







"""
Line 1: while True:
Starts an infinite loop . This ensures the program keeps running until the user explicitly quits (via break later). The loop will repeat indefinitely unless interrupted.
************************************************************
Line 2: user_input = input("Enter a number (or q to quit): ")
Prompts the user to enter a number or type "q" to exit. The input is stored as a string in user_input.
************************************************************
Line 3: if user_input.lower() == "q":
Checks if the user typed "q" (case-insensitive).

user_input.lower() converts the input to lowercase (e.g., "Q" or "q" → "Q").
If true, the program proceeds to exit.
************************************************************
Line 4: print("Good-bye!")
Prints a farewell message when the user quits.
***********************************************************
Line 5: break
Exits the infinite loop (while True), terminating the program.
************************************************************
Line 6: if not user_input.isdigit():
Checks if the input is not a valid digit (e.g., letters, symbols, decimals).

isdigit() returns True only for positive integers (e.g., "123" → True, "-5" or "0.5" → False).
This ensures only numeric input is processed further.
************************************************************
Line 7: print("→ Please enter a positive whole number.")
Informs the user to provide a valid positive integer if the input is invalid.
************************************************************
Line 8: continue
Skips the rest of the loop and restarts the cycle (prompting the user again). This avoids processing invalid inputs.
************************************************************
Line 9: num = int(user_input)
Converts the valid string input (e.g., "15") to an integer (e.g., 15). This allows mathematical operations.
************************************************************
Line 10: if num % 3 == 0 and num % 5 == 0:
Checks if the number is divisible by both 3 and 5 (i.e., divisible by 15).

% is the modulo operator, which returns the remainder of division.
This condition must come first to avoid being overridden by the individual checks for 3 or 5.
************************************************************
Line 11: print("FizzBuzz")
Prints "FizzBuzz" if the number is divisible by both 3 and 5.
************************************************************
Line 12: elif num % 3 == 0:
Checks if the number is divisible by 3 only .

elif means "else if" — this runs only if the previous condition is false.
************************************************************
Line 13: print("Fizz")
Prints "Fizz" if the number is divisible by 3 but not 5.
************************************************************
Line 14: elif num % 5 == 0:
Checks if the number is divisible by 5 only .
************************************************************
Line 15: print("Buzz")
Prints "Buzz" if the number is divisible by 5 but not 3.
************************************************************
Line 16: else:
Handles all remaining cases where the number is not divisible by 3 or 5 .
************************************************************
Line 17: print(num)
Prints the original number if it doesn’t meet any of the divisibility conditions.

Key Notes:
Input Validation : Ensures only positive integers are processed. Negative numbers, decimals, or non-numeric inputs trigger a warning.
Order of Checks : The FizzBuzz logic follows the correct priority:
Divisible by 15 (both 3 and 5).
Divisible by 3.
Divisible by 5.
Default to printing the number.
Edge Cases :
0 is treated as a valid input ("0".isdigit() is True), but it’s not a positive number. This could be a bug based on the prompt’s wording.
Negative numbers or decimals are rejected because isdigit() returns False for them.
"""
