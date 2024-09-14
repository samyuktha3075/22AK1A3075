import numpy as np

# Function to interchange the first and last columns of a matrix
def interchange_columns(matrix):
    num_rows, num_cols = matrix.shape
    
    # Check if the matrix has at least two columns
    if num_cols < 2:
        print("The matrix must have at least two columns to interchange.")
        return matrix
    
    # Interchange the first and last columns
    matrix[:, [0, -1]] = matrix[:, [-1, 0]]
    return matrix

# Input matrix (example)
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:")
print(matrix)

# Interchange columns
result_matrix = interchange_columns(matrix)

print("\nMatrix after interchanging first and last columns:")
print(result_matrix)