# QUESTION 4

# roundOff a float number having only one decimal place (3.2 = 3; 4.8 =5 etc)
# Note: It is not allowed to use any inbuilt language function.

def roundOff(n):
    n = int(n - 0.5)
    return n + 1