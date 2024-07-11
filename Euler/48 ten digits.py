#written using Cursor AI tool

def last_ten_digits_of_series_sum(n):
    """Find the last ten digits of the sum of the series of n^n."""
    series_sum = sum([pow(i, i, 10**10) for i in range(1, n+1)])
    return series_sum % (10**10)

print(last_ten_digits_of_series_sum(1000))