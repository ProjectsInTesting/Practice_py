"""
for number in range(1,101):
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)


while True:
    input_number = input("please enter a number between 1 and 100, or 'q' for quit: ")
    if input_number.lower() == 'q':
        print("good buy")
        break
    if not input_number.isdigit():
        print("please enter a valid digit between 1 and 100")
        continue

    number = int(input_number) 
    
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
"""
#update scrap paper

