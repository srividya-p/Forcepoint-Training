# QUESTION 5

# Find the sum of all the numbers that can be written as the sum of fifth powers of their
# digits.

# UPPER BOUND
# Till which point is the smallest n digit number (10 ^ n-1) less than the 
# largest n digit number's sum of 5th powers (9^5 + 9^5 + 9^5 ...  = n*9^5)?
# Once it becomes greater, there is no scope of the number and it's 5th power sum being equal.

n = 1
while(10 ** n-1 < n * 9**5):
    n += 1

upper = n * 9**5 #Precise, Approx = 10 ** n

#LOWER BOUND
# Similarly, till which point is the smallest n digit number's sum of 5th powers 
# (n*2^5, 1 is ignored as per question) greater than the smallest n digit number?
# As long as it is lesser, it can't be equal to the sum of 5th powers.

n = 1
while(n * 2**5 > 10 ** n-1):
    n += 1

lower = n * 2**5 #Precise, Approx = 10 ** n


def get5thPowSum():
    allPowSum = 0
    for i in range(lower, upper+1):
        num, powSum = i, 0
        while num > 0:
            powSum += (num % 10) ** 5
            num = num // 10

        if i == powSum:
            allPowSum += powSum
    return allPowSum





