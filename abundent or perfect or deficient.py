# Function to calculate the sum of proper divisors of a number
def sum_of_divisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

# Function to check whether the number is perfect, abundant, or deficient
def check_number_type(num):
    divisors_sum = sum_of_divisors(num)
    
    if divisors_sum == num:
        return "Perfect"
    elif divisors_sum > num:
        return "Abundant"
    else:
        return "Deficient"

# Main function to take input and display the result
def main():
    number = int(input("Enter a number: "))
    result = check_number_type(number)
    print(f"The number {number} is {result}.")

# Run the main function
main()