import bisect

def maximumSum(a, m):
    # Initialize prefix sum and maximum result
    prefix_sum = 0
    max_sum = 0
    prefix_sums = []  # Use a list to store prefix sums mod m

    for num in a:
        prefix_sum = (prefix_sum + num) % m  # Update the prefix sum mod m
        max_sum = max(max_sum, prefix_sum)    # Update max_sum with current prefix sum
        
        # Use binary search to find the first prefix sum that is >= prefix_sum
        pos = bisect.bisect_left(prefix_sums, prefix_sum + 1)
        
        # If there's a valid prefix sum that can maximize the result
        if pos < len(prefix_sums):
            current_sum = (prefix_sum - prefix_sums[pos] + m) % m
            max_sum = max(max_sum, current_sum)
        
        # Add the current prefix sum to the sorted list
        bisect.insort(prefix_sums, prefix_sum)
    
    return max_sum

# Example usage
a = [3, 3, 9, 9, 5]
m = 7
print(maximumSum(a, m))  # Output: 6
