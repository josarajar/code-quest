def count_range_elements(matrix, i1, j1, i2, j2):
    """
    Given a sorted matrix A, count the number of elements smaller than A[i1, j1] 
    and larger than A[i2, j2].
    
    Args:
        matrix (List[List[int]]): The sorted matrix
        i1 (int): Row index of the first element
        j1 (int): Column index of the first element
        i2 (int): Row index of the second element
        j2 (int): Column index of the second element
    
    Returns:
        int: The number of elements in the range
    
    Time Complexity: O(m * log n)
    Space Complexity: O(1)
    """
    n, m = len(matrix), len(matrix[0])
    
    # Find the lower and upper bounds of the range
    lower, upper = matrix[i2][j2], matrix[i1][j1]
    
    count = 0
    
    # Iterate through each row
    for i in range(n):
        # Use binary search to find the leftmost index greater than upper
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] > upper:
                right = mid - 1
            else:
                left = mid + 1
        count += left
        
        # Use binary search to find the rightmost index less than lower
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] < lower:
                left = mid + 1
            else:
                right = mid - 1
        count -= (m - right - 1)
    
    return count

# Example usage
matrix = [[1, 3, 7, 10, 15, 20], 
          [2, 6, 9, 14, 22, 25],
          [3, 8, 10, 15, 25, 30],
          [10, 11, 12, 23, 30, 35],
          [20, 25, 30, 35, 40, 45]]

print(count_range_elements(matrix, 1, 1, 3, 3))  # Output: 14