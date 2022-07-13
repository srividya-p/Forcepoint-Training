from stack import Stack

# Reverse
def reverse(s):
    rev, st = '', Stack(s)
    while not st.isEmpty(): rev += st.pop()
    return rev

# Reverse words
def reverseWords(s):
    rev = ''
    for word in s.split():
        rev += reverse(word) + ' '
    return rev

inputString = input('Enter a string - ')
print(reverse(inputString))
print(reverseWords(inputString))

#Who let the dogs out