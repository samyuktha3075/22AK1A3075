# Function to count occurrences of each character in a string
def count_characters(input_string):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1  # If the character is already in the dictionary, increment the count
        else:
            char_count[char] = 1  # If it's a new character, add it to the dictionary with count 1
    
    # Display the count of each character
    for char, count in char_count.items():
        print(f"'{char}': {count}")

# Input string from user
input_string = input("Enter a string: ")

# Call the function to count characters
count_characters(input_string)