def count_elements_brute_force(matrix, i1, j1, i2, j2):
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
    
    Time Complexity: O(m*n)
    Space Complexity: O(1)
    """
    n, m = len(matrix), len(matrix[0])
    
    # Find the lower and upper bounds of the range
    lower, upper = matrix[i1][j1], matrix[i2][j2]
    result = 0
    nops = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] < lower or matrix[i][j] > upper:
                result+=1
            nops+=1
    print(f'Full computation number of ops: {nops}. Result: {result}')

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
    
    Time Complexity: O(result)
    Space Complexity: O(1)
    """
    n, m = len(matrix), len(matrix[0])
    
    # Find the lower and upper bounds of the range
    lower, upper = matrix[i1][j1], matrix[i2][j2]

    result=0
    nops = 0

    # Count rows smaller than i1
    for i in range(i1):
        for j in range(m):
            nops+=1
            if matrix[i][j] >= lower:
                result+=j
                break
            elif j==m:
                result+=m

    # Count columns smaller than j1
    for j in range(j1):
        for i in range(i1+1, n):
            nops+=1
            if matrix[i][j] >= lower:
                result+=i-i1
                break
            elif i==n-1:
                result+=n-i1

    # Count rows greater than i2
    for i in range(i2+1, n):
        for j in reversed(range(m)):
            nops+=1
            if matrix[i][j] <= upper:
                result+=(m-j-1)
                break
            elif j==0:
                result+=m

    # Count columns greater than j2
    for j in range(j2+1, len(matrix[0])):
        for i in reversed(range(i2)):
            nops+=1
            if matrix[i][j] <= upper:
                result+=(i2-i)
                break
            elif i==0:
                result+=i2+1

    print(f'Reduced computation number of ops: {nops}. Result: {result}')
    return result

# Example usage
matrix = [[1, 3, 7, 10, 15, 20], 
          [2, 6, 9, 14, 22, 25],
          [3, 8, 10, 15, 25, 30],
          [10, 11, 12, 23, 30, 35],
          [20, 25, 30, 35, 40, 45]]

print(count_range_elements(matrix, 1, 1, 3, 3))  # Output: 14