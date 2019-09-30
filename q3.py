# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```
mergeArray = []
temp = []

for x in list_of_claim_nums_2:
    print(x)


for i in temp:
    print(i)


for eachEl in list_of_claim_nums_1:
    mergeArray.append(eachEl)
    mergeArray.append(temp)

for








# for i in list_of_claim_nums_2:
#     temp.append(i)

print(mergeArray)

# I want nums 2 to be in between nums 1 // second array then 1st array

# merge = []
# for i in merge:
#     merge.append(list_of_claim_nums_1)
#     merge.append(list_of_claim_nums_2)
#     print(merge)

