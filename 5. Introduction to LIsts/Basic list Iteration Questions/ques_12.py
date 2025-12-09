# Make your own list and print the smallest number present in that list

my_list = [51,85,1748,52,44,100,200]
smallest = 0

# Iterate by Value
# for i in my_list:
#     if i < smallest:
#         smallest = i
# print(smallest)


# Iterate by Index

# for i in range(0,len(my_list)):
#     if my_list[i] < smallest:
#         smallest = my_list[i]
# print(smallest)


# -----------Issue with -ve Numbers ( So, Consider the element at 0 position is largest and then start comparing) ------

my_list = [-3,-4,-1,-2]
smallest = my_list[0]

for i in range(0,len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]
print(smallest)