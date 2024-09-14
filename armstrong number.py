def is_armstrong_number(number):
    # Convert the number to a string to easily iterate through digits
    num_str = str(number)
    # Find the number of digits
    num_digits = len(num_str)
    
    # Compute the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

def main():
    # Read input from user
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            if is_armstrong_number(number):
                print(f"{number} is an Armstrong number.")
            else:
                print(f"{number} is not an Armstrong number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if _name_ == "_main_":
    main()