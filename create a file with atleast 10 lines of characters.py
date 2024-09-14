# Function to create a file with at least 10 lines
def create_file():
    with open("sample_file.txt", "w") as file:
        content = """Line 1: Hello, World!
Line 2: This is a Python script.
Line 3: Reading and writing files.
Line 4: Let's reverse some characters.
Line 5: Python is fun.
Line 6: File operations are easy.
Line 7: Learning programming.
Line 8: Handling text data.
Line 9: Complex operations made simple.
Line 10: Keep practicing to master."""
        file.write(content)

# Function to read the first 'n' characters from the file and display in reverse
def read_reverse_characters(n):
    with open("sample_file.txt", "r") as file:
        content = file.read()  # Read the entire file content
        first_n_chars = content[:n]  # Extract the first 'n' characters
        reversed_chars = first_n_chars[::-1]  # Reverse the characters
        print(f"First {n} characters in reverse:\n{reversed_chars}")

# Create the file
create_file()

# Read and reverse the first 'n' characters
n = 50  # Example: Read the first 50 characters
read_reverse_characters(n)