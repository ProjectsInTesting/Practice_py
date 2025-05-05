# Program to count vowels and consonants in a string

# Take user input
input_string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through each character in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the results
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")