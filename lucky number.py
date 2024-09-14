import random

def generate_lucky_number():
    # Generate a random integer between 1 and 9 (inclusive)
    return random.randint(1, 9)

def main():
    # Generate and print the lucky number
    lucky_number = generate_lucky_number()
    print(f"Your lucky number is: {lucky_number}")

if _name_ == "_main_":
    main()