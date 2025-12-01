# Make your own list and print the largest number present in that list

my_list = [51,85,1748,52,44,100,200]
largest = 0

# Iterate by Value
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)


# Iterate by Index

# for i in range(0,len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(largest)


# -----------Issue with -ve Numbers ( So, Consider the element at 0 position is largest and then start comparing) ------

my_list = [-3,-4,-1,-2]
largest = my_list[0]

for i in range(0,len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)