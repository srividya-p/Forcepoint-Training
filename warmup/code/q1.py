# QUESTION 1

# Write an algorithm to reverse a character array. Method signature: public char [] reverse
# (char [] input).

# Note:
# 1.It is not allowed to use any inbuilt language function
# 2. it is not allowed to use any temporary array
# 3. Basically it should be an in place reversal

def reverse(char_list):
    n = len(char_list)
    for i in range(n // 2):
        temp = char_list[i]
        char_list[i] = char_list[n- 1 - i]
        char_list[n- 1 - i] = temp
    return char_list
