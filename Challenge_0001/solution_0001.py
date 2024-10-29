def count_paths(n: int, m: int) -> int:
    """
    Count the number of paths from top-left to bottom-right corner in an N x M grid.
    Can only move right or down.
    
    Args:
        n (int): Number of rows
        m (int): Number of columns
    
    Returns:
        int: Number of possible paths
    
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    # Create a grid to store the number of paths to each cell
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # There is only one way to reach any cell in first row (moving right)
    for j in range(m):
        dp[0][j] = 1
        
    # There is only one way to reach any cell in first column (moving down)
    for i in range(n):
        dp[i][0] = 1
        
    # For all other cells, paths = paths from above + paths from left
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[n-1][m-1]

def count_paths_recursive(n: int, m: int) -> int:
    """
    Count the number of paths from top-left to bottom-right corner in an N x M grid.
    Can only move right or down.
    
    Args:
        n (int): Number of rows
        m (int): Number of columns
    
    Returns:
        int: Number of possible paths
    
    Time Complexity: To Compute
    Space Complexity: To Compute
    """
    nrows, ncols = (n, m) if n<m else (m,n)
    npaths = 0
    if nrows==1:
        npaths = 1
    else:
        for i in range(nrows):
            npaths += count_paths_recursive(nrows-1, i)
    return npaths

# Test cases
def test_count_paths():
    assert count_paths(2, 2) == 2, "2x2 grid should have 2 paths"
    assert count_paths(5, 5) == 70, "5x5 grid should have 70 paths"
    assert count_paths(1, 1) == 1, "1x1 grid should have 1 path"
    assert count_paths(3, 2) == 3, "3x2 grid should have 3 paths"
    assert count_paths(2, 3) == 3, "2x3 grid should have 3 paths"
    print("All test cases passed!")

test_count_paths()