# Function to print all even-length substrings
def print_even_length_substrings(s):
    length = len(s)
    # Iterate over all possible substrings
    for start in range(length):
        for end in range(start + 2, length + 1, 2):  # Ensure even length substrings
            substring = s[start:end]
            print(substring)

# Input string from the user
input_string = input("Enter a string: ")

# Print even-length substrings
print("Even-length substrings:")
print_even_length_substrings(input_string)