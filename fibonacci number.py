import math

# Function to check if a number is a perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

# Function to check if a number is a Fibonacci number
def is_fibonacci_number(n):
    # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Function to find the position of a Fibonacci number
def fibonacci_position(n):
    if n == 0:
        return 1  # position of 0 in Fibonacci sequence
    a, b = 0, 1
    position = 2  # Starting from position 2 as position 1 is for 0
    while b < n:
        a, b = b, a + b
        position += 1
    return position

# Main program
try:
    num = int(input("Enter an integer: "))
    
    if is_fibonacci_number(num):
        position = fibonacci_position(num)
        print(f"{num} is a Fibonacci number, and it is at position {position}.")
    else:
        print(f"{num} is not a Fibonacci number.")
except ValueError:
    print("Invalid input. Please enter an integer.")