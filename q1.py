# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List

# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```
# Using the provided list of numbers, use a for loop to iterate the array
# and print out all the values that are smaller than the user input
# and print out all the values that are larger than the number entered by the user.

list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]


def compare(a):
    for i in list_of_many_numbers:
        if i > a:
            print(i)
compare(30)

def compare2(b):
    for el in list_of_many_numbers:
        if el < b:
            print(el)
compare2(15)




# for i in list_of_many_numbers:
#     if i > num:
#         print(i)
#     elif i < num:
#         print(i)


# for eachEl in list_of_many_numbers:
#     if eachEl > list_of_many_numbers:
#         print(eachEl)

# for i in list_of_many_numbers:
#     if i > enterNum:
#         print(i)
