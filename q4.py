# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ``

def compare(a,b):
    if len(a) > len(b):
        print(f'{a} is longer than {b}')
    elif len(b) > len(a):
        print(f'{b} is longer than {a}')



word1 = input('enter first string')
word2 = input('enter second string')
print(compare(word1,word2))
