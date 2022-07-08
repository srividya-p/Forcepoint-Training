# QUESTION 2

# Find number of occurrences of each number from the array. Every number is in the range [0....100].
# Public void numberOfOccurences (int [] input){ //logic }

# Note: expecting O(n) solution which means no sorting or nested loops allowed

def numberOfOccurences(num_arr):
    frequency = dict()

    for n in num_arr:
        if n in frequency: 
            frequency[n] += 1
        else: 
            frequency[n] = 1

    return frequency
