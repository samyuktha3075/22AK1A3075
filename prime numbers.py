def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """Print all prime numbers in a specified range."""
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Example usage:
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print_primes_in_range(start, end)
