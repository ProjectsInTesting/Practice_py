# Check if a string is a palindrome

# Take user input
# Remove spaces and convert to lowercase for uniformity
# Check if the string is equal to its reverse

input_string = input("Enter a string to check if it's a palindrome: ")
normalized_string = input_string.replace(" ", "").lower()
if normalized_string == normalized_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

    #test 1
    #test 2
    #test 3
    
