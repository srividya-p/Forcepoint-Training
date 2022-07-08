# QUESTION 3

# Find first maximum and second maximum number from an integer array
# Note : expecting O(n) solution which means no sorting or nested loops allowed

def firstSecondMax(num_arr):
    
    first = second = num_arr[0]

    for n in num_arr:
        if n > first:
            second = first
            first = n
        elif n > second and n < first:
            second = n

    return [first, None] if first == second else [first, second]