#QUESTION 6

# Write a function that takes in an integer array and returns the item that occurs most
# often.
# int Most_frequent(inputArray [])
# If n is an input element in the array the possible values for n 1 ≤ n ≤ 100
# Note: Solution should be in O(n)

import sys

MIN_VALUE = -sys.maxsize - 1

def mostFrequent(num_arr):
    frequency = dict()

    for n in num_arr:
        if n in frequency: 
            frequency[n] += 1
        else: 
            frequency[n] = 1

    maxKey = num_arr[0]
    maxCount = frequency[maxKey]

    for key in frequency:
        if frequency[key] > maxCount:
            maxCount = frequency[key]
            maxKey = key
    
    return maxKey