import sys
# Function to find the two elements whose sum is closest to zero
def closest_to_zero(arr):
    # Sort the array first
    arr.sort()
    
    # Initialize variables to store the result
    left = 0
    right = len(arr) - 1
    closest_sum = sys.maxsize
    result_pair = (0, 0)
    
    # Use two pointers to find the closest sum to zero
    while left < right:
        current_sum = arr[left] + arr[right]
        
        # If the absolute value of the current sum is smaller than the closest sum
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result_pair = (arr[left], arr[right])
        
        # Move the left or right pointer
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    
    # Return the result
    return result_pair

# Input array
arr = [1, 60, -10, 70, -80, 85]

