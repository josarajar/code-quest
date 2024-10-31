def can_partition(nums):
    """
    Determine if a multiset can be partitioned into two subsets with equal sum.
    
    Args:
    nums (list of int): A multiset of integers
    
    Returns:
    bool: True if the multiset can be partitioned into two equal sum subsets, False otherwise
    """
    # Calculate the total sum of the multiset
    total_sum = sum(nums)
    
    # If total sum is odd, it can't be split into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # Target sum for each subset
    target = total_sum // 2
    
    # Dynamic programming approach 
    # dp[i] will be True if sum i can be achieved using a subset of nums
    dp = [False] * (target + 1)
    dp[0] = True  # Zero sum is always possible with an empty subset
    print(target, dp)
    # Iterate through each number in the multiset
    for num in nums:
        # We iterate backwards to avoid using same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    
    # If dp[target] is True, we can form a subset with sum equal to target
    print(dp)
    return dp[target]


    
if __name__ == '__main__':
    # Test cases
    test_cases = [
        [15, 5, 20, 10, 35, 15, 10],  # True case
        [15, 5, 20, 10, 35],          # False case
        [1, 2, 3, 4],                 # True case
        [1, 2, 5],                    # False case
    ]

    results = [True, False, True, False]
    # Run test cases
    for case, result in zip(test_cases, results):
       assert can_partition(case) == result, f'{case} {' can' if result else ' cannot'} split it up'

    print("All test cases passed!")

