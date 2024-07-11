
def count_numbers_with_digit_sum_constraint(max_digits, max_sum):
    """
    Count how many max_digits numbers exist such that no three consecutive digits have a sum greater than max_sum.
    
    Args:
    - max_digits: The maximum number of digits in the number.
    - max_sum: The maximum allowed sum of any three consecutive digits.
    
    Returns:
    - The count of numbers satisfying the above constraints.
    """
    # Use dynamic programming to store the count of valid numbers ending with two specific digits
    dp = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(max_digits + 1)]
    
    # Initialization: For a single digit, all digits from 1 to 9 are valid (0 is not allowed as it leads to leading zeros)
    for i in range(1, 10):
        dp[1][0][i] = 1
    
    # Fill the DP table
    for digit in range(2, max_digits + 1):
        for d1 in range(10):
            for d2 in range(10):
                for d3 in range(10):
                    if d1 + d2 + d3 <= max_sum:
                        dp[digit][d2][d3] += dp[digit - 1][d1][d2]
    
    # Sum all valid numbers of max_digits
    count = 0
    for d1 in range(10):
        for d2 in range(10):
            count += dp[max_digits][d1][d2]
    
    return count

# Example usage
print(count_numbers_with_digit_sum_constraint(20, 9))  # For 3-digit numbers with no three consecutive digits summing more than 6