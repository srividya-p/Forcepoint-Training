#QUESTION 7

# Given two sorted arrays in ascending order , write a function which takes both as input
# and returns an array of common elements.
# A = [1,3,4,6,7,9]
# B = [1,2,4,5,9,10]
# OutputArray: [1,4,9]
# Note: Solution should be in O(n)

def intersection(num_arr1, num_arr2):
    s = set(num_arr1)
    result = set()
    for n in num_arr2:
        if n in s:
            result.add(n)
    
    return list(result)


    