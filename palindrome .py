# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Function to find the next palindrome
def next_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

# Main function to take input and check the conditions
def check_prime_and_palindrome():
    number = int(input("Enter an integer: "))
    
    if is_prime(number):
        next_pal = next_palindrome(number)
        print(f"The number is prime. The next palindrome is {next_pal}.")
    else:
        print("Not Prime.")

# Run the main function
check_prime_and_palindrome()