# Make your own list and print the sum of all elements present in that list.

my_list = [51, 85, 91.66, 52, 44, 100, 200]
total = 0

# Iterate by Value
# for i in my_list:
#     total = total + i
# print(total)



# Iterate by Index
for i in range(0,len(my_list)):
    total = my_list[i] + total
print(total)