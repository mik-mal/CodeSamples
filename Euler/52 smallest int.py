def find_smallest_integer_with_same_digits():
    """Find the smallest positive integer such that 2x, 3x, 4x, 5x, and 6x contain the same digits."""
    x = 1
    while True:
        if all(sorted(str(x)) == sorted(str(x * multiplier)) for multiplier in range(2, 7)):
            return x
        x += 1

# Example usage
print(find_smallest_integer_with_same_digits())