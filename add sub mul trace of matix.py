# Function to add two matrices
def matrix_addition(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

# Function to subtract two matrices
def matrix_subtraction(matrix1, matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

# Function to multiply two matrices
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Iterating through rows of matrix1
    for i in range(len(matrix1)):
        # Iterating through columns of matrix2
        for j in range(len(matrix2[0])):
            # Iterating through rows of matrix2
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Function to calculate the trace of a matrix
def matrix_trace(matrix):
    trace_sum = 0
    for i in range(len(matrix)):
        trace_sum += matrix[i][i]
    return trace_sum

# Helper function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Main function to perform operations
def main():
    # Example matrices
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    print("Matrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)
    
    # Addition
    addition_result = matrix_addition(matrix1, matrix2)
    print("\nAddition of Matrix 1 and Matrix 2:")
    print_matrix(addition_result)
    
    # Subtraction
    subtraction_result = matrix_subtraction(matrix1, matrix2)
    print("\nSubtraction of Matrix 1 and Matrix 2:")
    print_matrix(subtraction_result)
    
    # Multiplication
    multiplication_result = matrix_multiplication(matrix1, matrix2)
    print("\nMultiplication of Matrix 1 and Matrix 2:")
    print_matrix(multiplication_result)
    
    # Trace of Matrix 1
    trace_result = matrix_trace(matrix1)
    print(f"\nTrace of Matrix 1: {trace_result}")

# Run the main function
main()
