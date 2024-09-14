# Function to perform relational operations on two integers
def relational_operations(num1, num2):
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    
    # Equal to
    print(f"{num1} == {num2}: {num1 == num2}")
    
    # Not equal to
    print(f"{num1} != {num2}: {num1 != num2}")
    
    # Greater than
    print(f"{num1} > {num2}: {num1 > num2}")
    
    # Less than
    print(f"{num1} < {num2}: {num1 < num2}")
    
    # Greater than or equal to
    print(f"{num1} >= {num2}: {num1 >= num2}")
    
    # Less than or equal to
    print(f"{num1} <= {num2}: {num1 <= num2}")

# Input two 10-digit integers from the user
num1 = int(input("Enter the first 10-digit integer: "))
num2 = int(input("Enter the second 10-digit integer: "))

# Ensure the numbers are 10 digits long
if len(str(num1)) == 10 and len(str(num2)) == 10:
    relational_operations(num1, num2)
else:
    print("Please enter valid 10-digit integers.")