# Function to reverse a given string
def reverse_string(s):
    return s[::-1]

# Main function to read input and reverse the string
def main():
    string_input = input("Enter a string: ")
    reversed_string = reverse_string(string_input)
    print(f"Reversed string: {reversed_string}")

# Run the main function
main()