# Define a function to perform operations on complex numbers
def complex_operations(num1, num2):
    # Addition
    addition = num1 + num2
    
    # Subtraction
    subtraction = num1 - num2
    
    # Multiplication
    multiplication = num1 * num2
    
    # Conjugate of the first complex number
    conjugate_num1 = num1.conjugate()
    
    # Conjugate of the second complex number
    conjugate_num2 = num2.conjugate()
    
    # Display the results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Conjugate of {num1}: {conjugate_num1}")
    print(f"Conjugate of {num2}: {conjugate_num2}")

# Example usage
num1 = complex(3, 4)  # 3 + 4j
num2 = complex(1, 2)  # 1 + 2j

complex_operations(num1, num2)