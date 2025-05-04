
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

# for loop and while loop

while True:                                          
    user_input = input("Enter a number (or q to quit): ") 

    if user_input.lower() == "q":                    
        print("Good-bye!")                           
        break                                        

    if not user_input.isdigit():                     
        print("→ Please enter a positive whole number.")   
        continue                                     

    num = int(user_input)                            

    if num % 3 == 0 and num % 5 == 0:                
        print("FizzBuzz")                            
    elif num % 3 == 0:                               
        print("Fizz")                                
    elif num % 5 == 0:                               
        print("Buzz")                                
    else:                                            
        print(num)      